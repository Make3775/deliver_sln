import os
import shutil
import cv2
  
# Function to extract frames from the video
def CaptureFrame(path): 
      
    # Path to video file 
    video_Object = cv2.VideoCapture(path)
    #Frame number counter
    count = 0
  
    # Has the frame been extracted successfully! 
    success = True
  
    while success: 

        #directory = "frames" 
        success, image = video_Object.read()
        #path = os.path.join(path, directory)
        #while os.path.isdir(path):
         #   shutil.rmtree(path, ignore_errors=True)
        #os.makedirs(path, mode=0o777) #intention was to load to a frame folder!

        # Saves the frames with frame-count to distinguish the frame number
        cv2.imwrite("frame%d.jpg" % count, image) 
        #increment the counter
        count += 1
  #main execution
if __name__ == '__main__': 
  
    # Calling the function 
    #Try out with any folder and see the frames generated
    CaptureFrame("video_data/catch/catch/Ball_hochwerfen_-_Rolle_-_Ball_fangen_(Timo_3)_catch_f_cm_np1_le_goo_0.avi") 