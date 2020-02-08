import numpy as np
import cv2 as cv
import os

# current directory path
file_path = './'

# image file name
img_file = IMAGE_FILE_NAME_HERE

threshold = 0.5  # human face's confidence threshold

# Load the pre-trained ResNetSSD caffe model
prototxt_file = file_path + 'Resnet_SSD_deploy.prototxt'
caffemodel_file = file_path + 'Res10_300x300_SSD_iter_140000.caffemodel'
net = cv.dnn.readNetFromCaffe(prototxt_file, caffeModel=caffemodel_file)
print('MobileNetSSD caffe model loaded successfully')

# Read picture
image = cv.imread(file_path + img_file)
origin_h, origin_w = image.shape[:2]

# Image preprocessing: resize, mean_subtrction, and scale
# https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
blob = cv.dnn.blobFromImage(cv.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

# Pass blobs as input into the network and propagate forward to get the output
net.setInput(blob)

# detections is a 4-dimensional list
# The third dimension is the number of faces detected on the image
# 1 in the fourth dimension is the category number of the object, 2 is the confidence, and 3: 7 is the bounding box position value
detections = net.forward()
print('Face detection accomplished')

# Traverse each face
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > threshold:
        # Take out the position value of the bounding box and restore it to the original image
        bounding_box = detections[0, 0, i, 3:7] * np.array([origin_w, origin_h, origin_w, origin_h])
        x_start, y_start, x_end, y_end = bounding_box.astype('int')

        label = '{0:.2f}%'.format(confidence * 100)
        cv.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 0, 255), 1)
        
        # Fill text background of painted text
        cv.rectangle(image, (x_start, y_start - 18), (x_end, y_start), (0, 0, 255), -1)
        cv.putText(image, label, (x_start+2, y_start-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv.imshow("Detected Faces",image)
cv.waitKey(0)
cv.destroyAllWindows()
