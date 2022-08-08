"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
from tkinter import *
import random


def board(screen, ukr):
    pass


Dimensi = 8
Dimensi2 = 8
Pieces = ['wB', 'bB', 'wK', 'bK', 'wN', 'bN', 'wP', 'bP', 'wQ', 'bQ', 'wR', 'bR', 'wBD', 'bBD', 'wCA', 'bCA', 'wWA',
          'bWA', 'wFA', 'bFA', 'wCR', 'bCR', 'wFN', 'bFN', 'wCN', 'bCN', 'wCO', 'bCO', 'wWR', 'bWR', 'wSR', 'bSR',
          'wHD', 'bHD', 'wCH', 'bCH']
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen', 'K': 'King', 'BD': 'Bede',
              'CA': 'Cardinal', 'WA': 'Waffle', 'FA': 'Fad', 'CR': 'Charging Rook', 'FN': 'Fibnif',
              'CN': 'Charging Knight', 'CO': 'Colonel', 'WR': 'Woody Rook', 'SR': 'Short Rook', 'HD': 'Half Duck',
              'CH': 'Chancellor'}
Theme = "Textures/CWDA/"
global Promotedpiece, WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces


def menu():
    global W, B
    # White pieces
    Root = Tk()
    Root.title("Options")
    Root.iconbitmap("Textures/GUI/wG.ico")
    Root.configure(bg="#202020")
    Root.resizable(False, False)

    awi = 325
    ahe = 380
    swi = Root.winfo_screenwidth()
    she = Root.winfo_screenheight()
    x = (swi/2) - (awi/2)
    y = (she/2) - (ahe/2)

    Root.geometry(f'{awi}x{ahe}+{int(x)}+{int(y)}')

    BB = PhotoImage(file=Theme + "BLB.png")
    BW = PhotoImage(file=Theme + "BLW.png")
    CCB = PhotoImage(file=Theme + "CCB.png")
    CCW = PhotoImage(file=Theme + "CCW.png")
    FFB = PhotoImage(file=Theme + "FFB.png")
    FFW = PhotoImage(file=Theme + "FFW.png")
    RRB = PhotoImage(file=Theme + "RRB.png")
    RRW = PhotoImage(file=Theme + "RRW.png")
    KKB = PhotoImage(file=Theme + "KKB.png")
    KKW = PhotoImage(file=Theme + "KKW.png")

    OptionsArmyW = {"Colourbound Cloberers": CCW, "Knutty Knights": KKW, "Fabulous FIDEs": FFW, "Remarkable Rookies": RRW}
    OptionsArmyB = {"Colourbound Cloberers": CCB, "Knutty Knights": KKB, "Fabulous FIDEs": FFB, "Remarkable Rookies": RRB}

    frameone = LabelFrame(Root, bg="#303030", borderwidth=0)
    frametwo = LabelFrame(Root, bg="white", borderwidth=0)
    frameone.grid(row=0, column=0, padx=10, columnspan=2)
    frametwo.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

    LW = Label(frametwo, image=BW, bg="white", fg="black")
    LW.grid(column=0, row=0)
    LB = Label(frameone, image=BB, bg="#303030", fg="White")
    LB.grid(column=0, row=0)

    W = False
    B = False

    def IW(event):
        global W, B
        W = True
        LW.configure(image=OptionsArmyW[clickedW.get()])
        if B:
            close.configure(image=okayB)

    def IB(event):
        global W, B
        B = True
        LB.configure(image=OptionsArmyB[clickedB.get()])
        if W:
            close.configure(image=okayB)

    def sel():
        global WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces
        WhitePieces = OptionsWhite[clickedW.get()]
        WhiteArmyPieces = OptionsArmy[clickedW.get()]
        BlackPieces = OptionsBlack[clickedB.get()]
        BlackArmyPieces = OptionsArmy[clickedB.get()]
        Root.destroy()
        return WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces

    def rand():
        Bl = random.choice(Options)
        Wh = random.choice(Options)
        clickedW.set(Wh)
        clickedB.set(Bl)

        global WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces
        WhitePieces = OptionsWhite[clickedW.get()]
        WhiteArmyPieces = OptionsArmy[clickedW.get()]
        BlackPieces = OptionsBlack[clickedB.get()]
        BlackArmyPieces = OptionsArmy[clickedB.get()]
        LB.configure(image=OptionsArmyB[clickedB.get()])
        LW.configure(image=OptionsArmyW[clickedW.get()])
        close.configure(image=okayB)
        return WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces

    def ext():
        global WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces
        WhitePieces = None
        WhiteArmyPieces = None
        BlackPieces = None
        BlackArmyPieces = None
        Root.destroy()
        return WhitePieces, WhiteArmyPieces, BlackPieces, BlackArmyPieces

    OptionsWhite = {"Colourbound Cloberers": ["wBD", "wWA", "wFA", "wCA", "wK", "wFA", "wWA", "wBD"], "Fabulous FIDEs": ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"], "Knutty Knights": ["wCR", "wFN", "wCN", "wCO", "wK", "wCN", "wFN", "wCR"], "Remarkable Rookies": ["wSR", "wWR", "wHD", "wCH", "wK", "wHD", "wWR", "wSR"]}

    OptionsBlack = {"Colourbound Cloberers": ["bBD", "bWA", "bFA", "bCA", "bK", "bFA", "bWA", "bBD"], "Fabulous FIDEs": ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], "Knutty Knights": ["bCR", "bFN", "bCN", "bCO", "bK", "bCN", "bFN", "bCR"], "Remarkable Rookies": ["bSR", "bWR", "bHD", "bCH", "bK", "bHD", "bWR", "bSR"]}

    OptionsArmy = {"Colourbound Cloberers": "CC", "Knutty Knights": "KK", "Fabulous FIDEs": "FF", "Remarkable Rookies": "RR"}

    Options = ["Colourbound Cloberers", "Knutty Knights", "Fabulous FIDEs", "Remarkable Rookies"]

    clickedW = StringVar()
    clickedW.set("Pilih set bidak untuk Putih")
    clickedB = StringVar()
    clickedB.set("Pilih set bidak untuk Hitam")

    comboW = OptionMenu(frametwo, clickedW, *Options, command=IW)
    comboW.grid(column=0, row=3, padx=10, pady=10)
    comboW.config(bg="white", borderwidth=1, activebackground="white", fg="black", activeforeground="black", highlightthickness=0)

    comboB = OptionMenu(frameone, clickedB, *Options, command=IB)
    comboB.grid(column=0, row=1, padx=10, pady=10)
    comboB.config(bg="#303030", borderwidth=1, activebackground="#303030", fg="white", activeforeground="white", highlightthickness=0)

    okayB = PhotoImage(file="Textures/GUI/okay.png")
    cancelB = PhotoImage(file="Textures/GUI/cancel.png")
    randomB = PhotoImage(file="Textures/GUI/random.png")
    close = Button(Root, image=cancelB, borderwidth=0, bg="#202020", activebackground="#202020", command=sel)
    close.grid(row=3, column=0)
    Button(Root, image=randomB, borderwidth=0, bg="#202020", activebackground="#202020", command=rand).grid(row=3, column=1)

    Root.protocol("WM_DELETE_WINDOW", ext)
    Root.mainloop()


class GameState:
    def __init__(self):
        menu()
        # papan caturnya daftar 2 dimensional, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is 8x8, every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            BlackPieces,
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            WhitePieces]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'Q': self.getqueenmoves, 'K': self.getkingmoves,
                             'BD': self.getbedemoves, 'CA': self.getcardinalmoves, 'WA': self.getwafflemoves,
                             'FA': self.getfadmoves, 'CR': self.getchargingrookmoves, 'FN': self.getfibnifmoves,
                             'CN': self.getchargingknightmoves, 'CO': self.getcolonelmoves,
                             'WR': self.getwoodyrookmoves, 'SR': self.getshortrookmoves, 'HD': self.gethalfduckmoves,
                             'CH': self.getchancellormoves}
        self.whitetomove = True
        self.movelog = []
        self.movelist = []
        self.whitekinglocation = (7, 4)
        self.blackkinglocation = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.promotionfail = True
        self.dropfail = True
        self.enpassantpossible = ()
        self.enpassantpossiblelog = [self.enpassantpossible]
        self.currentcastlerights = Castlerights(True, True, True, True)
        self.currentcastlerightslog = [Castlerights(self.currentcastlerights.wks, self.currentcastlerights.bks,
                                                    self.currentcastlerights.wqs, self.currentcastlerights.bqs)]

    '''
    mengambil langkah sebagai parameter kemudian mengeksekusinya (takes a move as a parameter and makes that move, this is used to check for checks)
    '''

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move)  # mencatat langkah biar bisa diundo (records the move so it can be undone)
        self.movelist.append(str(move))
        self.whitetomove = not self.whitetomove  # gantian giliran (changes the turn)
        if move.piecemoved == 'wK':
            self.whitekinglocation = (move.endrow, move.endcol)
        elif move.piecemoved == 'bK':
            self.blackkinglocation = (move.endrow, move.endcol)

        # update en passant rights
        if move.enpassant:
            self.board[move.startrow][move.endcol] = '--'

        if move.piecemoved[1] == 'P' and abs(move.startrow - move.endrow) == 2:
            self.enpassantpossible = ((move.startrow + move.endrow)//2, move.endcol)
        else:
            self.enpassantpossible = ()
        self.enpassantpossiblelog.append(self.enpassantpossible)

        # castling
        if move.castle:
            if move.endcol - move.startcol == 2:
                self.board[move.endrow][move.endcol - 1] = self.board[move.endrow][move.endcol + 1]
                self.board[move.endrow][move.endcol + 1] = '--'
            else:
                if move.endcol - move.startcol == -2:
                    self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 2]
                    self.board[move.endrow][move.endcol - 2] = '--'
                if move.endcol - move.startcol == -3:
                    self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 1]
                    self.board[move.endrow][move.endcol - 1] = '--'
        self.updatecastlerights(move)
        self.currentcastlerightslog.append(Castlerights(self.currentcastlerights.wks, self.currentcastlerights.bks,
                                                        self.currentcastlerights.wqs, self.currentcastlerights.bqs))

    '''
    undo lngkah terakhir (undo the last move)
    '''

    def undomove(self):
        if len(self.movelog) != 0:  # biar ada yg bisa diundo
            move = self.movelog.pop()
            self.movelist.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            self.board[move.endrow][move.endcol] = move.piececaptured
            self.whitetomove = not self.whitetomove
            if move.piecemoved == 'wK':
                self.whitekinglocation = (move.startrow, move.startcol)
            elif move.piecemoved == 'bK':
                self.blackkinglocation = (move.startrow, move.startcol)

            if move.enpassant:
                self.board[move.endrow][move.endcol] = '--'
                self.board[move.startrow][move.endcol] = move.piececaptured

            self.enpassantpossiblelog.pop()
            self.enpassantpossible = self.enpassantpossiblelog[-1]

            # castle
            self.currentcastlerightslog.pop()
            newrights = self.currentcastlerightslog[-1]
            self.currentcastlerights = Castlerights(newrights.wks, newrights.bks, newrights.wqs, newrights.bqs)

            if move.castle:
                if move.endcol - move.startcol == 2:
                    self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 1]
                    self.board[move.endrow][move.endcol - 1] = '--'
                else:
                    if move.endcol - move.startcol == -2:
                        self.board[move.endrow][move.endcol - 2] = self.board[move.endrow][move.endcol + 1]
                        self.board[move.endrow][move.endcol + 1] = '--'
                    if move.endcol - move.startcol == -3:
                        self.board[move.endrow][move.endcol - 1] = self.board[move.endrow][move.endcol + 1]
                        self.board[move.endrow][move.endcol + 1] = '--'

            self.checkmate = False
            self.stalemate = False

    """
    updates the castle rights
    """
    def updatecastlerights(self, move):
        if move.piecemoved == 'wK':
            self.currentcastlerights.wks = False
            self.currentcastlerights.wqs = False
        elif move.piecemoved == 'bK':
            self.currentcastlerights.bks = False
            self.currentcastlerights.bqs = False
        elif (move.piecemoved == 'wR') or (move.piecemoved == 'wSR') or (move.piecemoved == 'wBD') or (move.piecemoved == 'wCR'):
            if move.startrow == 7:
                if move.startcol == 0:
                    self.currentcastlerights.wqs = False
                elif move.startcol == 7:
                    self.currentcastlerights.wks = False
        elif (move.piecemoved == 'bR') or (move.piecemoved == 'bSR') or (move.piecemoved == 'bBD') or (move.piecemoved == 'bCR'):
            if move.startrow == 0:
                if move.startcol == 0:
                    self.currentcastlerights.bqs = False
                elif move.startcol == 7:
                    self.currentcastlerights.bks = False
        if move.piececaptured == 'wR' or move.piececaptured == 'wSR' or move.piececaptured == 'wBD' or move.piececaptured == 'wCR':
            if move.endcol == 0:
                self.currentcastlerights.wqs = False
            elif move.endcol == 7:
                self.currentcastlerights.wks = False
        elif move.piececaptured == 'bR' or move.piececaptured == 'bSR' or move.piececaptured == 'bBD' or move.piececaptured == 'bCR':
            if move.endcol == 0:
                self.currentcastlerights.bqs = False
            elif move.endcol == 7:
                self.currentcastlerights.bks = False

    '''
    semua langkah termasuk skak (all moves including checks)
    '''

    def getvalidmoves(self):
        tempenpassantpossible = self.enpassantpossible
        tempcastlerights = Castlerights(self.currentcastlerights.wks, self.currentcastlerights.bks,
                                        self.currentcastlerights.wqs, self.currentcastlerights.bqs)
        # 1. membuat semua langkah yang mungkin (makes all possible moves)
        moves = self.getallpossibledmoves()
        # 2. membuat semua langkah lawan yang mungkin (makes all possible opponent moves)
        for i in range(len(moves) - 1, -1, -1):
            self.makemove(moves[i])
            # 3. cek kallo raja kita lg diserang (checks if the king is in danger)
            self.whitetomove = not self.whitetomove
            if self.incheck():
                moves.remove(moves[i])  # 4. kalau ya maka tdk valid (if the king is in danger then the move is invalid)
            self.whitetomove = not self.whitetomove
            self.undomove()
        if len(moves) == 0:
            # antara skakmat atau stalemate (determines whether its checkmate or stalemate)
            if self.incheck():
                self.checkmate = True
            else:
                self.stalemate = True

        elif len(self.movelog) > 10:
            if (self.movelog[-1] == self.movelog[-5] == self.movelog[-9]) and (self.movelog[-2] == self.movelog[-6] == self.movelog[-10]):
                self.stalemate = True

        else:
            self.checkmate = False
            self.stalemate = False

        # 50 move rule
        captures = []
        pawnmoves = []
        signal = 'x'
        for i in range(1, 100):
            if len(self.movelist) >= 100:
                captures.append(str(self.movelist[-i]))
                pawnmoves.append(str(self.movelist[-i][0]))
        capturestring = ""
        firstletter = ""
        for e in captures:
            capturestring += e
        for p in pawnmoves:
            firstletter += p
        if signal not in capturestring:
            if firstletter.isupper():
                self.stalemate = True
        if self.whitetomove:
            self.getcastlemoves(self.whitekinglocation[0], self.whitekinglocation[1], moves)
        else:
            self.getcastlemoves(self.blackkinglocation[0], self.blackkinglocation[1], moves)

        self.enpassantpossible = tempenpassantpossible
        self.currentcastlerights = tempcastlerights
        return moves

    '''
    tau kalau lagi skak (checks for checks)
    '''

    def incheck(self):
        if self.whitetomove:
            return self.squareunderattack(self.whitekinglocation[0], self.whitekinglocation[1])
        else:
            return self.squareunderattack(self.blackkinglocation[0], self.blackkinglocation[1])

    '''
    petak yg lagi diserang (squares that are under attack)
    '''

    def squareunderattack(self, r, c):
        self.whitetomove = not self.whitetomove
        oppmoves = self.getallpossibledmoves()
        self.whitetomove = not self.whitetomove
        for move in oppmoves:
            if move.endrow == r and move.endcol == c:  # petak yg sedang diserang
                return True
        return False

    '''
    semua langkah tidak termasuk skak (all moves not including checks)
    '''

    def getallpossibledmoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whitetomove) or (turn == 'b' and not self.whitetomove):
                    bidak = self.board[r][c][1:]
                    self.movefunction[bidak](r, c, moves)  # berdasarkan tipe bidak
        return moves

    '''
    semua langkah pion lalu memasukan ke daftar (gets all the pawn moves and adds those to the valid moves list to be filtered)
    '''

    def getpawnmoves(self, r, c, moves):
        if self.whitetomove:  # pion putih (white pawn)
            if self.board[r - 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                    moves.append(Move((r, c), (r - 2, c), self.board))
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
                elif (r - 1, c - 1) == self.enpassantpossible:
                    moves.append(Move((r, c), (r - 1, c - 1), self.board, enpassant=True))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))
                elif (r - 1, c + 1) == self.enpassantpossible:
                    moves.append(Move((r, c), (r - 1, c + 1), self.board, enpassant=True))

        else:  # pion hitam
            if self.board[r + 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                    moves.append(Move((r, c), (r + 2, c), self.board))
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
                elif (r + 1, c - 1) == self.enpassantpossible:
                    moves.append(Move((r, c), (r + 1, c - 1), self.board, enpassant=True))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))
                elif (r + 1, c + 1) == self.enpassantpossible:
                    moves.append(Move((r, c), (r + 1, c + 1), self.board, enpassant=True))

    '''
    semua langkah benteng lalu memasukan ke daftar (gets all the rook moves and adds those to the valid moves list to be filtered)
    '''

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah kuda lalu memasukan ke daftar (gets all the knight moves and adds those to the valid moves list to be filtered)
    '''

    def getknightmoves(self, r, c, moves):
        langkahkuda = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the bishop moves and adds those to the valid moves list to be filtered)
    '''

    def getbishopmoves(self, r, c, moves):
        directions = ((-1, -1), (1, -1), (1, 1), (-1, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # diagonal bebas (moves freely diagonally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah mentri lalu memasukan ke daftar (gets all the queen moves and adds those to the valid moves list to be filtered)
    '''

    def getqueenmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getrookmoves(r, c, moves)

    '''
    semua langkah raja lalu memasukan ke daftar (gets all the king moves and adds those to the valid moves list to be filtered)
    '''

    def getkingmoves(self, r, c, moves):
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(8):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah bede lalu memasukan ke daftar (gets all the bede moves and adds those to the valid moves list to be filtered)
    '''

    def getbedemoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        langkahkuda = ((-2, 0), (0, -2), (2, 0), (0, 2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah cardinal lalu memasukan ke daftar (gets all the cardinal moves and adds those to the valid moves list to be filtered)
    '''

    def getcardinalmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah waffle lalu memasukan ke daftar (gets all the waffle moves and adds those to the valid moves list to be filtered)
    '''

    def getwafflemoves(self, r, c, moves):
        langkahkuda = ((-2, -2), (-2, 2), (2, -2), (2, 2), (-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah fad lalu memasukan ke daftar (gets all the fad moves and adds those to the valid moves list to be filtered)
    '''

    def getfadmoves(self, r, c, moves):
        langkahkuda = ((-2, 0), (0, -2), (2, 0), (0, 2), (-1, 1), (-1, -1), (1, -1), (1, 1), (-2, -2), (-2, 2), (2, -2), (2, 2))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah charging rook lalu memasukan ke daftar (gets all the charging rook moves and adds those to the valid moves list to be filtered)
    '''

    def getchargingrookmoves(self, r, c, moves):
        if self.whitetomove:
            langkahkuda = ((1, -1), (1, 0), (1, 1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            directions = ((-1, 0), (0, -1), (0, 1))
            warnamusuh = "b" if self.whitetomove else "w"
            for d in directions:
                for i in range(1, len(self.board[0])):
                    endrow = r + d[0]*i
                    endcol = c + d[1]*i
                    if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                        endpiece = self.board[endrow][endcol]
                        if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                        elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                            break
                        else:  # bidak sendiri (blocked by own piece)
                            break
                    else:  # diluar papan (out of the board)
                        break
        else:
            langkahkuda = ((-1, -1), (-1, 0), (-1, 1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            directions = ((1, 0), (0, -1), (0, 1))
            warnamusuh = "b" if self.whitetomove else "w"
            for d in directions:
                for i in range(1, len(self.board[0])):
                    endrow = r + d[0]*i
                    endcol = c + d[1]*i
                    if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                        endpiece = self.board[endrow][endcol]
                        if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                        elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                            break
                        else:  # bidak sendiri (blocked by own piece)
                            break
                    else:  # diluar papan (out of the board)
                        break

    '''
    semua langkah fibnif lalu memasukan ke daftar (gets all the fibnif moves and adds those to the valid moves list to be filtered)
    '''

    def getfibnifmoves(self, r, c, moves):
        langkahkuda = ((-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 1), (-1, -1), (1, -1), (1, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah charging knight lalu memasukan ke daftar (gets all the charging knight moves and adds those to the valid moves list to be filtered)
    '''

    def getchargingknightmoves(self, r, c, moves):
        if self.whitetomove:
            langkahkuda = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, -1), (1, 0), (1, 1), (0, 1), (0, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahkuda = ((2, 1), (2, -1), (1, 2), (1, -2), (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah colonel lalu memasukan ke daftar (gets all the colonel moves and adds those to the valid moves list to be filtered)
    '''

    def getcolonelmoves(self, r, c, moves):
        if self.whitetomove:
            langkahkuda = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, -1), (1, 0), (1, 1), (-1, 1), (-1, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            directions = ((-1, 0), (0, -1), (0, 1))
            warnamusuh = "b" if self.whitetomove else "w"
            for d in directions:
                for i in range(1, len(self.board[0])):
                    endrow = r + d[0]*i
                    endcol = c + d[1]*i
                    if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                        endpiece = self.board[endrow][endcol]
                        if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                        elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                            break
                        else:  # bidak sendiri (blocked by own piece)
                            break
                    else:  # diluar papan (out of the board)
                        break
        else:
            langkahkuda = ((2, 1), (2, -1), (1, 2), (1, -2), (-1, -1), (-1, 0), (-1, 1), (1, 1), (1, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            directions = ((1, 0), (0, -1), (0, 1))
            warnamusuh = "b" if self.whitetomove else "w"
            for d in directions:
                for i in range(1, len(self.board[0])):
                    endrow = r + d[0]*i
                    endcol = c + d[1]*i
                    if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                        endpiece = self.board[endrow][endcol]
                        if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                        elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                            moves.append(Move((r, c), (endrow, endcol), self.board))
                            break
                        else:  # bidak sendiri (blocked by own piece)
                            break
                    else:  # diluar papan (out of the board)
                        break

    '''
    semua langkah woody rook lalu memasukan ke daftar (gets all the woody rook moves and adds those to the valid moves list to be filtered)
    '''

    def getwoodyrookmoves(self, r, c, moves):
        langkahkuda = ((-2, 0), (2, 0), (0, -2), (0, 2), (-1, 0), (1, 0), (0, -1), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah short rook lalu memasukan ke daftar (gets all the short rook moves and adds those to the valid moves list to be filtered)
    '''

    def getshortrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 5):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah chancellor lalu memasukan ke daftar (gets all the chancellor moves and adds those to the valid moves list to be filtered)
    '''

    def getchancellormoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah half duck lalu memasukan ke daftar (gets all the half duck moves and adds those to the valid moves list to be filtered)
    '''

    def gethalfduckmoves(self, r, c, moves):
        langkahkuda = ((-2, 0), (2, 0), (0, -2), (0, 2), (-1, 1), (1, 1), (-1, -1), (1, -1), (-3, 0), (3, 0), (0, -3), (0, 3))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahkuda:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    rokade (castling moves)
    '''

    def getcastlemoves(self, r, c, moves):
        if self.squareunderattack(r, c):
            return
        if (self.whitetomove and self.currentcastlerights.wks) or (not self.whitetomove and self.currentcastlerights.bks):
            self.getkingcastlemoves(r, c, moves)
        if (self.whitetomove and self.currentcastlerights.wqs) or (not self.whitetomove and self.currentcastlerights.bqs):
            self.getqueencastlemoves(r, c, moves)

    '''
    rokade (castling moves)
    '''

    def getkingcastlemoves(self, r, c, moves):
        if self.board[r][c + 1] == '--' and self.board[r][c + 2] == '--':
            if not self.squareunderattack(r, c + 1) and not self.squareunderattack(r, c + 2):
                moves.append(Move((r, c), (r, c + 2), self.board, castle=True))

    '''
    rokade (castling moves)
    '''

    def getqueencastlemoves(self, r, c, moves):
        if self.board[r][c - 1] == '--' and self.board[r][c - 2] == '--' and self.board[r][c - 3] == '--':
            if self.board[r][c - 4][1:] != 'BD':
                if not self.squareunderattack(r, c - 1) and not self.squareunderattack(r, c - 2):
                    moves.append(Move((r, c), (r, c - 2), self.board, castle=True))
            elif self.board[r][c - 4][1:] == 'BD':
                if not self.squareunderattack(r, c - 1) and not self.squareunderattack(r, c - 2) and not self.squareunderattack(r, c - 3):
                    moves.append(Move((r, c), (r, c - 3), self.board, castle=True))

    '''
    promosi (promotion)
    '''

    def getpromotion(self, move):
        global Promotedpiece
        self.promotionfail = True
        Window = Tk()
        Window.configure(bg="#202020")
        Window.geometry('+%d+%d' % (100, 100))

        def Q():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "Q"
            Window.destroy()

        def B():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "B"
            Window.destroy()

        def K():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "N"
            Window.destroy()

        def R():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "R"
            Window.destroy()

        def BD():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "BD"
            Window.destroy()

        def WA():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "WA"
            Window.destroy()

        def FA():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "FA"
            Window.destroy()

        def CA():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "CA"
            Window.destroy()

        def CR():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "CR"
            Window.destroy()

        def FN():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "FN"
            Window.destroy()

        def CN():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "CN"
            Window.destroy()

        def CO():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "CO"
            Window.destroy()

        def SR():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "SR"
            Window.destroy()

        def WR():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "WR"
            Window.destroy()

        def HD():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "HD"
            Window.destroy()

        def CH():
            global Promotedpiece
            self.promotionfail = False
            Promotedpiece = "CH"
            Window.destroy()

        def ext():
            global Promotedpiece
            self.promotionfail = True
            Promotedpiece = "R"
            Window.destroy()

        if (WhiteArmyPieces == "FF" and not self.whitetomove) or (BlackArmyPieces == "FF" and self.whitetomove):
            QW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wQ.png")
            RW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wR.png")
            BW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wB.png")
            KW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wN.png")
            QB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bQ.png")
            RB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bR.png")
            BB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bB.png")
            KB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bN.png")

            Button(Window, image=QB if self.whitetomove else QW, command=Q, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=BB if self.whitetomove else BW, command=B, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=KB if self.whitetomove else KW, command=K, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=RB if self.whitetomove else RW, command=R, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()

        if (WhiteArmyPieces == "CC" and not self.whitetomove) or (BlackArmyPieces == "CC" and self.whitetomove):
            BDW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wBD.png")
            WAW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wWA.png")
            FAW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wFA.png")
            CAW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wCA.png")
            BDB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bBD.png")
            WAB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bWA.png")
            FAB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bFA.png")
            CAB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bCA.png")

            Button(Window, image=BDB if self.whitetomove else BDW, command=BD, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=WAB if self.whitetomove else WAW, command=WA, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=FAB if self.whitetomove else FAW, command=FA, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=CAB if self.whitetomove else CAW, command=CA, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            
        if (WhiteArmyPieces == "KK" and not self.whitetomove) or (BlackArmyPieces == "KK" and self.whitetomove):
            CRW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wCR.png")
            FNW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wFN.png")
            CNW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wCN.png")
            COW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wCO.png")
            CRB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bCR.png")
            FNB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bFN.png")
            CNB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bCN.png")
            COB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bCO.png")

            Button(Window, image=CRB if self.whitetomove else CRW, command=CR, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=FNB if self.whitetomove else FNW, command=FN, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=CNB if self.whitetomove else CNW, command=CN, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=COB if self.whitetomove else COW, command=CO, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()

        if (WhiteArmyPieces == "RR" and not self.whitetomove) or (BlackArmyPieces == "RR" and self.whitetomove):
            SRW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wSR.png")
            WRW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wWR.png")
            HDW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wHD.png")
            CHW = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/wCH.png")
            SRB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bSR.png")
            WRB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bWR.png")
            HDB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bHD.png")
            CHB = PhotoImage(file="Textures/CWDA/Piece Move Diagrams/bCH.png")

            Button(Window, image=SRB if self.whitetomove else SRW, command=SR, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=WRB if self.whitetomove else WRW, command=WR, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=HDB if self.whitetomove else HDW, command=HD, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
            Button(Window, image=CHB if self.whitetomove else CHW, command=CH, borderwidth=0,
                   bg="#202020",
                   activebackground="#202020", fg="White").pack()
        cancelM = PhotoImage(file="Textures/GUI/cancel.png")
        Button(image=cancelM, command=ext, borderwidth=0, bg="#202020", activebackground="#202020", fg="white", activeforeground="#909090").pack()
        Window.overrideredirect(1)
        Window.mainloop()
        self.board[move.endrow][move.endcol] = move.piecemoved[0] + Promotedpiece

    '''
    dropping
    '''

    def getdrop(self, move):
        pass

    def undodrop(self):
        pass


class Castlerights:
    def __init__(self, wks, bks, wqs, bqs):
        self.wks = wks
        self.bks = bks
        self.wqs = wqs
        self.bqs = bqs


class Move:
    # biar bisa baca notasi catur (so it can somewhat produce chess notation)
    rankstorows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                   "m": 12, "n": 13, "o": 14, "p": 15}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board, enpassant=False, castle=False):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]
        self.canpromote = False
        self.mustpromote = (self.piecemoved == 'wP' and self.endrow == 0) or (
                self.piecemoved == 'bP' and self.endrow == 7)
        self.ispromotion = self.mustpromote or self.canpromote

        self.enpassant = enpassant
        if enpassant:
            self.piececaptured = 'wP' if self.piecemoved == 'bP' else 'bP'

        self.castle = castle

        self.drop = self.endrow == self.startrow and self.endcol == self.startcol

        self.iscapture = self.piececaptured != '--'

        self.startsquare = self.colstofiles[self.startcol] + self.rowstoranks[self.startrow]
        self.endsquare = self.colstofiles[self.endcol] + self.rowstoranks[self.endrow]
        self.startsqcol = self.colstofiles[self.startcol]

        self.moveid = self.startrow*1000000 + self.startcol*10000 + self.endrow*100 + self.endcol

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.colstofiles[c] + self.rowstoranks[r]

    '''
    overriding samadengan (overriding the equal sign)
    '''

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveid == other.moveid
        return False

    '''
    overriding string
    '''

    def __str__(self):
        endsquare = self.getrankfile(self.endrow, self.endcol)
        # langkah pion(pawn moves)
        if self.piecemoved[1] == 'P':
            pawnmovestring = self.colstofiles[self.startcol]

            if self.iscapture:
                pawnmovestring += "x" + endsquare

            if not self.iscapture:
                pawnmovestring = endsquare

            if self.ispromotion:
                try:
                    pawnmovestring += "=" + Promotedpiece
                except NameError:
                    pawnmovestring += "=" + self.piecemoved

            return pawnmovestring
        # langkah bidak lainnya (other pieces' moves)
        movestring = self.piecemoved[1:]

        if self.iscapture:
            movestring += "x" + endsquare

        if not self.iscapture:
            movestring += endsquare

        if self.ispromotion:
            movestring += "=" + Promotedpiece

        return movestring
