############### IMPORTING lIBRARIES #####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

############### IMPORTING FILES AND MODULES ##############
from select_threat_object import show_pic
from training import main



##################### LOGIC ##############################

if __name__=="__main__":
    for i in range(0,5):
        for j in range(0,5):
            main(i,j)

'''
DONE BY - Rohit Arun Pawar
'''

