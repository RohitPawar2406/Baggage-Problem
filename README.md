# Baggage Problem  

This problem statement was by BaggageAI to segment the threat objects and paste it on background images. 

# Input images-  

Threat objects => /threat_png/     

Background images =>  /background_images/ 

# Outputs Images from Program - 

1)Final Outputs => /Assignement_Outputs/  ; 25 outputs images with each background with each threat objects has been placed. <br/>
2)Images after GrabCut & Cropping operations=> /grab_resized_images/ ; Grabcut and Cropping operation has done on all threat objects. 

# To Run program-  

Step 1 => Clone the project.  

Step 2 => open terminal and run python main.py 

Step 3 => After each image has been shown press ‘q’ for moving and seeing next images.  

# Description of each python file -  

1) select_threat_object.py -> This file work as follows :-	  <br/>

a)Reading Threat object .  <br/>
b)Using Mouse event from openCV  , we draw a rectangular box and passing to the Grabcut segmentation process.  <br/>
c)Grabcut function takes above rectangular co-ordinates and segment given image with the help of masking process.  <br/>
d)After Segmentation images having a black background , we resize images and save them into / grab_resized_images/ <br/>
