import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master: tk.Tk):
      '''
        初始化master(base class)
        初始化背景(canvas)
        初始化private成員變數：ball, paddle, bricks
  
        呼叫__setup_game()
      '''
  
    def __setup_game(self):
      '''
        移動ball, paddle到初始位置
        更新ball的生命值，並輸出在畫面上
        綁定space到self.start_game()
      '''
  
    def start_game(self):
      '''
        解除空白鍵綁定
        開始遊戲 呼叫self.__game_loop()
      '''
    def __game_loop(self):
      ''' 掌控遊戲情形：判斷ball的collision、生命值不夠而結束、磚塊全滅而勝利 '''
  
    # private method
    def __add_ball(self):
      ''' 新增球, 初始化與paddle的互動'''
  
    def __add_brick(self):
      ''' 新增一個磚塊，存放到dict中 '''
  
    def __draw_text(self, x: int, y: int, text: str, size = '40'):
      ''' 協助輸出文字在指定位置 '''
  
    def __update_lives_text(self):
      ''' 從ball獲取生命值，並更新輸出在畫面上的文字 '''
  
    def __check_collide(self):
      ''' 判斷ball是否有與其他物體(paddle, bricks)碰撞（不包含邊界) '''
    
    def __collide(self, game_object):
      ''' 
        確定產生碰撞，改變球的方向
        若game_object is brick，呼叫brick的method移除
      '''
    
    def __update_ball(self):
      ''' call collide first, 移動ball  '''