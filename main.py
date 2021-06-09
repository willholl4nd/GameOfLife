import os
import numpy as np
import random

from PIL import Image

black = [0,0,0]
white = [255,255,255]

class GameOfLife:
    def __init__(self, name, width = 1000, height = 1000, threshold = .5):
        self.name = name
        self.width = width
        self.height = height
        self.frame1 = np.empty((height, width, 3), dtype=np.uint8)
        self.frame2 = np.empty((height, width, 3), dtype=np.uint8)
        self.threshold = threshold
    
    def save_to_image(self, count):
        img = Image.fromarray(self.frame1)
        img.save(self.name + f"/{count}.jpg")

    def randomize(self):
        for i in range(self.height):
            for j in range(self.width):
                if(random.random() < self.threshold):
                    self.frame1[i][j] = white
                else:
                    self.frame1[i][j] = black

    def algorithm(self, generations = 100):
        os.system(f'mkdir {self.name}')

        for g in range(generations):
            self.save_to_image(g) 

            for i in range(self.height):
                for j in range(self.width):
                    self.frame2[i][j] = white

            for i in range(self.height):
                for j in range(self.width):
                    n_count = self.get_neighbor_count(i, j)
                    if(n_count == 2 and np.all(self.frame1[i][j] == 0)):
                        self.frame2[i][j] = black
                    elif(n_count == 3):
                        self.frame2[i][j] = black
                    else:
                        self.frame2[i][j] = white


            for i in range(self.height):
                for j in range(self.width):
                    self.frame1[i][j] = self.frame2[i][j]

    def get_neighbor_count(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.in_bounds(row+i, col+j)):
                    check = self.frame1[row+i][col+j]
                    if(np.all(check == 0)):
                        count += 1
        return count


    def in_bounds(self, i, j):
        return i >= 0 and i < self.height and j >= 0 and j < self.width


if( __name__ == "__main__"):
    GOL = GameOfLife("test", 100, 100)
    GOL.randomize()
    GOL.algorithm()