import tkinter as tk

class GameObject:
    def __init__(self, canvas, item):
        '''
            初始化_canvas, _item
        '''
        self._canvas = canvas
        self._item = item
        
    
    def get_position(self):
        '''
            return position in canvas
        '''
        return self._canvas.coords(self._item)

    def move(self, x, y):
        '''
            move to (x, y)
        '''
        self._canvas.move(self._item, x, y)

    def delete(self):
        '''
            delete the item from canvas
        '''
        self._canvas.delete(self._item)