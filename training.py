############### IMPORTING lIBRARIES #####################
import cv2
import numpy as np


####################### FUNCTIONS #######################

# SHOWING IMAGE
def show_picture(img,name=None):
    cv2.imshow(f"{name} Image!!",img)
    if cv2.waitKey(0) & 0xFF:
        cv2.destroyAllWindows() 
        
# CORRECTION OF THREAT OBJECT PIXELS
def correction_of_Filter(threat_object,sw,sh,sc):
    for i in range(0,sw):      
        for j in range(0,sh):
            for k in range(0, sc):
                if threat_object[i, j, k] < 10:
                    threat_object[i, j, k] = 0
    return threat_object                    

# PLACING THREAT OBJECT ON BACKGROUND IMAGE
def placing_threat_object(background_Image, threat_object,sw,sh,sc,ii):
    if ii==3 :          # PLACING IN THE REACTANGULAR BOC OF 3.JPG. 
        add_in_i=400
        add_in_j = 430
    elif ii==4:         # PLACING IN THE REACTANGULAR BOC OF 4.JPG.
        add_in_i=250
        add_in_j = 808
    else :
        add_in_i = background_Image.shape[0]//2
        add_in_j = background_Image.shape[1]//2
    
    '''ADDING THE COLOR PIXELS OF THREAT OBJECTS AND NOT THE BLACK PIXELS
    TO THE BACKGROUND IMAGE'''
    for i in range(0,sw):      
        for j in range(0,sh):
            for k in range(0, sc):
                if threat_object[i, j, k] != 0:
                    background_Image[i+add_in_i, j+add_in_j, k] = threat_object[i,j, k]
    return background_Image                    


def main(i=0,j=0):
    background_Image =  cv2.imread(f'background_images/{i}.jpg')
    threat_object = cv2.imread(f'grab_resized_images/{j}.png')
    threat_object = cv2.resize(threat_object, (75,75))
    sw,sh,sc = threat_object.shape
    threat_object=correction_of_Filter(threat_object,sw,sh,sc)
    background_Image = placing_threat_object(background_Image, threat_object,sw,sh,sc,i)
    show_picture(background_Image,"Final")
    cv2.imwrite(f'Assignment_Outputs/{i}_{j}.png', background_Image)