# Face Detection


## HAAR CASCADING
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Download `haarcascade_frontalface_default.xml`.</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:
<img height="300" width="600" src="FaceDetectionAnalysis/HaarResult/FaceDetected/img_40.jpg">


## MTCNN
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Run `!pip install mtcnn` on cmd.</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:

<img height="300" width="600" src="FaceDetectionAnalysis/MTCNNResult/FaceDetected/img_40.jpg">


## DLIB FRONTAL_FACE_DETECTION
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Dlib python Library</li>
  <li>Download `mmod_human_face_detector.dat`</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:

<img height="300" width="600" src="FaceDetectionAnalysis/DlibResult/FRONTAL_FACE_DETECTOR/FaceDetected/img_40.jpg">


## DLIB CNN_FACE_DETECTION
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Dlib python Library</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:
<img height="300" width="600" src="FaceDetectionAnalysis/DlibResult/CNN/FaceDetected/img_40.jpg">


## LBP CASCADING FACE DETECTION
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Numpy Library</li>
  <li>Download `lbpcascade_frontalface.xml`</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:
<img height="300" width="600" src="FaceDetectionAnalysis/LBPResult/FaceDetected/img_40.jpg">

## DNN - RESNET
##### Setup & Pre-requisites
<ol>
  <li>OpenCV Library</li>
  <li>Numpy Library</li>
  <li>Download `Resnet_SSD_deploy.prototxt`</li>
  <li>Download `Res10_300x300_SSD_iter_140000.caffemodel`</li>
  <li>Change `PATH_TO_IMAGE` with image path which you want to test.</li>
</ol>

##### Result:
<img height="300" width="600" src="FaceDetectionAnalysis/ResNetResult/FaceDetected/img_40.jpg">
