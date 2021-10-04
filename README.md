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
&nbsp; &nbsp; a)Reading Threat object .  <br/>
&nbsp; &nbsp; b)Using Mouse event from openCV  , we draw a rectangular box and passing to the Grabcut segmentation process.  <br/>
&nbsp; &nbsp; c)Grabcut function takes above rectangular co-ordinates and segment given image with the help of masking process.  <br/>
&nbsp; &nbsp; d)After Segmentation images having a black background , we resize images and save them into / grab_resized_images/ <br/>

2) training.py-> This file work as follows :- 
&nbsp; &nbsp; a) main function is called from main.py where it will read background image and also a threat object from /grab_resized_images/ 
&nbsp; &nbsp; b) now correction function is performed that is the black pixels which are observing are not absolute zero it is tending to zero. Therefore, this function makes all pixels 0 who has pixels size less than 10. 
&nbsp; &nbsp; c) Then in placing_threat_object( ) function we are just adding that segmented image of threat to the background image where condtion is that pixels are only added which are not 0 that means only colored object is added to background. 
