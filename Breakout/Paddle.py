import tkinter as tk
import GameObject

class Paddle(GameObject):
    def __init__(self, canvas, x, y):
      '''
        the shape is rectangle, init __width, __height
        __ball: Ball
        init __item
        call constructor of GameObject
      '''

    def set_ball(self, ball):
      ''' set the ball  '''

    def move(self, offset):
      ''' move the paddle horizontally'''