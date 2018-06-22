# VoiceNavi-with-drowsiness-detect-on-RPI3

Step1: What do we need?
=======================
In this guide, we will be using:

  - Raspberry Pi 3
  - Official Raspberry Pi 3.5” Display
  - USB microphone
  - Speaker
  - PiCamera

Step2: Setting Up Environment
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

Step3: Setting Up Hardware
==========================

In order to setup necessary hardwares mentioned in step1, we are going through some dependencies installing and configuration setting process. Insert the following code in RPI3 terminal:

```
$ sudo apt-get update
$ sudo apt-get -y upgrade
```

Installing PiCamera dependencies and enabling SPI and Camera interface used by PiCamera: 

```
$ pip install picamera[array]
$ sudo raspi-config
```

![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/Camera.png "Enable camera interface")
![Example](https://github.com/colinycw/VoiceNavi-with-drowsiness-detect-on-RPI3/blob/master/SPI.png "Enable SPI interface")

  Step3.1: Test out the PiCamera module
  -------------------------------------
  
  Before we run into the code, let do a quick check on whether camera is working properly.
