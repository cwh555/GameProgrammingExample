import tkinter as tk
from Ball import Ball
from Paddle import Paddle
from Brick import Brick

class Game(tk.Frame):
    def __init__(self, master: tk.Tk):
        '''
            初始化master(base class)
            初始化背景(canvas)
            初始化private成員變數：ball, paddle, bricks
    
            呼叫_setup_game()
        '''
        super().__init__(master)
        self._width = 610
        self._height = 400
        self._canvas = tk.Canvas(self, bg = '#aaaaff',
                                  width = self._width, height = self._height)
        self._canvas.pack()
        self.pack()
        # store paddle, bricks to handle the situation that collide with ball
        self._items = {}
        self._ball = None
        self._paddle = Paddle(self._canvas, self._width / 2, 326)
        self._items[self._paddle.get_item()] = self._paddle
        # init bricks
        for x in range(5, self._width - 5, 75):
            self._add_brick(x + 37.5, 50, 2)
            self._add_brick(x + 37.5, 70, 1)
            self._add_brick(x + 37.5, 90, 1)
        self._hud = None   # record life text
        self._setup_game()
        self._canvas.focus_set()

    def _setup_game(self):
        '''
            移動ball, paddle到初始位置
            更新ball的生命值，並輸出在畫面上
            綁定space到self.start_game()
        '''
        self._add_ball()
        self._update_lives_text()
        self._text = self._draw_text(300, 200, "Press Space to start")
        self._canvas.bind('<space>',
                          lambda _: self.start_game())
  
    def start_game(self):
        '''
            解除空白鍵綁定
            開始遊戲 呼叫self._game_loop()
        '''
        self._canvas.unbind('<space>')
        self._canvas.delete(self._text)
        self._paddle.set_ball(None)
        self._game_loop()

    def _game_loop(self):
        ''' 掌控遊戲情形：判斷ball的collision、生命值不夠而結束、磚塊全滅而勝利 '''
        self._check_collide()
        num_bricks = len(self._canvas.find_withtag('brick'))
        if num_bricks == 0:
            self._ball.set_speed(None)
            self.draw_text(300, 200, 'You win!')
        elif self._ball.get_position()[3] >= self._height:
            self._ball.set_speed(None)
            self._ball.modify_life(-1)
            if self._ball.get_life() <= 0:
                self._draw_text("Game over")
            else:
                self.after(1000, self._setup_game)
        else:
            self._ball.update_ball()
            self.after(50, self._game_loop)
  
    # private method
    def _add_ball(self):
        ''' 新增球, 初始化與paddle的互動'''
        if self._ball is not None:
           # delete old one
           self._ball.delete()
        paddle_coords = self._paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self._ball = Ball(self._canvas, x, 310)
        self._paddle.set_ball(self._ball)
  
    def _add_brick(self, x, y, hits):
        ''' 新增一個磚塊，存放到dict中 '''
        brick = Brick(self._canvas, x, y, hits)
        self._items[brick.get_item()] = brick
  
    def _draw_text(self, x: int, y: int, text: str, size = '40'):
        ''' 協助輸出文字在指定位置 '''
        font = ('Helvetica', size)
        return self._canvas.create_text(x, y, text = text, font = font)
  
    def _update_lives_text(self):
        ''' 從ball獲取生命值，並更新輸出在畫面上的文字 '''
        text = "Lives: %s" % self._ball.get_life()
        if self._hud is None:
            self._hud = self._draw_text(50, 20, text, 15)
        else:
            self._canvas.itemconfig(self._hud, text = text)
  
    def _check_collide(self):
        ''' 判斷ball是否有與其他物體(paddle, bricks)碰撞（不包含邊界) 並處理碰撞物'''
        ball_coords = self._ball.get_position()
        items = self._canvas.find_overlapping(*ball_coords)
        objects = [self._items[x] for x in items if x in self._items]
        self._ball._collide(objects)
