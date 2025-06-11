import tkinter as tk
import GameObject
import Brick

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

    def set_speed(self, speed):
        self._speed = speed

    def _collide(self, game_objects):
        ''' 
            確定產生碰撞，改變球的方向
            若game_object is brick，呼叫brick的method移除
        '''
        coords = self.get_position()
        x = (coords[0] + coords[2]) / 2
        if len(game_objects) > 1:
            self._direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()
            if x > coords[2]:
                self._direction[0] = 1
            elif x < coords[0]:
                self._direction[0] = -1
            else:
                self._direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit()

    def update_ball(self):
        ''' call collide first, 移動ball  '''
        self._check_collide()
        # bounce with boundary
        coords = self.get_position()
        width = self._canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self._direction[0] *= -1
        if coords[1] <= 0:
            self._direction[1] *= -1
        x = self._direction[0] * self._speed
        y = self._direction[1] * self._speed
        self.move(x, y)