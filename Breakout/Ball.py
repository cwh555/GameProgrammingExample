import tkinter as tk
import GameObject

class Ball(GameObject):
    def __init__(self, canvas, x, y, radius = 10, speed = 10, life = 3):
        '''
            初始化_radius, _direction[2], _speed, _life, _item
            call constructor of GameObject
        '''
        self._radius = radius
        self._speed = speed
        self._life = life
        self._direction = [1, -1]
        item = canvas.create_oval(x - radius, y - radius, 
                                         x + radius, y + radius,
                                         fill = 'white', tags = 'ball')
        super().__init__(self, canvas, item)

    def get_life(self):
        ''' return life '''
        return self._life

    def modify_life(self, delta):
        ''' _life += delta '''
        self._life += delta