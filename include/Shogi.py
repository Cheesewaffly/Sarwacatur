"""
File ini bertanggung jawab untuk menampung semua informasi permainan dan juga langkah-langkah valid dan mencatat langkah (this file is responsible for all the information in the game)
"""
from tkinter import *
import pygame as pg

Dimensi = 9
Dimensi2 = 11
Pieces = ['wB', 'bB', 'wK', 'bK', 'wN', 'bN', 'wP', 'bP', 'wR', 'bR', 'wS', 'bS', 'wG', 'bG', 'wL', 'bL', 'wPP', 'bPP', 'wPN', 'bPN', 'wPL', 'bPL', 'wPS', 'bPS', 'wD', 'bD', 'wH', 'bH', 'BBL']
Theme = "Textures/Shogi/"
PieceNames = {'P': 'Pawn', 'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'L': 'Lance',
              'K': 'King', 'G': 'Gold General', 'S': 'Silver General', 'D': 'Dragon King', 'H': 'Dragon Horse', 'PP': 'Promoted Pawn',
              'PN': 'Promoted Knight', 'PL': 'Promoted Lance', 'PS': 'Promoted Silver General'}
global Promotedpiece, piecedropped

droppedpiece = []
blackdrop = []
whitedrop = []
CapturedPieces = {'wB': 'bB', 'bB': 'wB', 'wN': 'bN', 'bN': 'wN', 'wP': 'bP', 'bP': 'wP', 'wR': 'bR', 'bR': 'wR',
                  'wS': 'bS', 'bS': 'wS', 'wG': 'bG', 'bG': 'wG', 'wL': 'bL', 'bL': 'wL', 'wPP': 'bP',
                  'bPP': 'wP', 'wPN': 'bN', 'bPN': 'wN', 'wPL': 'bL', 'bPL': 'wL', 'wPS': 'bS',
                  'bPS': 'wS', 'wD': 'bR', 'bD': 'wR', 'wH': 'bB', 'bH': 'wB'}
Images = {}


def board(screen, ukr):
    wpawncounter = wknightcounter = wlancecounter = wsilvercounter = wgoldcounter = wbishopcounter = wrookcounter = bpawncounter = bknightcounter = blancecounter = bsilvercounter = bgoldcounter = bbishopcounter = brookcounter = 0
    boardi = pg.transform.scale(pg.image.load(Theme + "lines.png"), (ukr*Dimensi, ukr*Dimensi2))
    screen.blit(boardi, (0, 0))
    screen.blit(pg.transform.scale(pg.image.load(Theme + "TranB.png"), (ukr*7, ukr)), (1*ukr, 0))
    screen.blit(pg.transform.scale(pg.image.load(Theme + "TranW.png"), (ukr*7, ukr)), (1*ukr, 10*ukr))
    for b in whitedrop:
        if b == "bP":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (1*ukr, 0))
            wpawncounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wpawncounter) + ".png"), (ukr, ukr)), (1*ukr, 0))
        if b == "bL":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (2*ukr, 0))
            wlancecounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wlancecounter) + ".png"), (ukr, ukr)), (2*ukr, 0))
        if b == "bN":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (3*ukr, 0))
            wknightcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wknightcounter) + ".png"), (ukr, ukr)), (3*ukr, 0))
        if b == "bS":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (4*ukr, 0))
            wsilvercounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wsilvercounter) + ".png"), (ukr, ukr)), (4*ukr, 0))
        if b == "bG":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (5*ukr, 0))
            wgoldcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wgoldcounter) + ".png"), (ukr, ukr)), (5*ukr, 0))
        if b == "bB":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (6*ukr, 0))
            wbishopcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wbishopcounter) + ".png"), (ukr, ukr)), (6*ukr, 0))
        if b == "bR":
            screen.blit(pg.transform.scale(pg.image.load(Theme + b + ".png"), (ukr, ukr)), (7*ukr, 0))
            wrookcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(wrookcounter) + ".png"), (ukr, ukr)), (7*ukr, 0))
    for w in blackdrop:
        pawncounter = knightcounter = lancecounter = silvercounter = goldcounter = bishopcounter = rookcounter = 0
        if w == "wP":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (1*ukr, 10*ukr))
            bpawncounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(bpawncounter) + ".png"), (ukr, ukr)), (1*ukr, 10*ukr))
        if w == "wL":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (2*ukr, 10*ukr))
            blancecounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(blancecounter) + ".png"), (ukr, ukr)), (2*ukr, 10*ukr))
        if w == "wN":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (3*ukr, 10*ukr))
            bknightcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(bknightcounter) + ".png"), (ukr, ukr)), (3*ukr, 10*ukr))
        if w == "wS":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (4*ukr, 10*ukr))
            bsilvercounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(bsilvercounter) + ".png"), (ukr, ukr)), (4*ukr, 10*ukr))
        if w == "wG":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (5*ukr, 10*ukr))
            bgoldcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(bgoldcounter) + ".png"), (ukr, ukr)), (5*ukr, 10*ukr))
        if w == "wB":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (6*ukr, 10*ukr))
            bbishopcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(bbishopcounter) + ".png"), (ukr, ukr)), (6*ukr, 10*ukr))
        if w == "wR":
            screen.blit(pg.transform.scale(pg.image.load(Theme + w + ".png"), (ukr, ukr)), (7*ukr, 10*ukr))
            brookcounter += 1
            screen.blit(pg.transform.scale(pg.image.load(Theme + str(brookcounter) + ".png"), (ukr, ukr)), (7*ukr, 10*ukr))


class GameState:
    def __init__(self):
        # papan caturnya, setiap elemen daftar mempunyai 2 karakter, karakter pertama warnanya, kedua tipenya (the board is 9x9, every element has 2 characters, the wirst one is the color, the second is the type)
        self.board = [
            ["BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL"],
            ["bL", "bN", "bS", "bG", "bK", "bG", "bS", "bN", "bL"],
            ["--", "bR", "--", "--", "--", "--", "--", "bB", "--"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["--", "wB", "--", "--", "--", "--", "--", "wR", "--"],
            ["wL", "wN", "wS", "wG", "wK", "wG", "wS", "wN", "wL"],
            ["BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL", "BBL"]]
        self.movefunction = {'P': self.getpawnmoves, 'R': self.getrookmoves, 'N': self.getknightmoves,
                             'B': self.getbishopmoves, 'L': self.getlancemoves, 'K': self.getkingmoves,
                             '-': self.getblankmoves, 'S': self.getsilvergeneralmoves, 'G': self.getgoldgeneralmoves,
                             'PS': self.getgoldgeneralmoves, 'PP': self.getgoldgeneralmoves,
                             'PL': self.getgoldgeneralmoves, 'PN': self.getgoldgeneralmoves, 'D': self.getdragonkingmoves, 'H': self.getdragonhorsemoves, 'BL': self.getblankmoves}
        self.whitetomove = True
        self.movelog = []
        self.whitekinglocation = (9, 4)
        self.blackkinglocation = (1, 4)
        self.checkmate = False
        self.stalemate = False
        self.promotionfail = True
        self.dropfail = True
        self.movelist = []
        if len(self.movelog) == 0:
            global whitedrop, blackdrop, droppedpiece
            droppedpiece = []
            blackdrop = []
            whitedrop = []

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
        if move.iscapture:
            if self.whitetomove:
                whitedrop.append(CapturedPieces[move.piececaptured])
            else:
                blackdrop.append(CapturedPieces[move.piececaptured])
        if move.drop:
            pawn = 'bP' if self.whitetomove else 'wP'
            drops = whitedrop if self.whitetomove else blackdrop
            if len(drops) != 0:
                self.board[move.endrow][move.endcol] = pawn
            elif len(drops) == 0:
                self.board[move.endrow][move.endcol] = '--'

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
            if move.iscapture:
                if self.whitetomove:
                    blackdrop.remove(CapturedPieces[move.piececaptured])
                else:
                    whitedrop.remove(CapturedPieces[move.piececaptured])
            if move.drop:
                self.board[move.endrow][move.endcol] = '--'

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
                self.getblankmoves(r, c, moves)
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
        else:  # pion hitam
            if r + 1 < len(self.board[0]):  # makan ke kiri (captures to the left)
                if self.board[r + 1][c][0] != 'b':  # ada bidak lawan (opponents piece that is blocking)
                    moves.append(Move((r, c), (r + 1, c), self.board))
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
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
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
        if self.whitetomove:
            langkahkuda = ((-2, -1), (-2, 1))
            warnateman = "w"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahkuda = ((2, -1), (2, 1))
            warnateman = "b"
            for m in langkahkuda:
                endrow = r + m[0]
                endcol = c + m[1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
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
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
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
    semua langkah lance lalu memasukan ke daftar (gets all the lance moves and adds those to the valid moves list to be filtered)
    '''

    def getlancemoves(self, r, c, moves):
        if self.whitetomove:
            d = (-1, 0)
            warnamusuh = "b"
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
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
            d = (1, 0)
            warnamusuh = "w"
            for i in range(1, len(self.board[0])):
                endrow = r + d[0]*i
                endcol = c + d[1]*i
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
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
    semua langkah raja lalu memasukan ke daftar (gets all the king moves and adds those to the valid moves list to be filtered)
    '''

    def getkingmoves(self, r, c, moves):
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(8):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman and endpiece[0] != "B":
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah gold general lalu memasukan ke daftar (gets all the gold general moves and adds those to the valid moves list to be filtered)
    '''

    def getgoldgeneralmoves(self, r, c, moves):
        if self.whitetomove:
            langkahraja = ((-1, -1), (-1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
            warnateman = "w"
            for i in range(6):
                endrow = r + langkahraja[i][0]
                endcol = c + langkahraja[i][1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahraja = ((1, -1), (1, 1), (-1, 0), (0, -1), (1, 0), (0, 1))
            warnateman = "b"
            for i in range(6):
                endrow = r + langkahraja[i][0]
                endcol = c + langkahraja[i][1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    semua langkah silver general lalu memasukan ke daftar (gets all the silver general moves and adds those to the valid moves list to be filtered)
    '''

    def getsilvergeneralmoves(self, r, c, moves):
        if self.whitetomove:
            langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0))
            warnateman = "w"
            for i in range(5):
                endrow = r + langkahraja[i][0]
                endcol = c + langkahraja[i][1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
                        moves.append(Move((r, c), (endrow, endcol), self.board))
        else:
            langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0))
            warnateman = "b"
            for i in range(5):
                endrow = r + langkahraja[i][0]
                endcol = c + langkahraja[i][1]
                if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                    endpiece = self.board[endrow][endcol]
                    if endpiece[0] != warnateman and endpiece[0] != "B":
                        moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    untuk drop (for drops)
    '''

    def getblankmoves(self, r, c, moves):
        if self.board[r][c] == '--':
            moves.append(Move((r, c), (r, c), self.board))

    '''
    semua langkah dragon horse lalu memasukan ke daftar (gets all the dragon horse moves and adds those to the valid moves list to be filtered)
    '''

    def getdragonhorsemoves(self, r, c, moves):
        self.getbishopmoves(r, c, moves)
        langkahraja = ((-1, 0), (0, -1), (1, 0), (0, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(4):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman and endpiece[0] != "B":
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
   semua langkah dragon king lalu memasukan ke daftar (gets all the dragon king moves and adds those to the valid moves list to be filtered)
   '''

    def getdragonkingmoves(self, r, c, moves):
        self.getrookmoves(r, c, moves)
        langkahraja = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        warnateman = "w" if self.whitetomove else "b"
        for i in range(4):
            endrow = r + langkahraja[i][0]
            endcol = c + langkahraja[i][1]
            if 0 <= endrow < 11 and 0 <= endcol < len(self.board[0]):
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != warnateman and endpiece[0] != "B":
                    moves.append(Move((r, c), (endrow, endcol), self.board))

    '''
    promosi (promotion)
    '''

    def getpromotion(self, move):
        global Promotedpiece
        if move.canpromote:
            self.promotionfail = True
            Window = Tk()
            Window.configure(bg="#202020")
            Window.geometry('+%d+%d' % (100, 100))

            def PP():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "PP"
                Window.destroy()

            def PN():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "PN"
                Window.destroy()

            def PL():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "PL"
                Window.destroy()

            def PSG():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "PS"
                Window.destroy()

            def DK():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "D"
                Window.destroy()

            def DH():
                global Promotedpiece
                self.promotionfail = False
                Promotedpiece = "H"
                Window.destroy()

            def ext():
                global Promotedpiece
                self.promotionfail = True
                Promotedpiece = move.piecemoved[1:]
                Window.destroy()

            PPW = PhotoImage(file=Theme + "Piece Move Diagrams/wPP.png")
            PNW = PhotoImage(file=Theme + "Piece Move Diagrams/wPN.png")
            PLW = PhotoImage(file=Theme + "Piece Move Diagrams/wPL.png")
            PSGW = PhotoImage(file=Theme + "Piece Move Diagrams/wPS.png")
            DKW = PhotoImage(file=Theme + "Piece Move Diagrams/wD.png")
            DHW = PhotoImage(file=Theme + "Piece Move Diagrams/wH.png")
            PPB = PhotoImage(file=Theme + "Piece Move Diagrams/bPP.png")
            PNB = PhotoImage(file=Theme + "Piece Move Diagrams/bPN.png")
            PLB = PhotoImage(file=Theme + "Piece Move Diagrams/bPL.png")
            PSGB = PhotoImage(file=Theme + "Piece Move Diagrams/bPS.png")
            DKB = PhotoImage(file=Theme + "Piece Move Diagrams/bD.png")
            DHB = PhotoImage(file=Theme + "Piece Move Diagrams/bH.png")

            if move.piecemoved[1:] == 'P':
                Button(Window, image=PPB if self.whitetomove else PPW, command=PP, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            if move.piecemoved[1:] == 'N':
                Button(Window, image=PNB if self.whitetomove else PNW, command=PN, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            if move.piecemoved[1:] == 'L':
                Button(Window, image=PLB if self.whitetomove else PLW, command=PL, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            if move.piecemoved[1:] == 'S':
                Button(Window, image=PSGB if self.whitetomove else PSGW, command=PSG, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            if move.piecemoved[1:] == 'R':
                Button(Window, image=DKB if self.whitetomove else DKW, command=DK, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            if move.piecemoved[1:] == 'B':
                Button(Window, image=DHB if self.whitetomove else DHW, command=DH, borderwidth=0,
                       bg="#202020",
                       activebackground="#202020", fg="White").grid(row=0, column=0)
            cancelM = PhotoImage(file="Textures/GUI/cancel.png")
            Button(image=cancelM, command=ext, borderwidth=0, bg="#202020", activebackground="#202020", fg="white", activeforeground="#909090").grid(row=1, column=0)
            Window.overrideredirect(1)
            Window.mainloop()
            self.board[move.endrow][move.endcol] = move.piecemoved[0] + Promotedpiece
        elif move.mustpromote:
            if move.piecemoved[1:] == 'P':
                Promotedpiece = "PP"
                self.board[move.endrow][move.endcol] = move.piecemoved[0] + Promotedpiece
                self.promotionfail = False
            elif move.piecemoved[1:] == 'L':
                Promotedpiece = "PL"
                self.board[move.endrow][move.endcol] = move.piecemoved[0] + Promotedpiece
                self.promotionfail = False
            elif move.piecemoved[1:] == 'N':
                Promotedpiece = "PN"
                self.board[move.endrow][move.endcol] = move.piecemoved[0] + Promotedpiece
                self.promotionfail = False

    '''
    dropping
    '''

    def getdrop(self, move):
        self.dropfail = True
        global piecedropped
        Window = Tk()
        Window.configure(bg="#202020")
        Window.geometry('+%d+%d' % (100, 100))

        def wP():
            global piecedropped
            self.dropfail = False
            piecedropped = 'P'
            droppedpiece.append("wP")
            Window.destroy()

        def wB():
            global piecedropped
            self.dropfail = False
            piecedropped = 'B'
            droppedpiece.append("wB")
            Window.destroy()

        def wK():
            global piecedropped
            self.dropfail = False
            piecedropped = 'N'
            droppedpiece.append("wN")
            Window.destroy()

        def wR():
            global piecedropped
            self.dropfail = False
            piecedropped = 'R'
            droppedpiece.append("wR")
            Window.destroy()

        def wS():
            global piecedropped
            self.dropfail = False
            piecedropped = 'S'
            droppedpiece.append("wS")
            Window.destroy()

        def wL():
            global piecedropped
            self.dropfail = False
            piecedropped = 'L'
            droppedpiece.append("wL")
            Window.destroy()

        def wG():
            global piecedropped
            self.dropfail = False
            piecedropped = 'G'
            droppedpiece.append("wG")
            Window.destroy()

        def bP():
            global piecedropped
            self.dropfail = False
            piecedropped = 'P'
            droppedpiece.append("bP")
            Window.destroy()

        def bB():
            global piecedropped
            self.dropfail = False
            piecedropped = 'B'
            droppedpiece.append("bB")
            Window.destroy()

        def bK():
            global piecedropped
            self.dropfail = False
            piecedropped = 'N'
            droppedpiece.append("bN")
            Window.destroy()

        def bR():
            global piecedropped
            self.dropfail = False
            piecedropped = 'R'
            droppedpiece.append("bR")
            Window.destroy()

        def bS():
            global piecedropped
            self.dropfail = False
            piecedropped = 'S'
            droppedpiece.append("bS")
            Window.destroy()

        def bL():
            global piecedropped
            self.dropfail = False
            piecedropped = 'L'
            droppedpiece.append("bL")
            Window.destroy()

        def bG():
            global piecedropped
            self.dropfail = False
            piecedropped = 'G'
            droppedpiece.append("bG")
            Window.destroy()

        def ext():
            global piecedropped
            self.dropfail = True
            piecedropped = '-'
            droppedpiece.append("--")
            Window.destroy()

        PW = PhotoImage(file=Theme + "Piece Move Diagrams/wP.png")
        RW = PhotoImage(file=Theme + "Piece Move Diagrams/wR.png")
        BW = PhotoImage(file=Theme + "Piece Move Diagrams/wB.png")
        KW = PhotoImage(file=Theme + "Piece Move Diagrams/wN.png")
        LW = PhotoImage(file=Theme + "Piece Move Diagrams/wL.png")
        GGW = PhotoImage(file=Theme + "Piece Move Diagrams/wG.png")
        SGW = PhotoImage(file=Theme + "Piece Move Diagrams/wS.png")

        PB = PhotoImage(file=Theme + "Piece Move Diagrams/bP.png")
        RB = PhotoImage(file=Theme + "Piece Move Diagrams/bR.png")
        BB = PhotoImage(file=Theme + "Piece Move Diagrams/bB.png")
        KB = PhotoImage(file=Theme + "Piece Move Diagrams/bN.png")
        LB = PhotoImage(file=Theme + "Piece Move Diagrams/bL.png")
        GGB = PhotoImage(file=Theme + "Piece Move Diagrams/bG.png")
        SGB = PhotoImage(file=Theme + "Piece Move Diagrams/bS.png")

        if not self.whitetomove:
            for wp in blackdrop:
                if wp == "wP":
                    Button(Window, image=PW, command=wP, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=0)
                if wp == "wB":
                    Button(Window, image=BW, command=wB, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=1)
                if wp == "wN":
                    Button(Window, image=KW, command=wK, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=2)
                if wp == "wR":
                    Button(Window, image=RW, command=wR, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=3)
                if wp == "wS":
                    Button(Window, image=SGW, command=wS, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=4)
                if wp == "wL":
                    Button(Window, image=LW, command=wL, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=5)
                if wp == "wG":
                    Button(Window, image=GGW, command=wG, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=6)
        if self.whitetomove:
            for wb in whitedrop:
                if wb == "bP":
                    Button(Window, image=PB, command=bP, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=0)
                if wb == "bB":
                    Button(Window, image=BB, command=bB, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=1)
                if wb == "bN":
                    Button(Window, image=KB, command=bK, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=2)
                if wb == "bR":
                    Button(Window, image=RB, command=bR, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=3)
                if wb == "bS":
                    Button(Window, image=SGB, command=bS, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=4)
                if wb == "bL":
                    Button(Window, image=LB, command=bL, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=5)
                if wb == "bG":
                    Button(Window, image=GGB, command=bG, borderwidth=0,
                           bg="#202020",
                           activebackground="#202020", fg="White").grid(column=0, row=6)
        cancelM = PhotoImage(file="Textures/GUI/cancel.png")
        Button(image=cancelM, command=ext, borderwidth=0, bg="#202020", activebackground="#202020", fg="white",
               activeforeground="#909090").grid(row=100, column=0)
        Window.overrideredirect(1)
        Window.mainloop()
        self.makedrop(move)
        if self.dropfail:
            self.undodrop()
            self.undomove()

    def makedrop(self, move):
        yes = []
        if len(droppedpiece) >= 1:
            if move.drop:
                self.board[move.endrow][move.endcol] = droppedpiece[-1]
                if droppedpiece[-1][0] == 'w':
                    blackdrop.remove(droppedpiece[-1])
                elif droppedpiece[-1][0] == 'b':
                    whitedrop.remove(droppedpiece[-1])
                if len(droppedpiece) >= 1:
                    if droppedpiece[-1][1] == 'P' or droppedpiece[-1][1] == 'L' or droppedpiece[-1][1] == 'N':
                        if self.whitetomove:
                            if move.endrow == 9:
                                self.dropfail = True
                        else:
                            if move.endrow == 1:
                                self.dropfail = True

                for r in range(len(self.board)):
                    if len(droppedpiece) >= 1:
                        if droppedpiece[-1] == 'wP':
                            if self.board[r][move.endcol] == 'wP':
                                if self.board[move.endrow][move.endcol] == self.board[r][move.endcol]:
                                    yes.append('pawnthere')
                        elif droppedpiece[-1] == 'bP':
                            if self.board[r][move.endcol] == 'bP':
                                if self.board[move.endrow][move.endcol] == self.board[r][move.endcol]:
                                    yes.append('pawnthere')
                if len(yes) > 1:
                    self.dropfail = True
                if len(droppedpiece) >= 1:
                    if droppedpiece[-1][1] == 'P':
                        moves = self.getvalidmoves()
                        if len(moves) == 0:
                            if self.incheck():
                                self.dropfail = True

    def undodrop(self):
        if len(self.movelog) != 0:  # biar ada yg bisa diundo
            if self.movelog[-1].drop:
                if len(droppedpiece) != 0:
                    if droppedpiece[-1][0] == 'w':
                        blackdrop.append(droppedpiece[-1])
                        droppedpiece.remove(droppedpiece[-1])
                    elif droppedpiece[-1][0] == 'b':
                        whitedrop.append(droppedpiece[-1])
                        droppedpiece.remove(droppedpiece[-1])
                    elif droppedpiece[-1][0] == '-':
                        del droppedpiece[-1]


class Move:
    # biar bisa baca notasi catur (so it can somewhat produce chess notation)
    rankstorows = {"1": 10, "2": 9, "3": 8, "4": 7, "5": 6, "6": 5, "7": 4, "8": 3, "9": 2, "10": 1, "11": 0}
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
        self.piecepromoted = board[self.startrow][self.endcol][1]
        self.piececaptured = board[self.endrow][self.endcol]
        self.canpromote = (self.piecemoved == 'wP' and self.endrow == 2) or (self.piecemoved == 'bP' and self.endrow == 8)\
                          or (self.piecemoved == 'wP' and self.endrow == 3) or (self.piecemoved == 'bP' and self.endrow == 7)\
                          or (self.piecemoved == 'wL' and self.endrow == 2) or (self.piecemoved == 'bL' and self.endrow == 8)\
                          or (self.piecemoved == 'wL' and self.endrow == 3) or (self.piecemoved == 'bL' and self.endrow == 7)\
                          or (self.piecemoved == 'wN' and self.endrow == 2) or (self.piecemoved == 'bN' and self.endrow == 8)\
                          or (self.piecemoved == 'wN' and self.endrow == 3) or (self.piecemoved == 'bN' and self.endrow == 7)\
                          or (self.piecemoved == 'wS' and self.endrow == 1) or (self.piecemoved == 'bS' and self.endrow == 9)\
                          or (self.piecemoved == 'wS' and self.endrow == 2) or (self.piecemoved == 'bS' and self.endrow == 8)\
                          or (self.piecemoved == 'wS' and self.endrow == 3) or (self.piecemoved == 'bS' and self.endrow == 7)\
                          or (self.piecemoved == 'wB' and self.endrow == 1) or (self.piecemoved == 'bB' and self.endrow == 9)\
                          or (self.piecemoved == 'wB' and self.endrow == 2) or (self.piecemoved == 'bB' and self.endrow == 8)\
                          or (self.piecemoved == 'wB' and self.endrow == 3) or (self.piecemoved == 'bB' and self.endrow == 7)\
                          or (self.piecemoved == 'wR' and self.endrow == 1) or (self.piecemoved == 'bR' and self.endrow == 9)\
                          or (self.piecemoved == 'wR' and self.endrow == 2) or (self.piecemoved == 'bR' and self.endrow == 8)\
                          or (self.piecemoved == 'wR' and self.endrow == 3) or (self.piecemoved == 'bR' and self.endrow == 7)\
                          or (self.piecemoved == 'wS' and self.startrow == 1) or (self.piecemoved == 'bS' and self.startrow == 9)\
                          or (self.piecemoved == 'wS' and self.startrow == 2) or (self.piecemoved == 'bS' and self.startrow == 8)\
                          or (self.piecemoved == 'wS' and self.startrow == 3) or (self.piecemoved == 'bS' and self.startrow == 7)\
                          or (self.piecemoved == 'wB' and self.startrow == 1) or (self.piecemoved == 'bB' and self.startrow == 9)\
                          or (self.piecemoved == 'wB' and self.startrow == 2) or (self.piecemoved == 'bB' and self.startrow == 8)\
                          or (self.piecemoved == 'wB' and self.startrow == 3) or (self.piecemoved == 'bB' and self.startrow == 7)\
                          or (self.piecemoved == 'wR' and self.startrow == 1) or (self.piecemoved == 'bR' and self.startrow == 9)\
                          or (self.piecemoved == 'wR' and self.startrow == 2) or (self.piecemoved == 'bR' and self.startrow == 8)\
                          or (self.piecemoved == 'wR' and self.startrow == 3) or (self.piecemoved == 'bR' and self.startrow == 7)
        self.mustpromote = (self.piecemoved == 'wP' and self.endrow == 1) or (self.piecemoved == 'bP' and self.endrow == 9)\
                           or (self.piecemoved == 'wL' and self.endrow == 1) or (self.piecemoved == 'bL' and self.endrow == 9)\
                           or (self.piecemoved == 'wN' and self.endrow == 1) or (self.piecemoved == 'bN' and self.endrow == 9)
        self.ispromotion = self.mustpromote or self.canpromote

        self.enpassant = enpassant
        if enpassant:
            self.piececaptured = 'wP' if self.piecemoved == 'bP' else 'bP'

        self.castle = castle

        self.drop = self.endrow == self.startrow and self.endcol == self.startcol

        self.iscapture = self.piececaptured != '--' and self.piececaptured != 'BBL'
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
        # langkahpion(pawnmoves)
        if self.piecemoved[1:] == 'P':
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
            try:
                movestring += "=" + Promotedpiece
            except NameError:
                movestring += movestring + self.piecemoved

        if self.drop:
            try:
                movestring = piecedropped + '*' + endsquare
            except NameError:
                movestring = self.piecemoved + '*' + endsquare

        return movestring
