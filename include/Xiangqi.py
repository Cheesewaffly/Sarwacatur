"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
import pygame as pg


Dimensi = 9
Dimensi2 = 10
Pieces = ['wE', 'bE', 'wK', 'bK', 'wH', 'bH', 'wP', 'bP', 'wG', 'bG', 'wR', 'bR', 'wC', 'bC']
Theme = "Textures/Xiangqi/"
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'H': 'Horse', 'G': 'Guard', 'C': 'Cannon',
              'K': 'King', 'E': 'Elephant'}
global Promotedpiece


def board(screen, ukr):
    boardi = pg.transform.scale(pg.image.load(Theme + "lines.png"), (ukr*Dimensi, ukr*Dimensi2))
    screen.blit(boardi, (0, 0))


class GameState:
    def __init__(self):
        # papan caturnya, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is 9x10, every element has 2 characters, the first one is the color, the second is the type)
        self.board = [
            ["bR", "bH", "bE", "bG", "bK", "bG", "bE", "bH", "bR"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "bC", "--", "--", "--", "--", "--", "bC", "--"],
            ["bP", "--", "bP", "--", "bP", "--", "bP", "--", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "--", "wP", "--", "wP", "--", "wP", "--", "wP"],
            ["--", "wC", "--", "--", "--", "--", "--", "wC", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wR", "wH", "wE", "wG", "wK", "wG", "wE", "wH", "wR"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'H': self.getknightmoves,
                             'C': self.getcannonmoves, 'E': self.getelephantmoves, 'K': self.getkingmoves, 'G': self.getguardmoves}

        self.whitetomove = True
        self.movelog = []
        self.movelist = []
        self.whitekinglocation = (9, 4)
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
            elif moves[i].piecemoved[0] == 'w':
                d = (-1, 0)
                for k in range(1, len(self.board[1])):
                    midrow = self.whitekinglocation[0] + d[0]*k
                    midcol = self.whitekinglocation[1] + d[1]*k
                    if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                        midpiece = self.board[midrow][midcol]
                        if midpiece != "--" and midpiece != "bK":
                            break
                        if midpiece == "bK":
                            moves.remove(moves[i])
            elif moves[i].piecemoved[0] == 'b':
                d = (1, 0)
                for k in range(1, len(self.board[1])):
                    midrow = self.blackkinglocation[0] + d[0]*k
                    midcol = self.blackkinglocation[1] + d[1]*k
                    if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                        midpiece = self.board[midrow][midcol]
                        if midpiece != "--" and midpiece != "wK":
                            break
                        if midpiece == "wK":
                            moves.remove(moves[i])
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
            if r - 1 >= 0:  # makan ke kiri (captures to the left)
                if self.board[r - 1][c][0] != 'w':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r - 1, c), self.board))
            if r < 5:
                if c - 1 >= 0:
                    if self.board[r][c - 1][0] != 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r, c - 1), self.board))
                if c + 1 <= 8:
                    if self.board[r][c + 1][0] != 'w':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r, c + 1), self.board))
        else:  # pion hitam
            if r + 1 <= 9:  # makan ke kiri (captures to the left)
                if self.board[r + 1][c][0] != 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c), self.board))
            if r > 4:
                if c - 1 >= 0:
                    if self.board[r][c - 1][0] != 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r, c - 1), self.board))
                if c + 1 <= 8:
                    if self.board[r][c + 1][0] != 'b':  # ada bidak lawan (opponents piece that is blocking)
                        moves.append(Move((r, c), (r, c + 1), self.board))

    '''
    semua langkah benteng lalu memasukan ke daftar (gets all the rook moves and adds those to the valid moves list to be filtered)
    '''

    def getrookmoves(self, r, c, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnamusuh = "b" if self.whitetomove else "w"
        for d in directions:
            for i in range(1, len(self.board[1])):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
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
        warnateman = "w" if self.whitetomove else "b"
        if c - 1 > 0 and self.board[r][c - 1] == '--':
            langkahkuda = ((-1, -2), (1, -2))
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        if c + 1 <= 8 and self.board[r][c + 1] == '--':
            langkahkuda = ((-1, 2), (1, 2))
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        if r - 1 > 0 and self.board[r - 1][c] == '--':
            langkahkuda = ((-2, -1), (-2, 1))
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        if r + 1 <= 9 and self.board[r + 1][c] == '--':
            langkahkuda = ((2, -1), (2, 1))
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah gajah lalu memasukan ke daftar (gets all the elephant moves and adds those to the valid moves list to be filtered)
    '''

    def getelephantmoves(self, r, c, moves):
        warnateman = "w" if self.whitetomove else "b"
        if self.whitetomove:
            if c - 1 > 0 and r - 1 > 0 and self.board[r - 1][c - 1] == '--':
                m = (-2, -2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 5 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c + 1 <= 8 and r - 1 > 0 and self.board[r - 1][c + 1] == '--':
                m = (-2, 2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 5 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c + 1 <= 8 and r + 1 <= 9 and self.board[r + 1][c + 1] == '--':
                m = (2, 2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 5 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c - 1 > 0 and r + 1 <= 9 and self.board[r + 1][c - 1] == '--':
                m = (2, -2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 5 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            if c - 1 > 0 and r - 1 > 0 and self.board[r - 1][c - 1] == '--':
                m = (-2, -2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 5 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c + 1 <= 8 and r - 1 > 0 and self.board[r - 1][c + 1] == '--':
                m = (-2, 2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 5 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c + 1 <= 8 and r + 1 <= 9 and self.board[r + 1][c + 1] == '--':
                m = (2, 2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 5 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            if c - 1 > 0 and r + 1 <= 9 and self.board[r + 1][c - 1] == '--':
                m = (2, -2)
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 5 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah meriam lalu memasukan ke daftar (gets all the cannon moves and adds those to the valid moves list to be filtered)
    '''

    def getcannonmoves(self, r, c, moves):
        warnamusuh = "b" if self.whitetomove else "w"
        d = (-1, 0)
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece == "--":
                    moves.append(Move((r, c), (midrow, midcol), self.board))
                else:
                    break
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece != "--":
                    for j in range(1, len(self.board[1])):
                        endrow = midrow + d[0]*j
                        endcol = midcol + d[1]*j
                        if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":
                                pass
                            elif endpiece[0] == warnamusuh:
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:
                                break
                    break
        d = (1, 0)
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece == "--":
                    moves.append(Move((r, c), (midrow, midcol), self.board))
                else:
                    break
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece != "--":
                    for j in range(1, len(self.board[1])):
                        endrow = midrow + d[0]*j
                        endcol = midcol + d[1]*j
                        if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":
                                pass
                            elif endpiece[0] == warnamusuh:
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:
                                break
                    break
        d = (0, 1)
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece == "--":
                    moves.append(Move((r, c), (midrow, midcol), self.board))
                else:
                    break
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece != "--":
                    for j in range(1, len(self.board[1])):
                        endrow = midrow + d[0]*j
                        endcol = midcol + d[1]*j
                        if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":
                                pass
                            elif endpiece[0] == warnamusuh:
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:
                                break
                    break
        d = (0, -1)
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece == "--":
                    moves.append(Move((r, c), (midrow, midcol), self.board))
                else:
                    break
        for i in range(1, len(self.board[1])):
            midrow = r + d[0]*i
            midcol = c + d[1]*i
            if 0 <= midrow < 10 and 0 <= midcol < len(self.board[0]):
                midpiece = self.board[midrow][midcol]
                if midpiece != "--":
                    for j in range(1, len(self.board[1])):
                        endrow = midrow + d[0]*j
                        endcol = midcol + d[1]*j
                        if 0 <= endrow < 10 and 0 <= endcol < len(self.board[0]):
                            endpiece = self.board[endrow][endcol]
                            if endpiece == "--":
                                pass
                            elif endpiece[0] == warnamusuh:
                                moves.append(Move((r, c), (endrow, endcol), self.board))
                                break
                            else:
                                break
                    break

    '''
    semua langkah mentri lalu memasukan ke daftar (gets all the quard moves and adds those to the valid moves list to be filtered)
    '''

    def getguardmoves(self, r, c, moves):
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(4):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if self.whitetomove:
                if 6 <= endrow <= 9 and 3 <= endcol <= 5:
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            else:
                if 0 <= endrow <= 2 and 3 <= endcol <= 5:
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah raja lalu memasukan ke daftar (gets all the king moves and adds those to the valid moves list to be filtered)
    '''

    def getkingmoves(self, r, c, moves):
        langkahraja = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(4):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if self.whitetomove:
                if 6 <= endrow <= 9 and 3 <= endcol <= 5:
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))
            else:
                if 0 <= endrow <= 2 and 3 <= endcol <= 5:
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman:
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    promosi (promotion)
    '''

    def getpromotion(self, move):
        pass

    '''
    dropping
    '''

    def getdrop(self, move):
        pass

    def undodrop(self):
        pass


class Move:
    # biar bisa baca notasi catur (so it can somewhat produce chess notation)
    rankstorows = {"1": 9, "2": 8, "3": 7, "4": 6, "5": 5, "6": 4, "7": 3, "8": 2, "9": 1, "10": 0}
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
        self.mustpromote = False
        self.ispromotion = False

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

            return pawnmovestring
        # langkah bidak lainnya (other pieces' moves)
        movestring = self.piecemoved[1:]

        if self.iscapture:
            movestring += "x" + endsquare

        if not self.iscapture:
            movestring += endsquare

        return movestring
