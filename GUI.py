from tkinter import *
from tkinter import ttk
import sys
global Choice, img, awi, ahe, swi, she, x, y

Variants = {0: 'Alice Chess',
1: 'Almost Chess',
2: 'Antichess',
3: 'Capablanca Chess',
4: 'Charge of the Light Brigade',
5: 'Chess',
6: 'Chess with Different Armies',
7: 'Cylindrical Chess',
8: 'Los Alamos Chess',
9: 'Peasants Revolt',
10: 'Shogi',
11: 'Tjatoer!',
12: 'Xiangqi'}


def maingui():
    BG = "#202020"
    Window = Tk()
    Window.title("Sarwacatur")
    Window.iconbitmap("Textures/GUI/wG.ico")
    Window.configure(bg=BG)
    Window.resizable(False, False)

    V = StringVar()
    V.set('none')

    def ext():
        sys.exit()

    def CB():
        global img, awi, ahe, swi, she, x, y
        img = PhotoImage(file="Textures/GUI/Games/"+V.get()+".png")
        close.configure(image=okayB)
        Board.configure(image=img, borderwidth=10)
        Prev.destroy()

        awi = Board.winfo_reqwidth() + 74
        ahe = 850
        swi = Window.winfo_screenwidth()
        she = Window.winfo_screenheight()
        x = (swi/2) - (awi/2)
        y = (she/2) - (ahe/2)
        Window.geometry('+%d+%d' % (x, y))

    def Var(value):
        global Choice
        if value != 'none':
            Choice = value
            Window.destroy()
            return Choice
        else:
            pass

    style = ttk.Style(Window)
    # create new scrollbar layout
    style.layout('arrowless.Vertical.TScrollbar',
                 [('Vertical.Scrollbar.trough',
                   {'children': [('Vertical.Scrollbar.thumb',
                                  {'expand': '1', 'sticky': 'nswe'})],
                    'sticky': 'ns'})])

    frametwo = LabelFrame(Window, bg=BG)
    frameone = LabelFrame(Window, bg=BG)

    canvasone = Canvas(frameone, bg=BG, highlightthickness=0)
    canvasone.pack(side=LEFT, fill="both")

    scrollone = ttk.Scrollbar(frameone, orient="vertical", command=canvasone.yview, style='arrowless.Vertical.TScrollbar')
    scrollone.pack(side=RIGHT, fill="y")

    canvasone.configure(yscrollcommand=scrollone.set)
    canvasone.bind('<Configure>', lambda e: canvasone.configure(scrollregion=canvasone.bbox('all')))

    areaone = Frame(canvasone, bg=BG)
    canvasone.create_window((0, 0), window=areaone, anchor="nw")

    for i in range(0, len(Variants)):
        Radiobutton(areaone, text=Variants[i], variable=V, value=Variants[i], command=CB, indicatoron=0, borderwidth=0, fg="white", selectcolor=BG, activeforeground="#505050", width=100, anchor='w', bg=BG, activebackground=BG).grid(row=i, column=0, pady=3, padx=3)

    frametwo.pack(fill="both", expand=1, padx=10, pady=10)
    frameone.pack(fill="both", expand=1, padx=10)
    okayB = PhotoImage(file="Textures/GUI/okay.png")
    cancelB = PhotoImage(file="Textures/GUI/cancel.png")
    close = Button(Window, image=cancelB, borderwidth=0, bg=BG, activebackground="#202020", command=lambda: Var(V.get()))
    close.pack(pady=10)

    BlankB = PhotoImage(file="Textures/GUI/BlankBoard.png")

    Board = Label(frametwo, image=BlankB, borderwidth=10, bg="white", activebackground="#202020")
    Board.grid(row=0, column=0, pady=25, padx=25)

    Prev = Label(frametwo, text="Pratinjau", bg=BG, fg='white')
    Prev.grid(row=0, column=0)

    awi = 454
    ahe = 850
    swi = Window.winfo_screenwidth()
    she = Window.winfo_screenheight()
    x = (swi/2) - (awi/2)
    y = (she/2) - (ahe/2)
    Window.geometry('+%d+%d' % (x, y))

    Window.protocol("WM_DELETE_WINDOW", ext)

    Window.mainloop()
    return Choice
