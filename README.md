# VoiceNavi-with-drowsiness-detect-on-RPI3

In this guide, we will be using:

  - Raspberry Pi 3
  - Official Raspberry Pi 3.5” Display
  - USB microphone
  - Speaker
  - PiCamera

Setting Up Hardware
===================

In order to setup necessary hardware running on RPI3, we are going through some dependencies installing and configuration setting process. Insert the following code in RPI3 terminal:

```
$ sudo apt-get update
$ sudo apt-get --dist -y upgrade
```

Enable the SPI interface used by PiCamera: 
