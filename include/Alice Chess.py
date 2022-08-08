"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
from tkinter import *
import pygame as pg


Dimensi = 16
Dimensi2 = 8
Pieces = ['wB', 'bB', 'wK', 'bK', 'wN', 'bN', 'wP', 'bP', 'wQ', 'bQ', 'wR', 'bR']
Theme = "Textures/Alice Chess/"
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen',
              'K': 'King'}
global Promotedpiece


def board(screen, ukr):
    boardi = pg.transform.scale(pg.image.load(Theme + "lines.png"), (ukr*Dimensi, ukr*Dimensi2))
    screen.blit(boardi, (0, 0))


class GameState:
    def __init__(self):
        # papan caturnya, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is len(self.board[0])xlen(self.board[0]), every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR", "--", "--", "--", "--", "--", "--", "--", "--"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'Q': self.getqueenmoves, 'K': self.getkingmoves, }

        self.whitetomove = True
        self.movelog = []
        self.movelist = []
        self.whitekinglocation = (7, 4)
        self.blackkinglocation = (0, 4)
        self.checkmate = False
        self.stalemate = False
        self.promotionfail = True
        self.dropfail = True

    '''
    mengambil langkah sebagai parameter kemudian mengeksekusinya (takes a move as a parameter and makes that move, this is used to check for checks)
    '''

    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        if move.iscapture:
            if move.startcol <= 7:
                self.board[move.endrow][move.endcol - 8] = "--"
            if 7 < move.startcol < 16:
                self.board[move.endrow][move.endcol + 8] = "--"
        self.movelog.append(move)  # mencatat langkah biar bisa diundo (records the move so it can be undone)
        self.movelist.append(str(move))
        self.whitetomove = not self.whitetomove  # gantian giliran (changes the turn)
        if move.piecemoved == 'wK':
            self.whitekinglocation = (move.endrow, move.endcol)
        elif move.piecemoved == 'bK':
            self.blackkinglocation = (move.endrow, move.endcol)

    '''
    undo lngkah terakhir (undo the last move)
    '''

    def undomove(self):
        if len(self.movelog) != 0:  # biar ada yg bisa diundo
            move = self.movelog.pop()
            self.movelist.pop()
            self.board[move.startrow][move.startcol] = move.piecemoved
            if move.iscapture:
                self.board[move.endrow][move.endcol] = "--"
                if move.startcol <= 7:
                    self.board[move.endrow][move.endcol - 8] = move.piececaptured
                if 7 < move.startcol < 16:
                    self.board[move.endrow][move.endcol + 8] = move.piececaptured
            if not move.iscapture:
                self.board[move.endrow][move.endcol] = move.piececaptured
            self.whitetomove = not self.whitetomove
            if move.piecemoved == 'wK':
                self.whitekinglocation = (move.startrow, move.startcol)
            elif move.piecemoved == 'bK':
                self.blackkinglocation = (move.startrow, move.startcol)

            self.checkmate = False
            self.stalemate = False

    '''
    semua langkah termasuk skak (all moves including checks)
    '''

    def getvalidmoves(self):
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
            if move.endrow == r:
                if move.startcol <= 7:
                    if move.endcol - 8 == c:  # petak yg sedang diserang
                        return True
                if 7 < move.startcol < 16:
                    if move.endcol + 8 == c:  # petak yg sedang diserang
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
            if c <= 7:
                if self.board[r - 1][c] == "--" and self.board[r - 1][c + 8] == "--":  # maju 1 petak (move 1 squre forward)
                    moves.append(Move((r, c), (r - 1, c + 8), self.board))
                    if r == 6 and self.board[r - 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
                        moves.append(Move((r, c), (r - 2, c + 8), self.board))
                if 0 <= c - 1 < 8:  # makan ke kiri (captures to the left)
                    if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r - 1, c - 1 + 8), self.board, capture=True))
                if 0 <= c + 1 < 8:  # makan ke kanan (captures to the right)
                    if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r - 1, c + 1 + 8), self.board, capture=True))
            if 7 < c < 16:
                if self.board[r - 1][c] == "--" and self.board[r - 1][c - 8] == "--":  # maju 1 petak (move 1 squre forward)
                    moves.append(Move((r, c), (r - 1, c - 8), self.board))
                    if r == 6 and self.board[r - 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
                        moves.append(Move((r, c), (r - 2, c - 8), self.board))
                if 7 < c - 1 < len(self.board[0]):  # makan ke kiri (captures to the left)
                    if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r - 1, c - 1 - 8), self.board, capture=True))
                if 7 < c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                    if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r - 1, c + 1 - 8), self.board, capture=True))

        else:  # pion hitam
            if c <= 7:
                if self.board[r + 1][c] == "--" and self.board[r + 1][c + 8] == "--":  # maju 1 petak (move 1 squre forward)
                    moves.append(Move((r, c), (r + 1, c + 8), self.board))
                    if r == 1 and self.board[r + 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
                        moves.append(Move((r, c), (r + 2, c + 8), self.board))
                if 0 <= c - 1 < 8:  # makan ke kiri (captures to the left)
                    if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r + 1, c - 1 + 8), self.board, capture=True))
                if 0 <= c + 1 < 8:  # makan ke kanan (captures to the right)
                    if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r + 1, c + 1 + 8), self.board, capture=True))
            if 7 < c < 16:
                if self.board[r + 1][c] == "--" and self.board[r + 1][c - 8] == "--":  # maju 1 petak (move 1 squre forward)
                    moves.append(Move((r, c), (r + 1, c - 8), self.board))
                    if r == 1 and self.board[r + 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
                        moves.append(Move((r, c), (r + 2, c - 8), self.board))
                if 7 < c - 1 < len(self.board[0]):  # makan ke kiri (captures to the left)
                    if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r + 1, c - 1 - 8), self.board, capture=True))
                if 7 < c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                    if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r + 1, c + 1 - 8), self.board, capture=True))

    '''
    semua langkah benteng lalu memasukan ke daftar (gets all the rook moves and adds those to the valid moves list to be filtered)
    '''

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                realendcol = c + d[1]*i
                if c <= 7:
                    fakeendcol = c + d[1]*i + 8
                if 7 < c < 16:
                    fakeendcol = c + d[1]*i - 8
                if 0 <= endrow < 8 and 0 <= fakeendcol < len(self.board[0]) and 0 <= realendcol < len(self.board[0]):
                    fakeendpiece = self.board[endrow][fakeendcol]
                    realendpiece = self.board[endrow][realendcol]
                    if realendpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, fakeendcol), self.board))
                        if fakeendpiece != "--":
                            moves.remove(Move((r, c), (endrow, fakeendcol), self.board))
                    elif realendpiece[0] == warnamusuh:
                        moves.append(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
                        if fakeendpiece != "--":
                            moves.remove(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
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
        warnamusuh = "b" if self.whitetomove else "w"
        for m in langkahkuda:
            endrow = r + m[0]
            realendcol = c + m[1]
            if c <= 7:
                fakeendcol = c + m[1] + 8
            if 7 < c < 16:
                fakeendcol = c + m[1] - 8
            if 0 <= endrow < 8 and 0 <= fakeendcol < len(self.board[0]) and 0 <= realendcol < len(self.board[0]):
                fakeendpiece = self.board[endrow][fakeendcol]
                realendpiece = self.board[endrow][realendcol]
                if realendpiece == "--":  # horizontal bebas (moves freely horizontally)
                    moves.append(Move((r, c), (endrow, fakeendcol), self.board))
                    if fakeendpiece != "--":
                        moves.remove(Move((r, c), (endrow, fakeendcol), self.board))
                elif realendpiece[0] == warnamusuh:
                    moves.append(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
                    if fakeendpiece != "--":
                        moves.remove(Move((r, c), (endrow, fakeendcol), self.board, capture=True))

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the bishop moves and adds those to the valid moves list to be filtered)
    '''

    def getbishopmoves(self, r, c, moves):
        directions = ((-1, -1), (1, -1), (1, 1), (-1, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                realendcol = c + d[1]*i
                if c <= 7:
                    fakeendcol = c + d[1]*i + 8
                if 7 < c < 16:
                    fakeendcol = c + d[1]*i - 8
                if 0 <= endrow < 8 and 0 <= fakeendcol < len(self.board[0]) and 0 <= realendcol < len(self.board[0]):
                    fakeendpiece = self.board[endrow][fakeendcol]
                    realendpiece = self.board[endrow][realendcol]
                    if realendpiece == "--":  # horizontal bebas (moves freely horizontally)
                        moves.append(Move((r, c), (endrow, fakeendcol), self.board))
                        if fakeendpiece != "--":
                            moves.remove(Move((r, c), (endrow, fakeendcol), self.board))
                    elif realendpiece[0] == warnamusuh:
                        moves.append(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
                        if fakeendpiece != "--":
                            moves.remove(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
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
        warnamusuh = "b" if self.whitetomove else "w"
        for i in range(8):
            endrow = r + langkahraja[i][0]
            realendcol = c + langkahraja[i][1]
            if c <= 7:
                fakeendcol = c + langkahraja[i][1] + 8
            if 7 < c < 16:
                fakeendcol = c + langkahraja[i][1] - 8
            if 0 <= endrow < 8 and 0 <= fakeendcol < len(self.board[0]) and 0 <= realendcol < len(self.board[0]):
                fakeendpiece = self.board[endrow][fakeendcol]
                realendpiece = self.board[endrow][realendcol]
                if realendpiece == "--":  # horizontal bebas (moves freely horizontally)
                    moves.append(Move((r, c), (endrow, fakeendcol), self.board))
                    if fakeendpiece != "--":
                        moves.remove(Move((r, c), (endrow, fakeendcol), self.board))
                elif realendpiece[0] == warnamusuh:
                    moves.append(Move((r, c), (endrow, fakeendcol), self.board, capture=True))
                    if fakeendpiece != "--":
                        moves.remove(Move((r, c), (endrow, fakeendcol), self.board, capture=True))

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

        def ext():
            global Promotedpiece
            self.promotionfail = True
            Promotedpiece = "P"
            Window.destroy()

        QW = PhotoImage(file="Textures/Chess/Piece Move Diagrams/wQ.png")
        RW = PhotoImage(file="Textures/Chess/Piece Move Diagrams/wR.png")
        BW = PhotoImage(file="Textures/Chess/Piece Move Diagrams/wB.png")
        KW = PhotoImage(file="Textures/Chess/Piece Move Diagrams/wN.png")
        QB = PhotoImage(file="Textures/Chess/Piece Move Diagrams/bQ.png")
        RB = PhotoImage(file="Textures/Chess/Piece Move Diagrams/bR.png")
        BB = PhotoImage(file="Textures/Chess/Piece Move Diagrams/bB.png")
        KB = PhotoImage(file="Textures/Chess/Piece Move Diagrams/bN.png")

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


class Move:
    # biar bisa baca notasi catur (so it can somewhat produce chess notation)
    rankstorows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'a', 9: 'b', 10: 'c', 11: 'd', 12: 'e', 13: 'f', 14: 'g', 15: 'h'}
    colstofiles = {v: k for k, v in filestocols.items()}

    def __init__(self, startsq, endsq, board, enpassant=False, castle=False, capture=False):
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

        if capture:
            self.piececaptured = board[self.endrow][self.endcol - 8] if self.startcol <= 7 else board[self.endrow][self.endcol + 8]

        self.iscapture = capture

        self.startsquare = self.filestocols[self.startcol] + self.rowstoranks[self.startrow]
        self.endsquare = self.filestocols[self.endcol] + self.rowstoranks[self.endrow]
        self.startsqcol = self.filestocols[self.startcol]

        self.moveid = self.startrow*1000000 + self.startcol*10000 + self.endrow*100 + self.endcol

    def getchessnotation(self):
        return self.getrankfile(self.startrow, self.startcol) + self.getrankfile(self.endrow, self.endcol)

    def getrankfile(self, r, c):
        return self.filestocols[c] + self.rowstoranks[r]

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
        # langkah pion (pawn moves)
        if self.piecemoved[1] == 'P':
            pawnmovestring = self.filestocols[self.startcol]

            if self.iscapture:
                pawnmovestring += "x" + endsquare

            else:
                pawnmovestring = endsquare

            if self.ispromotion:
                try:
                    pawnmovestring += "=" + Promotedpiece
                except NameError:
                    pawnmovestring += "=" + self.piecemoved

            return pawnmovestring + "/A" if self.endcol <= 7 else pawnmovestring + "/B"
        # langkah bidak lainnya (other pieces' moves)
        movestring = self.piecemoved[1:]

        if self.iscapture:
            movestring += "x" + endsquare

        else:
            movestring += endsquare

        if self.ispromotion:
            movestring += "=" + Promotedpiece

        return movestring + "/A" if self.endcol <= 7 else movestring + "/B"
