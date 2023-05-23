import os
import glob
import numpy as np
from PIL import Image

#split the data from the txt file
split_data = {}
for file in sorted(glob.glob('test_train_splits/')):
    with open(file) as f:
        for line in f:
            split_data[line.split(' ')[0].split('.')[0]] = int(line.split(' ')[1])

#declare any location in the video_data folder
location = 'video_data'
#store in empty array
train_data , train_labels = [],[]
test_data , test_labels = [],[]
validation_data , validation_labels = [],[]
classes = []
#object
labels = {}
#pick all folder names->Ensure that every rar file has its own directory
for folder_name in sorted(os.listdir(location)):
    classes.append(folder_name)
for i in range(len(classes)):
    tmp = np.zeros(len(classes),dtype=np.int32)
    tmp [i] = 1
    labels[classes[i]]=tmp


for video in classes:
    for video_name in sorted(glob.glob(location+video+'/*')):
        print(video_name.split('/')[-1])
        print(video)
        print('='*50)
        size_x = 220
        size_y = 300

        #train model
        if split_data[video_name.split('/')[-1]] == 1 :
            for img in sorted(glob.glob(video_name+'/*')):
                print('Image is being processed. Hold on!',end='\r')
                image = Image.open(img)
                #resize the image
                image = image.resize((size_x,size_y), Image.ANTIALIAS)
                tmp = np.asarray(image)
                train_data.append(tmp)
                train_labels.append(labels[video])
        
        #testing data     
        elif split_data[video_name.split('/')[-1]] == 2 :
            for img in sorted(glob.glob(video_name+'/*')):
                print('Image is being processed. Hold on!',end='\r')
                image = Image.open(img)
                #resize the image
                image = image.resize((size_x,size_y), Image.ANTIALIAS)
                tmp = np.asarray(image)
                test_data.append(tmp)
                test_labels.append(labels[video]) 
        
        #validation of data function
        elif split_data[video_name.split('/')[-1]] == 0 :
            for img in sorted(glob.glob(video_name+'/*')):
                print('Image is being processed. Hold on!',end='\r')
                image = Image.open(img)
                #resize the image
                image = image.resize((size_x,size_y), Image.ANTIALIAS)
                tmp = np.asarray(image)
                validation_data.append(tmp)
                validation_labels.append(labels[video])

                           
np.savetxt('train_data.txt',np.array(train_data))
np.savetxt('train_labels.txt',np.array(train_labels))


np.savetxt('test_data.txt',np.array(test_data))
np.savetxt('test_labels.txt',np.array(test_labels))


np.savetxt('validation_data.txt',np.array(validation_data))
np.savetxt('val_labels.txt',np.array(validation_labels))

