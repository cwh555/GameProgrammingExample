import tkinter as tk
import GameObject

class Brick(GameObject):
    # colors for bricks with difference hits
    __COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}
    def __init__(self, canvas, x, y, hits, width = 75, height = 20):
        ''' hits 代表還可以被碰撞幾次 '''
        self.__hits = hits
        self.__width = width
        self.__height = height
        color = self.__class__.__COLORS[hits]
        item = canvas.create_rectangle(x - width / 2, y - height / 2,
                                       x + width / 2, y + height / 2,
                                       fill = color, tags = 'brick')
        super().__init__(canvas, item)

    def hit(self):
        ''' 被球碰撞一次 '''
        self.__hits -= 1
        if self.__hits == 0:
            # delete brick from canvas
            self.delete()
        else:
            # change color
            self.__canvas.itemconfig(self.__item, fill = self.__class__.COLORS[self.__hits])