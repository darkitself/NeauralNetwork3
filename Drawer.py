from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self, n, np):
        self.root = Tk()
        self.n = n
        self.np = np

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='Wipe', command=self.wipe)
        self.eraser_button.grid(row=0, column=2)

        self.analyze_button = Button(self.root, text='Analyze', command=self.analyze)
        self.analyze_button.grid(row=0, column=3)

        self.labelText = StringVar()
        self.result = Label(self.root, textvariable=self.labelText)
        self.result.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=28 * 30, height=28 * 30)
        self.c.create_rectangle(0, 0, 28 * 30, 28 * 30, fill='white')

        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.line_width = 1
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def analyze(self):
        x = 15
        y = 15
        data = []
        for i in range(28):
            for j in range(28):
                ids = self.c.find_overlapping(x + 30 * j, y + 30 * i, x + 30 * j, y + 30 * i)
                if len(ids) > 0:
                    index = ids[-1]
                    color = self.c.itemcget(index, "fill").upper()
                    if color == "BLACK":
                        data.append(254)
                    else:
                        data.append(0)
        scaled_input = ((self.np.asfarray(data) / 255.0 * 0.99) + 0.01)
        output_num = self.np.argmax(self.np.transpose(self.n.query(scaled_input)))
        self.labelText.set(output_num)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def wipe(self):
        self.c.create_rectangle(0, 0, 28 * 30, 28 * 30, fill='white')

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.color
        self.c.create_rectangle((event.x // 30) * 30, (event.y // 30) * 30, (event.x // 30) * 30 + 30, (event.y // 30) * 30 + 30,
                                fill=paint_color, outline = paint_color)


if __name__ == '__main__':
    Paint()
