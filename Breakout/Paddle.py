import tkinter as tk
import GameObject

class Paddle(GameObject):
    def __init__(self, canvas, x, y, width = 80, height = 10):
        '''
            the shape is rectangle, init __width, __height
            __ball: Ball
            init __item
            call constructor of GameObject
        '''
        self.__width = width
        self.__height = height
        self.__ball = None
        item = canvas.create_rectangle(x - width / 2, y - height / 2,
                                       x + width / 2, y + height / 2,
                                       fill = 'blue')
        super().__init__(canvas, item)

    def set_ball(self, ball):
        ''' set the ball  '''
        self.__ball = ball

    def move(self, offset):
        ''' move the paddle horizontally'''
        coords = self.getposition()
        # get the width of canvas
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super().move(offset, 0)
            if self.__ball is not None:
                # ball should move with the paddle since the game has not started yet
                self.__ball.move(offset, 0)