"""
File driver utama, bertanggung jawab atas user input dan display (Main file driver, responsible for user input and display)
"""
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
sys.getwindowsversion()
import pygame as p
from tkinter import *
import GUI
from importlib.machinery import SourceFileLoader

ModuleName = GUI.maingui()
module = SourceFileLoader(ModuleName, "Include/" + ModuleName + ".py").load_module()

WindowHeight = (800//module.Dimensi2)*module.Dimensi2
WindowWidth = (WindowHeight//module.Dimensi2)*module.Dimensi
MoveWidth = 300
MoveHeight = WindowHeight
Dimension = module.Dimensi
Dimension2 = module.Dimensi2
Theme = module.Theme
Ukr_Petak = WindowHeight//Dimension2
FPSMaks = 30  # buat animasi (for animation, though animation is not implemented yet)
Images = {}

'''
memulai kamus global gambar, akan dipanggil hanya sekali (global dictionary for images, called only once)
'''


def loadimages():
    pieces = module.Pieces
    for bidak in pieces:
        Images[bidak] = p.transform.scale(p.image.load(Theme + bidak + ".png"), (Ukr_Petak, Ukr_Petak))
    # gambar bisa dipanggil dengan bilang Images['bidak']


'''
driver utama kode, akan menghandle user input (main driver code, handles user input)
'''


def main():
    p.display.set_caption(ModuleName)
    programIcon = p.image.load("Textures/Tjatoer!/wG.png")
    p.display.set_icon(programIcon)
    # variables
    p.init()
    screen = p.display.set_mode((WindowWidth + MoveWidth, WindowHeight))
    clock = p.time.Clock()
    screen.fill(p.Color("#202020"))
    movelogfont = p.font.Font("Fonts/RobotoMono-Medium.ttf", 12)
    gs = module.GameState()
    validmoves = gs.getvalidmoves()
    movemade = False
    moveundone = False
    loadimages()  # sebelum while loop (before the while loop)
    running = True
    sqselected = ()  # tdk ada petak yang dipilih, mencatat petak yang user klik (row, col) (no square selected, records selected squares in (row, col))
    playerclicks = []  # mencatat klik user [(row,col),(row,col)] (records user clicks in [(row, col), (row, col)])
    move = ()
    gameover = False
    moveundone = False
    movelist = []
    movedup = []
    sound = p.mixer.Sound("Sounds/gamestart.mp3")
    sound.play()

    # statement utama (main statement)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                sys.exit()
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameover:
                    location = p.mouse.get_pos()  # lokasi pointer mouse (mouse pointer location)
                    col = location[0]//Ukr_Petak
                    row = location[1]//Ukr_Petak
                    if e.button == 1:
                        if (sqselected == (row, col) and gs.board[row][col] != '--') or col >= module.Dimensi or row >= module.Dimensi2:
                            sqselected = ()  # biar gabisa diklik 2 kali (so that the user can't click the same square twice)
                            playerclicks = []  # biar gabisa diklik 2 kali (so that the user can't click the same square twice)
                        else:
                            sqselected = (row, col)
                            playerclicks.append(sqselected)
                        if len(playerclicks) == 1:
                            movenota = []
                            movedup = []
                            for m in validmoves:
                                movenota.append(str(m))
                                anydup(movenota, movedup)
                        if len(playerclicks) == 2:  # setelah klik kedua (after the second click)
                            move = module.Move(playerclicks[0], playerclicks[1], gs.board)
                            for i in range(len(validmoves)):
                                if move == validmoves[i]:
                                    gs.makemove(validmoves[i])
                                    movemade = True
                                    moveundone = False
                                    sqselected = ()
                                    playerclicks = []
                                    checksandstuff(gs, move, movelist, validmoves)
                                    if move.mustpromote:
                                        if gs.promotionfail:
                                            moveundone = True
                                    for md in movedup:
                                        if str(move) == md:
                                            if len(movelist) != 0:
                                                del movelist[-1]
                                            else:
                                                movelist = []
                                            if gs.incheck():
                                                if move.iscapture:
                                                    movelist.append(move.piecemoved[1:] + move.startsquare + 'x' + move.endsquare + '+')
                                                else:
                                                    movelist.append(move.piecemoved[1:] + move.startsquare + move.endsquare + '+')
                                            if not gs.incheck():
                                                if move.iscapture:
                                                    movelist.append(move.piecemoved[1:] + move.startsquare + 'x' + move.endsquare)
                                                else:
                                                    movelist.append(move.piecemoved[1:] + move.startsquare + move.endsquare)
                            if not movemade:
                                playerclicks = [sqselected]
                    if e.button == 3:
                        if len(playerclicks) == 1:
                            playerclicks = []
                            sqselected = ()
                            bidak = gs.board[row][col][1:]
                            if bidak != '-' and bidak != 'BL':
                                movediagram(gs, col, bidak)
            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo ketika tekan z (undo when z is pressed)
                    gs.undodrop()
                    gameover = False
                    movemade = True
                    gs.undomove()
                    if len(movelist) != 0:
                        del movelist[-1]
                    else:
                        pass
                if e.key == p.K_r:
                    p.display.quit()
                    main()
                    sys.exit()

        drawgamestate(screen, gs, validmoves, sqselected, movelist, movelogfont)

        if gs.checkmate or gs.stalemate:
            gameover = True
            if gs.checkmate:
                if len(movelist) != 0:
                    del movelist[-1]
                else:
                    movelist = []
                movelist.append(str(move) + "#")
                for md in movedup:
                    if str(move) == md:
                        if len(movelist) != 0:
                            del movelist[-1]
                        else:
                            movelist = []
                        if move.iscapture:
                            movelist.append(move.piecemoved[1:] + move.startsquare + 'x' + move.endsquare + '#')
                        else:
                            movelist.append(move.piecemoved[1:] + move.startsquare + move.endsquare + '#')
            drawendgametext(screen, 'REMIS!' if gs.stalemate else 'SKAKMAT! HITAM MENANG' if gs.whitetomove else 'SKAKMAT! PUTIH MENANG')

        if movemade:
            # telah terbuatnya langkah (a move is made)
            validmoves = gs.getvalidmoves()
            playsound(move, gs, moveundone)
            movemade = False
        clock.tick(FPSMaks)
        p.display.flip()


'''
bertugas menggambar grafik pada permainan (is tasked with drawing the graphics of the game)
'''


def drawgamestate(screen, gs, validmoves, sqselected, movelist, movelogfont):
    drawboard(screen)  # menggambar petak pada papan (draws squares on the board)
    highlightsquares(screen, gs, validmoves, sqselected, movelist)
    drawpieces(screen, gs.board)  # menggmbar bidak diatas petak (puts the pieces on the squares)
    drawmovelog(screen, movelist, movelogfont)


'''
bertugas memainkan suara (is tasked with playing the game sounds)
'''


def playsound(move, gs, moveundone):
    if not moveundone:
        if gs.checkmate:
            sound = p.mixer.Sound("Sounds/checkmate.mp3")
            sound.play()
        elif gs.stalemate:
            sound = p.mixer.Sound("Sounds/stalemate.mp3")
            sound.play()
        elif gs.incheck():
            sound = p.mixer.Sound("Sounds/check.mp3")
            sound.play()
        else:
            if len(gs.movelog) >= 1:
                m = gs.movelog[-1]
                if m.enpassant:
                    if move == m:
                        sound = p.mixer.Sound("Sounds/capture.mp3")
                        sound.play()
                if m.castle:
                    if move == m:
                        sound = p.mixer.Sound("Sounds/castling.mp3")
                        sound.play()
                if m.iscapture:
                    if move == m:
                        sound = p.mixer.Sound("Sounds/capture.mp3")
                        sound.play()
                if not m.enpassant and not m.castle and not m.iscapture:
                    if move == m:
                        sound = p.mixer.Sound("Sounds/move.mp3")
                        sound.play()


'''
menggambar petak (draws the squares)
'''


def drawboard(screen):
    warnawarna = [p.Color("#FFCE9E"), p.Color("#D18B47")]
    for r in range(Dimension2):
        for c in range(Dimension):
            warna = warnawarna[((r + c) % 2)]
            p.draw.rect(screen, warna, p.Rect(c*Ukr_Petak, r*Ukr_Petak, Ukr_Petak, Ukr_Petak))


'''
highlight petak (highlights the squares)
'''


def highlightsquares(screen, gs, validmoves, sqselected, movelist):
    s = p.Surface((Ukr_Petak, Ukr_Petak))
    movecircle = p.transform.scale(p.image.load("Textures\GUI\movecircle.png"), (Ukr_Petak, Ukr_Petak))
    capturecircle = p.transform.scale(p.image.load("Textures\GUI\capturecircle.png"), (Ukr_Petak, Ukr_Petak))
    if (len(gs.movelog)) > 0:
        lastmove = gs.movelog[-1]
        s.set_alpha(255)
        s.fill(p.Color('#ffbc40'))
        if lastmove.piecemoved != '--':
            screen.blit(s, (lastmove.endcol*Ukr_Petak, lastmove.endrow*Ukr_Petak))
        elif len(movelist) >= 1:
            lastlist = movelist[-1]
            if '*' in lastlist:
                screen.blit(s, (lastmove.endcol*Ukr_Petak, lastmove.endrow*Ukr_Petak))

    if sqselected != ():
        r, c = sqselected
        theirturn = gs.board[r][c][0] == ('w' if gs.whitetomove else 'b')
        if gs.board[r][c][1] != '-':  # petak yg dipilih adalah bidak yg bisa jalan (selected square is a piece that is able to move)
            # highlight petak
            s.set_alpha(255)  # trasparansi (transparancy)
            s.fill(p.Color('#ffe08a' if theirturn else '#ffb091'))
            screen.blit(s, (c*Ukr_Petak, r*Ukr_Petak))
            # highlight langkah
            for move in validmoves:
                if move.startrow == r and move.startcol == c:
                    if not move.iscapture:
                        screen.blit(movecircle, (move.endcol*Ukr_Petak, move.endrow*Ukr_Petak))
                    else:
                        screen.blit(capturecircle, (move.endcol*Ukr_Petak, move.endrow*Ukr_Petak))


'''
menggambar bidak (draws the pieces)
'''


def drawpieces(screen, board):
    for r in range(Dimension2):
        for c in range(Dimension):
            bidak = board[r][c]
            if bidak != "--":
                screen.blit(Images[bidak], p.Rect(c*Ukr_Petak, r*Ukr_Petak, Ukr_Petak, Ukr_Petak))
    module.board(screen, Ukr_Petak)


"""
movelog (draws the movelog)
"""


def drawmovelog(screen, movelist, font):
    movelogrect = p.Rect(WindowWidth, 0, MoveWidth, MoveHeight)
    p.draw.rect(screen, p.Color('#202020'), movelogrect)
    movelog = movelist
    movetexts = []
    for i in range(0, len(movelog), 2):
        movestring = str(i//2 + 1) + "." + str(movelog[i]) + " "
        if i + 1 < len(movelog):  # memastikan hitam sudah jalan (makes sure that black has made a move)
            movestring += str(movelog[i + 1]) + "  "
        movetexts.append(movestring)
    movesperrow = 2
    padding = 5
    texty = padding
    linespacing = 2
    for i in range(0, len(movetexts), movesperrow):
        text = ""
        for j in range(movesperrow):
            if i + j < len(movetexts):
                text += movetexts[i + j]
        textobject = font.render(text, True, p.Color('White'))
        textlocation = movelogrect.move(padding, texty)
        screen.blit(textobject, textlocation)
        texty += textobject.get_height() + linespacing


'''
menggambar text (draws the game over text)
'''


def drawendgametext(screen, text):
    font = p.font.Font("Fonts/HelveticaNeueLTStd-Blk.otf", 50)
    textobject = font.render(text, True, p.Color('black'))
    textlocation = p.Rect(0, 0, WindowWidth, WindowHeight).move(WindowWidth/2 - textobject.get_width()/2,
                                                                WindowHeight/2 - textobject.get_height()/2)
    screen.blit(textobject, textlocation)


def movediagram(gs, col, bidak):
    if col <= len(gs.board[0]):
        Window = Tk()
        bg = "#202020"
        bg2 = "#303030"
        fg = "White"

        Window.iconbitmap("Textures/GUI/Folder.ico")
        Window.configure(bg=bg)
        Window.resizable(False, False)
        Window.title(module.PieceNames[bidak])

        frameone = LabelFrame(Window, bg=bg2, borderwidth=0)
        frameone.grid(row=1, column=0)

        ChessM = PhotoImage(file=Theme + "Piece Move Diagrams/" + module.PieceNames[bidak] + " Moves.png")
        InfoM = PhotoImage(file="Textures/GUI/info.png")
        PieceMW = PhotoImage(file=Theme + "Piece Move Diagrams/" + "w" + bidak + ".png")
        PieceMB = PhotoImage(file=Theme + "Piece Move Diagrams/" + "b" + bidak + ".png")

        Label(Window, text=("The " + module.PieceNames[bidak]), bg="#202020", fg=fg,
              font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
        Label(frameone, image=PieceMW, bg=bg2, fg=fg, borderwidth=0).grid(row=1, column=0, sticky='e')
        Label(frameone, image=PieceMB, bg=bg2, fg=fg, borderwidth=0).grid(row=1, column=1, sticky='w')
        Label(frameone, image=ChessM, bg=bg2, fg=fg, borderwidth=0).grid(row=2, column=0, columnspan=2)
        Label(frameone, image=InfoM, bg=bg2, fg=fg, borderwidth=0).grid(row=3, column=0, columnspan=2)
        cancelB = PhotoImage(file="Textures/GUI/cancel.png")
        close = Button(Window, image=cancelB, borderwidth=0, bg="#202020", activebackground="#202020",
                       command=Window.destroy, height=100)
        close.grid(row=4, column=0, columnspan=2)

        awi = 500
        ahe = 950
        swi = Window.winfo_screenwidth()
        she = Window.winfo_screenheight()
        x = (swi/2) - (awi/2)
        y = (she/2) - (ahe/2)
        Window.geometry('+%d+%d'%(x, y))

        Window.overrideredirect(1)
        Window.mainloop()


def checksandstuff(gs, move, movelist, validmoves):
    if move.canpromote:
        gs.getpromotion(move)
    if move.mustpromote:
        gs.getpromotion(move)
        if gs.promotionfail:
            gs.undomove()
    if move.drop:
        gs.getdrop(move)
    movelist.append(str(gs.movelog[-1]))
    if move.mustpromote:
        if gs.promotionfail:
            if len(movelist) != 0:
                del movelist[-1]
            else:
                movelist = []
    if move.drop:
        if gs.dropfail:
            if len(movelist) != 0:
                del movelist[-1]
            else:
                movelist = []
    if gs.incheck():
        if len(movelist) != 0:
            del movelist[-1]
        else:
            movelist = []
        movelist.append(str(gs.movelog[-1]) + "+")
    for m in validmoves:
        if m.enpassant:
            if move == m:
                if len(movelist) != 0:
                    del movelist[-1]
                else:
                    movelist = []
                movelist.append(move.startsqcol + 'x' + str(move) + ' e.p.')
        if m.castle:
            if move == m:
                if len(movelist) != 0:
                    del movelist[-1]
                else:
                    movelist = []
                if move.endcol - move.startcol > 0:
                    movelist.append('O-O')
                if move.endcol - move.startcol < 0:
                    movelist.append('O-O-O')


def anydup(daftar, movedup):
    seen = set()
    for x in daftar:
        if x in seen:
            movedup.append(x)
        seen.add(x)


if __name__ == "__main__":
    main()
