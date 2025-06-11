import tkinter as tk
import GameObject

class Ball(GameObject):
    def __init__(self, canvas, x, y, radius = 10, speed = 10, life = 3):
        '''
            初始化__radius, __direction[2], __speed, __life, __item
            call constructor of GameObject
        '''
        self.__radius = radius
        self.__speed = speed
        self.__life = life
        self.__direction = [1, -1]
        item = canvas.create_oval(x - radius, y - radius, 
                                         x + radius, y + radius,
                                         fill = 'white', tags = 'ball')
        super().__init(self, canvas, item)

    def get_life(self):
        ''' return life '''
        return self.__life

    def modify_life(self, delta):
        ''' __life += delta '''
        self.__life += delta