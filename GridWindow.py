from tkinter import *


class GridWindow:
    def __init__(self, parent,  width, height):
        self.geometry = [200, 200, 0, 0]
        self.root = Toplevel(parent)
        self.root.overrideredirect(True)
        self.canvas = Canvas(self.root, bg="gray")
        self.canvas.pack(fill=BOTH, expand=True)
        self.segments_len = 10
        self.alpha = 1
        self.UpdateGeometry()
        self.GenerateGrid()


    def UpdateGeometry(self):
        self.root.geometry(f"{self.geometry[0]}x{self.geometry[1]}+{self.geometry[2]}+{self.geometry[3]}")
        # self.GenerateGrid()


    def GenerateGrid(self):
        self.canvas.delete("all")
        y = 0
        for i in range(400 // self.segments_len):
            y = i * self.segments_len
            self.canvas.create_line(0, y, 1000, y ,fill='red', width=2)


    # def setAlpha(self, value):
    #     self.root.wm_attributes('-alpha', self.alpha)
