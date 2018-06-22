# VoiceNavi-with-drowsiness-detect-on-RPI3

The primary purpose for this navigation system is where it can act as a verbal guidance for the driver on their way but simultaneously detecting whether the driver is truly focusing on driving! This is particularly useful when people are in a long haul drive or for someone like truck drivers who would usually driving for a long time. By implementing this system on every cars, we are able to create a safer driving environment not only for driver themselves but also for those people who have rights to be on a safe and secure highway or road. Nonetheless, the most effective way of protecting everyone's safety while driving is operating vehicles according to local regulations as well as making sure we are in the best physical and mental state of driving a car.

Step 1: What do we need?
=======================
In this guide, we will be using:

  - Raspberry Pi 3
  - Official Raspberry Pi 3.5” Display
  - USB microphone
  - Speaker
  - PiCamera

Step 2: Setting Up Environment
=============================
For the sake of tidiness in system wide python library, we will be finishing this whole project within one virtual environment. The package management program we are using in this project is called "Berryconda", which is a Conda based distribution for the RPI3. To install Berryconda on RPI3, first download installer script according to the Raspberry Pi you are using from the website below and follow the steps:

https://github.com/jjhelmus/berryconda

```
$ chmod +x Berryconda3-2.0.0-Linux-armv7l.sh`
$ ./Berryconda3-2.0.0-Linux-armv7l.sh
```

After following the prompt and finish the installation, we are then creating a virtual environment called "navi" and going into the virtual environment.

```
$ conda create -n navi
$ conda install conda
$ source activate navi
```

For more information on how to use Conda, visit documentation website on https://conda.io/docs/

Step 3: Setting Up Hardware
==========================

In order to setup necessary hardwares mentioned in step1, we are going through some dependencies installing and configuration setting process. Insert the following code in RPI3 terminal:

```
$ sudo apt-get update
$ sudo apt-get -y upgrade
$ sudo apt-get install python2-dev python3-dev
```

Enabling SPI and Camera interface used by PiCamera and changing source for speaker output: 

```
$ sudo raspi-config
```

![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/Camera.png "Enable camera interface")
![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/SPI.png "Enable SPI interface")
![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/Audio1.png "Audio")
![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/Audio2.png "Audio")

  Step 3.1: Test out the PiCamera module
  --------------------------------------
  
  Before we run into the code, let do a quick check on whether camera is working properly.
  
  ```
  $ raspistill -o output.jpg
  ```

  Now you shoud see an "output.jpg" file in your current directory. Open and see it!
  
  Step 3.2: Test out the Speaker and Microphone
  ---------------------------------------------
  
  ```
  $ arecord -D plughw:1,0 -d 3 test.wav && aplay test.wav
  ```
  
  For detailed setup for microphone, visit USB microphone wiki on 
  http://wiki.sunfounder.cc/index.php?title=To_use_USB_mini_microphone_on_Raspbian
  
Step 4: Setting Up Drowsiness detection
=======================================

In this section, we are going to build up drowsiness detection on RPI3. Before that, libraries required for executing related python script are OpenCV, dlib. The installation guidance for these libraries are described carefully below. Follow it step by step.

  Step 4.1: Install OpenCV3
  -------------------------
  First of all, expand your file system to make sure we are able to use full space in our SD card.
  ```
  $ sudo raspi-config
  ```
  ![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/Expand%20File%20System.png "Expand file system")
  
  Next, we want to uninstall several applications that will not be used withing this project in order to free up some space.
  ```
  $ sudo apt-get remove --purge wolfram-engine libreoffice*
  $ sudo apt-get clean
  $ sudo apt-get autoremove
  ```
  
  We then need to install some developer tools which will help us on OpenCV installation process. This process is going to take some times, but don't get your coffee yet. I'll inform you later at the best timing to get it.
  ```
  $ sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran python2.7-dev python3-dev
  ```
  
  Now we have our dependencies installed, we will download and unzip OpenCV source codes for future execution.
  ```
  $ cd ~
  $ wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
  $ wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
  $ unzip opencv.zip
  $ unzip opencv_contrib.zip
  ```
  
  Before compiling OpenCV source code, we have to install Numpy package and setup our build by typing:
  ```
  $ pip install numpy
  $ cd ~/opencv-3.3.0/
  $ mkdir build
  $ cd build
  $ cmake -D CMAKE_BUILD_TYPE=RELEASE \
  $ -D CMAKE_INSTALL_PREFIX=/usr/local \
  $ -D INSTALL_PYTHON_EXAMPLES=ON \
  $ -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
  $ -D BUILD_EXAMPLES=ON ..
  ```
  
  Before we start the compiling process, we should increase our swap space size by changing CONF_SWAPSIZE value in /etc/dphys-swapfile from 100 (default) to 1024 and reactivate our configuration after modification. (Remember the change the value back after the installtion process.)
  ```
  $ # set size to absolute value, leaving empty (default) then uses computed value
  $ #   you most likely don't want this, unless you have an special disk situation
  $ CONF_SWAPSIZE=1024
  $ sudo /etc/init.d/dphys-swapfile stop
  $ sudo /etc/init.d/dphys-swapfile start
  ```
  
  Here comes the compiling process! This will be a good time for you to grab some coffee and desserts cause this will takes a long long time.....................................(Probably 2 to 3 hours or more)
  ```
  $ make -j4
  ```
  
  Having a nice rest? From here, the last thing we need to do is install OpenCV on RPI3:
  ```
  $ sudo make install
  $ sudo ldconfig
  ```
  
  And finally, create a soft link OpenCV bindings from where your OpenCV is installed.
  ```
  $ sudo ln -s /usr/local/lib/python2.7/dist-packages/cv2.so /home/pi/berryconda3/envs/navi/lib/python3.5/site-packages
  ```
  
  Step 4.2: Install dlib
  ----------------------

  First of all, we are going to install prerequisites for dlib library by typing the following command into terminal:
  ```
  $ sudo apt-get install build-essential cmake libgtk-3-dev libboost-all-dev
  $ pip install scipy scikit-image
  ```
  
  Install dlib by typing:
  ```
  $ pip install dlib
  ```
  
  Step 4.3: Testing OpenCV and dlib
  ---------------------------------
  
  If the installation process was working fine, the results of import command should give you the exact same output as depicted in the picture below.
  
  ![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/opencv%20and%20dlib%20test.png)

  Step 4.4: Building drowsiness detection with OpenCV and dlib
  ------------------------------------------------------------
  
  To start our implementation, we will need to install some packages in our environment.
  ```
  $ pip install imutils playsound pyobjc
  ```
  
  Then download the Drowsiness detection folder and place it at somewhere easy to reach. Execute python script file "donotsleep.py" by type in:
  ```
  $ python donotsleep.py --shape-predictor landmarks.dat --alarm alarm.wav
  ```
  
  By this time when your eyes have been closed beyond total of 10 frames, indicating the driver is probably fall in a sleep, the speaker will play out alarm sound to wake the driver up. For the testing purpose, the screen will also show "DROWSINESS ALERT" in the frame. The result is depicted as the following figure.
  ![Example]()
  
  Well done! You have now created a driver drowsiness warning system on your RPI3.
  
  Next, we will keep on to install navigation application on our RPI3.
  
Step 5: Setting Up Waze Navigation Application
==============================================

The program we will be using for navigation is an open source application called "Waze". The installation process of it would be relatively simple in contrast to the previous step. To install waze on RPI3, we need to download the source code of backport of waze to linux on this website: https://github.com/sashakh/waze

And then, download required dependencies for building waze by type in the following code:
```
$ sudo apt-get install libgps-dev libsqlite3-dev libgtk2.0-dev libagg-dev libfribidi-dev libssl-dev
$ make
$ make install-user
$ make install
```

To run the program, execute code in terminal:
```
$ waze
```

Because of the fact that we are not using a working gps module for positioning in this project, we can only use this as a demo and see the result in the picture below. But it still proves that the program is working properly on RPI3!
![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/waze.png "Waze")

Step 6: Hook Up All The Stuff
=============================

Just like what we have mentioned at the very begining of this guide. We want a navigation system act as an verbal guidance and also detecting drive's degree of concentration all at the same time. Now we have two of our major modules each working perfectly by their own, we are then going to let them doing their jobs in a simultaneous manner. To order to do this, create a python script called "saveDrive.py" and insert the following code in it: (Or you may directly download the python script file in this branch.)

```
import os
import threading 

def drowsinessDetect():
	os.system("sudo modprobe bcm2835-v4l2")
	os.system("python ~/IOT/Drowsiness\ detection/nosleep.py --shape-predictor ~/IOT/Drowsiness\ detection/landmarks.dat --alarm ~/IOT/Drowsiness\ detection/alarm.wav")

def navigation():
	os.system("waze")

t1 = threading.Thread(target=drowsinessDetect, args=[])
t2 = threading.Thread(target=navigation, args=[])

t1.start()
t2.start()
```

After that, we can execute the python script by typing in the code below and make this system working. Drive safe!
```
$ python saveDrive.py
```
