import os
import random
import math
import pygame
from os import listdir
from os.path import isfile,join
pygame.init()

pygame.display.set_caption("Platformer")

background_color = (255,255,255)
WIDTH,HEIGHT = 1000,800