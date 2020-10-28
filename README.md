# Ideas
- Track eyes , use geometry to figure out head facing direction
- Use CNN based facial keypoints and pose to pose difference to figure out head movement
- Also can use object detection to detect items that can be used for cheating

## Main FrameWorks
- OpenCV -> For Processing on Vedio and images
- TF , Keras -> For Deep Learning using facial keypoints

## Research on Ideas
1. Tracking eyes 
  - [Haar-Cascade-Approach](https://www.youtube.com/watch?v=RvfF9CDzn1s&ab_channel=ProgrammingKnowledge)
  - Advantages
    - Required Less Computer power
  - Disadvantage
    - accuracy is questionable!
2. Facial Keypoints
  - [Facial-Keypoint-Approach](https://www.youtube.com/watch?v=vC3bTziLRTA&ab_channel=NeuralDimension)
3. Object Detection
  - Fairly simple!
  - Not know wheather it will be helpful or not

## How to use?
- create an enviroment using requirements.txt
- FOR LINUX USERS
```
    conda create --name <name> --file requirements.txt
```
- FOR WINDOWS USERS
- OpenCV for facial detection
```
   conda install -c conda-forge opencv
```
- Tensorflow for facial keypoint detection
```
   conda install -c conda-forge tensorflow 
```
- **Above command can take time , also might be fail intial solves , but will install finally !**
- Pynput for tracking mouse !
```
   conda install -c conda-forge pynput
```
- Pyqt for GUI
```
   conda install -c anaconda pyqt
```
- Tkinkter also for GUI
```
   conda install -c anaconda tk
```
