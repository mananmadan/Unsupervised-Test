# AI Proctoring System

## Features
- GUI for test taking
- Face Verification
- Mouse Location Tracking to detect cheating
- Facial Tracking during exam to detect fraud

## Output
![output](output.jpg)


## Installation
- create an enviroment using requirements.txt
- FOR CONDA INSTALL
```
    conda create --name <name> --file requirements.txt
```
- FOR MANUAL INSTALL
- OpenCV for facial detection
```
   conda install -c conda-forge opencv
```
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
- Face Recognition Library
```
  conda install -c conda-forge face_recognition
```
- Library for clicking screenshots in case cheating attempt happens
```
  conda install -c conda-forge pyautogui
```
- Linux Install for clicking screenshots using programs
```
  sudo apt-get install scrot
```
- Sound Device for recoding audio
```
  conda install -c conda-forge python-sounddevice
```

## Future Scope
- Object Detection to detect objects through which cheating can be done!
- creditability score using the performance and cheating instances!


