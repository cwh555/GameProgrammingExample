import tkinter as tk
from GameObject import GameObject
import time

class Paddle(GameObject):
    def __init__(self, canvas, x, y, width = 80, height = 10):
        '''
            the shape is rectangle, init _width, _height
            _ball: Ball
            init _item
            call constructor of GameObject
        '''
        self._width = width
        self._height = height
        self._ball = None
        self._moving = False
        item = canvas.create_rectangle(x - width / 2, y - height / 2,
                                       x + width / 2, y + height / 2,
                                       fill = 'blue', tags = 'paddle')
        super().__init__(canvas, item)
        self._canvas.bind("<KeyPress-Left>",
                          lambda _: self._action(-1))
        self._canvas.bind("<KeyRelease-Left>",
                          lambda _: setattr(self, '_moving', False))
        self._canvas.bind("<KeyPress-Right>",
                          lambda _: self._action(1))
        self._canvas.bind("<KeyRelease-Right>",
                          lambda _: setattr(self, '_moving', False))

    def set_ball(self, ball):
        ''' set the ball  '''
        self._ball = ball

    def move(self, offset):
        ''' move the paddle horizontally'''
        coords = self.get_position()
        # get the width of canvas
        width = self._canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super().move(offset, 0)
            if self._ball is not None:
                # ball should move with the paddle since the game has not started yet
                self._ball.move(offset, 0)

    def get_item(self):
        return self._item
    
    def _set_time(self) -> None:
        self._time = time.time()

    def _get_time(self) -> float:
        return time.time() - self._time
    
    def _action(self, direction: int) -> None:
        self._moving = True
        self._set_time()
        self._continue_moving(direction)

    def _continue_moving(self, direction: int) -> None:
        if self._moving:
            self.move(10 * direction * (self._get_time() + 0.5))
            self._canvas.after(50, lambda: self._continue_moving(direction))