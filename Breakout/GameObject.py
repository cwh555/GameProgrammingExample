import tkinter as tk

class GameObject:
    def __init__(self, canvas, item):
        '''
            初始化__canvas, __item
        '''
        self.__canvas = canvas
        self.__item = item
        
    
    def get_position(self):
        '''
            return position in canvas
        '''
        return self.__canvas.coords(self.__item)

    def move(self, x, y):
        '''
            move to (x, y)
        '''
        self.__canvas.move(self.__item, x, y)

    def delete(self):
        '''
            delete the item from canvas
        '''
        self.__canvas.delete(self.__item)