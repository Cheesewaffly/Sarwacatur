"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
from tkinter import *


def board(screen, ukr):
    pass


Dimensi = 16
Dimensi2 = 16
Pieces = ['wA', 'bA', 'wB', 'bB', 'wC', 'bC', 'wD', 'bD', 'wE', 'bE', 'wF', 'bF', 'wG', 'bG', 'wH', 'bH', 'wI', 'bI',
          'wJ', 'bJ', 'wK', 'bK', 'wL', 'bL', 'wM', 'bM', 'wN', 'bN', 'wO', 'bO', 'wP', 'bP', 'wQ', 'bQ', 'wR', 'bR',
          'wS', 'bS', 'wT', 'bT', 'wU', 'bU', 'wV', 'bV', 'wW', 'bW', 'wX', 'bX', 'wY', 'bY', 'wZ', 'bZ']
Theme = "Textures/Tjatoer!/"
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen',
              'K': 'King', 'F': 'Ferz', 'M': 'Man', 'G': 'Gajah',
              'L': 'Lance', 'A': 'Archbishop', 'I': 'Imam',
              'O': 'Oknha', 'J': 'Jester', 'C': 'Chariot',
              'D': 'Duchess', 'E': 'Esquire', 'H': 'Hawk',
              'X': 'Xiphodon', 'V': 'Viscount', 'S': 'Shrook',
              'T': 'Thalia', 'U': 'Upasaka', 'W': 'Warrior',
              'Y': 'Yishi', 'Z': 'Zebra'}
global Promotedpiece


class GameState:
    def __init__(self):
        # papan caturnya, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is 16x16, every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            ["bY", "bU", "bQ", "bX", "bV", "bO", "bF", "bL", "bK", "bE", "bD", "bV", "bX", "bQ", "bU", "bY"],
            ["bR", "bC", "bG", "bJ", "bB", "bM", "bM", "bM", "bM", "bM", "bM", "bB", "bJ", "bG", "bC", "bR"],
            ["bZ", "bI", "bN", "bA", "bH", "bS", "bT", "bW", "bW", "bT", "bS", "bH", "bA", "bN", "bI", "bZ"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wZ", "wI", "wN", "wA", "wH", "wS", "wT", "wW", "wW", "wT", "wS", "wH", "wA", "wN", "wI", "wZ"],
            ["wR", "wC", "wG", "wJ", "wB", "wM", "wM", "wM", "wM", "wM", "wM", "wB", "wJ", "wG", "wC", "wR"],
            ["wY", "wU", "wQ", "wX", "wV", "wO", "wF", "wL", "wK", "wE", "wD", "wV", "wX", "wQ", "wU", "wY"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'Q': self.getqueenmoves, 'K': self.getkingmoves,
                             'F': self.getferzmoves, 'M': self.getmanmoves, 'G': self.getgajahmoves,
                             'L': self.getlancemoves, 'A': self.getarchbishopmoves, 'I': self.getimammoves,
                             'O': self.getoknhamoves, 'J': self.getjestermoves, 'C': self.getchariotmoves,
                             'D': self.getduchessmoves, 'E': self.getesquiremoves, 'H': self.gethawkmoves,
                             'X': self.getxiphodonmoves, 'V': self.getviscountmoves, 'S': self.getshrookmoves,
                             'T': self.getthaliamoves, 'U': self.getupasakamoves, 'W': self.getwarriormoves,
                             'Y': self.getyishimoves, 'Z': self.getzebramoves}
        self.whitetomove = True
        self.movelog = []
        self.movelist = []
        self.whitekinglocation = (15, 8)
        self.blackkinglocation = (0, 8)
        self.checkmate = False
        self.stalemate = False
        self.dropfail = True
        self.promotionfail = False

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
        for i in range(1, 200):
            if len(self.movelist) >= 200:
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
                    bidak = self.board[r][c][1]
                    self.movefunction[bidak](r, c, moves)  # berdasarkan tipe bidak
        return moves

    '''
    semua langkah pion lalu memasukan ke daftar (gets all the pawn moves and adds those to the valid moves list to be filtered)
    '''

    def getpawnmoves(self, r, c, moves):
        if self.whitetomove:  # pion putih (white pawn)
            if self.board[r - 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r - 1, c), self.board))
                for n in range(2, 5):
                    if r == 12 and self.board[r - n][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                        moves.append(Move((r, c), (r - n, c), self.board))
                    else:
                        break
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 1][c - 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r - 1][c + 1][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # pion hitam
            if self.board[r + 1][c] == "--":  # maju 1 petak (move 1 squre forward)
                moves.append(Move((r, c), (r + 1, c), self.board))
                for n in range(2, 5):
                    if r == 3 and self.board[r + n][c] == "--":  # maju 4 petak di langkah pertama (moves upto 4 squares forward in the first move)
                        moves.append(Move((r, c), (r + n, c), self.board))
                    else:
                        break
            if c - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r + 1][c - 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 < len(self.board[0]):  # makan ke kanan (captures to the right)
                if self.board[r + 1][c + 1][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

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
    semua langkah hawk lalu memasukan ke daftar (gets all the hawk moves and adds those to the valid moves list to be filtered)
    '''

    def gethawkmoves(self, r, c, moves):
        self.getknightmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

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
    semua langkah ferz lalu memasukan ke daftar (gets all the ferz moves and adds those to the valid moves list to be filtered)
    '''

    def getferzmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah duchess lalu memasukan ke daftar (gets all the duchess moves and adds those to the valid moves list to be filtered)
    '''

    def getduchessmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah esquire lalu memasukan ke daftar (gets all the esquire moves and adds those to the valid moves list to be filtered)
    '''

    def getesquiremoves(self, r, c, moves):
        self.getgajahmoves(r, c, moves)
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah man lalu memasukan ke daftar (gets all the man moves and adds those to the valid moves list to be filtered)
    '''

    def getmanmoves(self, r, c, moves):
        self.getknightmoves(r, c, moves)
        self.getkingmoves(r, c, moves)

    '''
    semua langkah oknha lalu memasukan ke daftar (gets all the oknha moves and adds those to the valid moves list to be filtered)
    '''

    def getoknhamoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the elephant moves and adds those to the valid moves list to be filtered)
    '''

    def getgajahmoves(self, r, c, moves):
        langkahgajah = ((-3, -1), (-3, 1), (3, -1), (3, 1), (-1, 3), (-1, -3), (1, 3), (1, -3))
        warnateman = "w" if self.whitetomove else "b"
        for m in langkahgajah:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah jester lalu memasukan ke daftar (gets all the jester moves and adds those to the valid moves list to be filtered)
    '''

    def getjestermoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah charriot lalu memasukan ke daftar (gets all the chariot moves and adds those to the valid moves list to be filtered)
    '''

    def getchariotmoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah lance lalu memasukan ke daftar (gets all the lance moves and adds those to the valid moves list to be filtered)
    '''

    def getlancemoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)
        self.getgajahmoves(r, c, moves)

    '''
    semua langkah archbisop lalu memasukan ke daftar (gets all the archbishop moves and adds those to the valid moves list to be filtered)
    '''

    def getarchbishopmoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah imam lalu memasukan ke daftar (gets all the imam moves and adds those to the valid moves list to be filtered)
    '''

    def getimammoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        self.getknightmoves(r, c, moves)

    '''
    semua langkah xiphodon lalu memasukan ke daftar (gets all the xiphodon moves and adds those to the valid moves list to be filtered)
    '''

    def getxiphodonmoves(self, r, c, moves):
        if r - 1 > 0:
            if self.board[r - 1][c] == '--':
                d = (-1, 0)
                a = (-1, -1)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (-1, 1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        if r + 1 < len(self.board[0]):
            if self.board[r + 1][c] == '--':
                d = (1, 0)
                a = (1, -1)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (1, 1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        if c - 1 > 0:
            if self.board[r][c - 1] == '--':
                d = (0, -1)
                a = (-1, -1)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (1, -1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        if c + 1 < len(self.board[0]):
            if self.board[r][c + 1] == '--':
                d = (0, 1)
                a = (1, 1)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (-1, 1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        langkahxiphodon = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for x in langkahxiphodon:
            endrow = r + x[0]
            endcol = c + x[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah shrook lalu memasukan ke daftar (gets all the shrook moves and adds those to the valid moves list to be filtered)
    '''

    def getshrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 3):
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
    semua langkah thalia lalu memasukan ke daftar (gets all the thalia moves and adds those to the valid moves list to be filtered)
    '''

    def getthaliamoves(self, r, c, moves):
        directions = ((-1, 1), (1, -1), (1, 1), (-1, -1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 3):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece == "--":  # horizontal bebas (moves freely diagonally)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                    elif endpiece[0] == warnamusuh:  # ketutupan musuh (blocked by enemy piece)
                        moves.append(Move((r, c), (endrow, endcol), self.board))
                        break
                    else:  # bidak sendiri (blocked by own piece)
                        break
                else:  # diluar papan (out of the board)
                    break

    '''
    semua langkah viscount lalu memasukan ke daftar (gets all the viscount moves and adds those to the valid moves list to be filtered)
    '''

    def getviscountmoves(self, r, c, moves):
        if r - 1 > 0 and c - 1 > 0:
            if self.board[r - 1][c - 1] == '--':
                d = (-1, -1)
                a = (-1, 0)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (0, -1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
            if r - 1 > 0 and c + 1 < len(self.board[0]):
                if self.board[r - 1][c + 1] == '--':
                    d = (-1, 1)
                    a = (0, 1)
                    warnamusuh = "b" if self.whitetomove else "w"
                    midrow = r + d[0]
                    midcol = c + d[1]
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0]*i
                        endcol = midcol + a[1]*i
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
                    a = (-1, 0)
                    midrow = r + d[0]
                    midcol = c + d[1]
                    for i in range(1, len(self.board[0])):
                        endrow = midrow + a[0]*i
                        endcol = midcol + a[1]*i
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
        if r + 1 < len(self.board[0]) and c - 1 > 0:
            if self.board[r + 1][c - 1] == '--':
                d = (1, -1)
                a = (1, 0)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (0, -1)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        if r + 1 < len(self.board[0]) and c + 1 < len(self.board[0]):
            if self.board[r + 1][c + 1] == '--':
                d = (1, 1)
                a = (0, 1)
                warnamusuh = "b" if self.whitetomove else "w"
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
                a = (1, 0)
                midrow = r + d[0]
                midcol = c + d[1]
                for i in range(1, len(self.board[0])):
                    endrow = midrow + a[0]*i
                    endcol = midcol + a[1]*i
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
        langkahviscount = ((-1, 1), (1, -1), (1, 1), (-1, -1))
        warnateman = "w" if self.whitetomove else "b"
        for x in langkahviscount:
            endrow = r + x[0]
            endcol = c + x[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman:
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah zebra lalu memasukan ke daftar (gets all the zebra moves and adds those to the valid moves list to be filtered)
    '''

    def getzebramoves(self, r, c, moves):
        directions = ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, 8):
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
    semua langkah warrior lalu memasukan ke daftar (gets all the warrior moves and adds those to the valid moves list to be filtered)
    '''

    def getwarriormoves(self, r, c, moves):
        langkahwarrior = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        for m in langkahwarrior:
            endrow = r + m[0]
            endcol = c + m[1]
            if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece == "--":
                    moves.append(Move((r, c), (endrow, endcol), self.board))
        if self.whitetomove:
            if r - 2 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 2][c][0] == 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 2, c), self.board))
        else:
            if r + 2 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r + 2][c][0] == 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 2, c), self.board))

    '''
    semua langkah upasaka lalu memasukan ke daftar (gets all the upasaka moves and adds those to the valid moves list to be filtered)
    '''

    def getupasakamoves(self, r, c, moves):
        if self.whitetomove:
            langkahupasaka = (
                (-2, 1), (-2, -1), (-1, 2), (-1, -2), (-1, 0), (0, -1), (0, 1), (-2, 0), (0, -2), (0, 2), (1, 0))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahupasaka:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahupasaka = (
                (2, 1), (2, -1), (1, 2), (1, -2), (0, -1), (1, 0), (0, 1), (0, -2), (2, 0), (0, 2), (-1, 0))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahupasaka:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah yishi lalu memasukan ke daftar (gets all the yishi moves and adds those to the valid moves list to be filtered)
    '''

    def getyishimoves(self, r, c, moves):
        if self.whitetomove:
            langkahyishi = ((-1, -1), (-1, 1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (-2, -2), (-2, 2), (1, -1), (1, 1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahyishi:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahyishi = ((1, -1), (1, 1), (2, 1), (2, -1), (1, 2), (1, -2), (2, -2), (2, 2), (-1, 1), (-1, -1))
            warnateman = "w" if self.whitetomove else "b"
            for m in langkahyishi:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < len(self.board[0]) and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    promosi (promotion)
    '''

    def getpromotion(self, move):
        global Promotedpiece

        if move.piecemoved[1] == 'S' or move.piecemoved[1] == 'T' or move.piecemoved == 'W':
            if move.piecemoved[1] == 'S':
                Promotedpiece = "R"
                self.promotionfail = False

            if move.piecemoved[1] == 'T':
                Promotedpiece = "B"
                self.promotionfail = False

            if move.piecemoved[1] == 'W':
                Promotedpiece = "N"
                self.promotionfail = False

        if move.piecemoved[1] == 'P' or move.piecemoved[1] == 'M':
            Window = Tk()
            Window.title("White Pieces")
            Window.iconbitmap("Textures/GUI/wG.ico")
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

            def U():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "U"
                Window.destroy()

            def Y():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "Y"
                Window.destroy()

            def G():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "G"
                Window.destroy()

            def J():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "J"
                Window.destroy()

            def C():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "C"
                Window.destroy()

            def H():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "H"
                Window.destroy()

            def Z():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "Z"
                Window.destroy()

            def I():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "I"
                Window.destroy()

            def A():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "A"
                Window.destroy()

            def X():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "X"
                Window.destroy()

            def V():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "V"
                Window.destroy()

            def O():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "O"
                Window.destroy()

            def F():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "F"
                Window.destroy()

            def L():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "L"
                Window.destroy()

            def D():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "D"
                Window.destroy()

            def E():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "E"
                Window.destroy()

            def ext():
                global Promotedpiece
                self.promotionfail = True
                Promotedpiece = "R"
                Window.destroy()

            Window.protocol("WM_DELETE_WINDOW", ext)

            if move.piecemoved[1] == 'P':
                QW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wQ.png")
                RW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wR.png")
                BW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wB.png")
                KW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wN.png")
                UW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wU.png")
                YW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wY.png")
                GW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wG.png")
                JW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wJ.png")
                CW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wC.png")
                HW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wH.png")
                ZW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wZ.png")
                IW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wI.png")
                AW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wA.png")
                QB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bQ.png")
                RB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bR.png")
                BB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bB.png")
                KB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bN.png")
                UB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bU.png")
                YB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bY.png")
                GB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bG.png")
                JB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bJ.png")
                CB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bC.png")
                HB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bH.png")
                ZB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bZ.png")
                IB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bI.png")
                AB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bA.png")

                Button(Window, image=QB if self.whitetomove else QW, command=Q, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=0)
                Button(Window, image=BB if self.whitetomove else BW, command=B, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=1)
                Button(Window, image=KB if self.whitetomove else KW, command=K, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=2)
                Button(Window, image=RB if self.whitetomove else RW, command=R, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=3)
                Button(Window, image=UB if self.whitetomove else UW, command=U, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=4)
                Button(Window, image=YB if self.whitetomove else YW, command=Y, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=5)
                Button(Window, image=GB if self.whitetomove else GW, command=G, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=6)
                Button(Window, image=JB if self.whitetomove else JW, command=J, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=0)
                Button(Window, image=CB if self.whitetomove else CW, command=C, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=1)
                Button(Window, image=HB if self.whitetomove else HW, command=H, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=2)
                Button(Window, image=ZB if self.whitetomove else ZW, command=Z, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=3)
                Button(Window, image=IB if self.whitetomove else IW, command=I, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=4)
                Button(Window, image=AB if self.whitetomove else AW, command=A, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=1, row=5)

            if move.piecemoved[1] == 'M':
                XW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wX.png")
                VW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wV.png")
                OW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wO.png")
                FW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wF.png")
                LW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wL.png")
                DW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wD.png")
                EW = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/wE.png")
                XB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bX.png")
                VB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bV.png")
                OB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bO.png")
                FB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bF.png")
                LB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bL.png")
                DB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bD.png")
                EB = PhotoImage(file="Textures/Tjatoer!/Piece Move Diagrams/bE.png")

                Button(Window, image=XB if self.whitetomove else XW, command=X, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=0)
                Button(Window, image=VB if self.whitetomove else VW, command=V, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=1)
                Button(Window, image=OB if self.whitetomove else OW, command=O, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=2)
                Button(Window, image=FB if self.whitetomove else FW, command=F, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=3)
                Button(Window, image=LB if self.whitetomove else LW, command=L, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=4)
                Button(Window, image=DB if self.whitetomove else DW, command=D, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=5)
                Button(Window, image=EB if self.whitetomove else EW, command=E, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(column=0, row=6)

            cancelM = PhotoImage(file="Textures/GUI/cancel.png")
            Button(image=cancelM, command=ext, borderwidth=0, bg="#202020", activebackground="#202020", fg="white",
                   activeforeground="#909090").grid(row=100, column=0, columnspan=2)
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
    rankstorows = {"1": 15, "2": 14, "3": 13, "4": 12, "5": 11, "6": 10, "7": 9, "8": 8, "9": 7, "10": 6, "11": 5,
                   "12": 4, "13": 3, "14": 2, "15": 1, "16": 0}
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
        self.mustpromote = (self.piecemoved == 'wP' and self.endrow == 0) or (self.piecemoved == 'bP' and self.endrow == 15)\
                           or (self.piecemoved == 'wM' and self.endrow == 0) or (self.piecemoved == 'bM' and self.endrow == 15)\
                           or (self.piecemoved == 'wS' and self.endrow == 0) or (self.piecemoved == 'bS' and self.endrow == 15)\
                           or (self.piecemoved == 'wT' and self.endrow == 0) or (self.piecemoved == 'bT' and self.endrow == 15)\
                           or (self.piecemoved == 'wW' and self.endrow == 0) or (self.piecemoved == 'bW' and self.endrow == 15)
        self.ispromotion = self.mustpromote or self.canpromote

        self.enpassant = enpassant

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
        # langkah pion, man, shrook, thalia, dan warrior (pawn, man, shrook, thalia, and warrior moves)
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
        elif self.piecemoved[1] == 'M' or self.piecemoved[1] == 'S' or self.piecemoved[1] == 'T' or self.piecemoved[1] == 'W':
            manmovestring = self.piecemoved[1]

            if self.iscapture:
                manmovestring += "x" + endsquare

            if not self.iscapture:
                manmovestring += endsquare

            if self.ispromotion:
                try:
                    manmovestring += "=" + Promotedpiece
                except NameError:
                    manmovestring += "=" + 'M'

            return manmovestring
        # langkah bidak lainnya (other pieces' moves)
        movestring = self.piecemoved[1:]

        if self.iscapture:
            movestring += "x" + endsquare

        if not self.iscapture:
            movestring += endsquare

        if self.ispromotion:
            movestring += "=" + Promotedpiece

        return movestring
