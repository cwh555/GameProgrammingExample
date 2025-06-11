import tkinter as tk
import GameObject

class Brick(GameObject):
    # colors for bricks with difference hits
    _COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}
    def __init__(self, canvas, x, y, hits, width = 75, height = 20):
        ''' hits 代表還可以被碰撞幾次 '''
        self._hits = hits
        self._width = width
        self._height = height
        color = Brick._COLORS[hits]
        item = canvas.create_rectangle(x - width / 2, y - height / 2,
                                       x + width / 2, y + height / 2,
                                       fill = color, tags = 'brick')
        super().__init__(canvas, item)

    def hit(self):
        ''' 被球碰撞一次 '''
        self._hits -= 1
        if self._hits == 0:
            # delete brick from canvas
            self.delete()
        else:
            # change color
            self._canvas.itemconfig(self._item, fill = Brick._COLORS[self._hits])