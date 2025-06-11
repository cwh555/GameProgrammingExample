import tkinter as tk
import GameObject

class Ball(GameObject):
    def __init__(self, canvas, x, y):
      '''
        初始化__radius, __direction[2], __speed, __live, __item
        call constructor of GameObject
      '''

    def get_life(self):
      ''' return life '''

    def modify_life(self, delta):
      ''' __life += delta '''