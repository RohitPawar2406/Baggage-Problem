#Importing Libraries
import cv2
import numpy as np

# Global variables
refPT = []
cropping =False

# SHOWING IMAGE
def show_pic(img,name=None):
    cv2.imshow(f"{name} Image!!",img)
    if cv2.waitKey(0) & 0xFF:
        cv2.destroyAllWindows()  

''' CLICKING REACTANGULAR FRAME AND GETTING THAT PIXELS ONLY INTO SAME MATRIX'''
def click_crop(event,x,y,flags,params):
    global refPT,cropping;
    
    if event==cv2.EVENT_LBUTTONDOWN:
        refPT=[(x,y)]
        cropping=True
    elif event == cv2.EVENT_LBUTTONUP:
        refPT.append((x,y));
        cropping = False
        
        cv2.rectangle(image, refPT[0], refPT[1],(0,255,0),2)
        cv2.imshow('image',image)

''' GRABCUT CV FUNCTION IS IMPLEMENTED WITH ITS PARAMERTES'''
def grabCut(image,refPT):
    bgModel = np.zeros((1,65))*255
    fgModel = np.zeros((1,65))*255
    mask = np.zeros(image.shape[:2],np.uint8)
    rect = (refPT[0][0],refPT[0][1],refPT[1][0],refPT[1][1])
    cv2.grabCut(image,mask, rect,bgModel,fgModel,7, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    image = image*mask2[:,:,np.newaxis]
    show_pic(image,"GrabCut")
    return image
'''RESIZING AND SAVING CROPPED/RECTANGULAR IMAGE INTO A FOLDER''' 
def resize_saving_cropFile(image,refPT):
    res = image.copy()
    res_pic = image[refPT[0][1]:refPT[1][1] , refPT[0][0]:refPT[1][0]]
    show_pic(res_pic,"Re-Size Pic")
    cv2.imwrite('grab_resized_images/1.png',res_pic)
    
################ IMPLEMENTATION STARTS FROM HERE #########################
if __name__=='__main__':
    image = cv2.imread('threat_png/1.png',-1)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback('image',click_crop)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            image = clone.copy()
            break;
    cv2.destroyAllWindows()
    image=grabCut(image,refPT)
    #resize_saving_cropFile(image,refPT)
    
    # Reading Grabing .png photos
    grab_img = cv2.imread('grab_resized_images/1.png')
    show_pic(grab_img,"Grab Image")
    