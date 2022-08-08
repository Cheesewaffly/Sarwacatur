"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
from tkinter import *


def board(screen, ukr):
    pass


Dimensi = 8
Dimensi2 = 8
Pieces = ['wB', 'bB', 'wK', 'bK', 'wN', 'bN', 'wP', 'bP', 'wQ', 'bQ', 'wR', 'bR']
Theme = "Textures/Chess/"
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen',
              'K': 'King'}
global Promotedpiece


class GameState:
    def __init__(self):
        # papan caturnya, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is len(self.board[0])xlen(self.board[0]), every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
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
                self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 2]
                self.board[move.endrow][move.endcol - 2] = '--'

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
                    self.board[move.endrow][move.endcol - 2] = self.board[move.endrow][move.endcol + 1]
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
        elif move.piecemoved == 'wR':
            if move.startrow == 7:
                if move.startcol == 0:
                    self.currentcastlerights.wqs = False
                elif move.startcol == 7:
                    self.currentcastlerights.wks = False
        elif move.piecemoved == 'bR':
            if move.startrow == 0:
                if move.startcol == 0:
                    self.currentcastlerights.bqs = False
                elif move.endcol == 7:
                    self.currentcastlerights.bks = False
        if move.piececaptured == 'wR':
            if move.endcol == 0:
                self.currentcastlerights.wqs = False
            elif move.endcol == 7:
                self.currentcastlerights.wks = False
        elif move.piececaptured == 'bR':
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
                if r == 6 and self.board[r - 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
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
                if r == 1 and self.board[r + 2][c] == "--":  # maju 2 petak di langkah pertama (moves upto 2 squares forward in the first move)
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
                else:
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
    castling moves
    '''

    def getcastlemoves(self, r, c, moves):
        if self.squareunderattack(r, c):
            return
        if (self.whitetomove and self.currentcastlerights.wks) or (not self.whitetomove and self.currentcastlerights.bks):
            self.getkingcastlemoves(r, c, moves)
        if (self.whitetomove and self.currentcastlerights.wqs) or (not self.whitetomove and self.currentcastlerights.bqs):
            self.getqueencastlemoves(r, c, moves)

    '''
    castling moves
    '''

    def getkingcastlemoves(self, r, c, moves):
        if self.board[r][c + 1] == '--' and self.board[r][c + 2] == '--':
            if not self.squareunderattack(r, c + 1) and not self.squareunderattack(r, c + 2):
                moves.append(Move((r, c), (r, c + 2), self.board, castle=True))

    '''
    castling moves
    '''

    def getqueencastlemoves(self, r, c, moves):
        if self.board[r][c - 1] == '--' and self.board[r][c - 2] == '--' and self.board[r][c - 3] == '--':
            if not self.squareunderattack(r, c - 1) and not self.squareunderattack(r, c - 2):
                moves.append(Move((r, c), (r, c - 2), self.board, castle=True))

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
        # langkah pion (pawn moves)
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
