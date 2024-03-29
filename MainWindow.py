from tkinter import *
from GridWindow import *
import json

class MainWindow:
    def __init__(self, width, height, title="C PZDR"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.createSliders()
        

    def createSliders(self):
        self.scale_w = Scale(self.root, from_ = 20, to = 1000, orient='horizontal', length= 200, command=self.changeSliderWidth)
        self.scale_h = Scale(self.root, from_ = 20, to = 400, orient='horizontal', length= 200, command=self.changeSliderHeight)

        self.scale_x = Scale(self.root, from_ = 20, to = 1000, orient='horizontal', length= 200, command=self.changeSliderX)
        self.scale_y = Scale(self.root, from_ = 20, to = 700, orient='horizontal', length= 200, command=self.changeSliderY)
        self.scale_segmets = Scale(self.root, from_ = 10, to = 40, orient='horizontal', length= 200, command=self.changeSliderSegments)
        self.scaleOpacity = Scale(self.root, from_ = 100, to = 20, orient='horizontal', length= 200, command=self.changeSliderOpacity)

        self.scale_w.pack()
        self.scale_w.set(200)
        self.scale_h.pack()
        self.scale_h.set(200)

        self.scale_x.pack()
        self.scale_y.pack()
        self.scale_segmets.pack()
        self.scaleOpacity.pack()
        self.scaleOpacity.set(100)

        Button(text="Save configuration", width=28, command=self.buttonSaveConfig).pack()
        Button(text="Load configuration", width=28, command=self.buttonLoadConfig).pack()



    def changeSliderWidth(self, value):
        self.gridWindow.geometry[0] = value
        self.gridWindow.UpdateGeometry()


    def changeSliderHeight(self, value):
        self.gridWindow.geometry[1] = value
        self.gridWindow.UpdateGeometry()


    def changeSliderX(self, value):
        self.gridWindow.geometry[2] = value
        self.gridWindow.UpdateGeometry()


    def changeSliderY(self, value):
        self.gridWindow.geometry[3] = value
        self.gridWindow.UpdateGeometry()


    def changeSliderSegments(self, value):
        self.gridWindow.segments_len = int(value)
        self.gridWindow.GenerateGrid()


    def changeSliderOpacity(self, value):
        self.gridWindow.alpha = int(value)
        self.gridWindow.root.wm_attributes('-alpha', int(value) / 100)


    def buttonSaveConfig(self):
        data = {
            "orders_grid" :{
                    "width" : int(self.gridWindow.geometry[0]),
                    "height" : int(self.gridWindow.geometry[1]),
                    "pos_x" : int(self.gridWindow.geometry[2]),
                    "pos_y" : int(self.gridWindow.geometry[3]),
                    "alpha" : int(self.gridWindow.alpha),
                    "segments_len" : int(self.gridWindow.segments_len)
                    }
                }
        with open("config.json", "w") as file:
            json.dump(data, file, indent=4)


    def buttonLoadConfig(self):
        with open("config.json", "r") as file:
            data = json.load(file)
            self.gridWindow.geometry[0] = data["orders_grid"]["width"]
            self.gridWindow.geometry[1] = data["orders_grid"]["height"]
            self.gridWindow.geometry[2] = data["orders_grid"]["pos_x"]
            self.gridWindow.geometry[3] = data["orders_grid"]["pos_y"]
            self.gridWindow.UpdateGeometry()

            self.gridWindow.alpha = int(data["orders_grid"]["alpha"])
            self.gridWindow.root.wm_attributes('-alpha', (int(data["orders_grid"]["alpha"]) / 100))

            self.gridWindow.segments_len = int(data["orders_grid"]["segments_len"])
            self.gridWindow.GenerateGrid()

            self.scale_w.set(int(data["orders_grid"]["width"]))
            self.scale_h.set(int(data["orders_grid"]["height"]))
            self.scale_x.set(int(data["orders_grid"]["pos_x"]))
            self.scale_y.set(int(data["orders_grid"]["pos_y"]))
            self.scale_segmets.set(int(data["orders_grid"]["segments_len"]))
            self.scaleOpacity.set(int(data["orders_grid"]["alpha"]))


    def run(self):
        self.root.mainloop()


    def CreateGridWindow(self, width, height):
        self.gridWindow = GridWindow(self.root, width, height)



# if __name__ == '__main__':
#     mainWindow = MainWindow(400, 200)
#     mainWindow.run()
