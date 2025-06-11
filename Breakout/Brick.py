import tkinter as tk
import GameObject

class Brick(GameObject):
    def __init__(self, canvas, x, y, hits):
      ''' hits 代表還可以被碰撞幾次 '''

    def hit(self):
      ''' 被球碰撞一次 '''