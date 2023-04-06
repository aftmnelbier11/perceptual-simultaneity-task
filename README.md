# Perceptual Simultaneity Task 

An open source script to behaviorally assess visotemporal perception

## Description

The Perceptual Simultaneity Task (PST) assesses visotemporal perception in a classic simultaneity judgment paradigm using psychophysical measures. This repo offers a Python script for experimental presentation. The PST was developed based on the methods described in Falter et al. (2012).

## Getting Started

### System Dependencies

* Python3.8
* PsychoPy

### Hardware

* 120 Hz monitor

### Tested Usage

This code has been tested using Python3.8 and Psychopy 2020.2.5 (via PyCharm 2021.1.3) on a Lenovo Thinkpad (Windows OS) with an Acer 120 Hz monitor for presentation. Psychopy is best supported by Python3.8, while newer versions of PsychoPy (e.g., 2023.1.0) are possible to use. It should also be possible to run from the terminal or other Python-supported environments assuming the necessary dependencies are installed. 

### Installing

* Download the script and unzip it in your desired directory. 
* No modifications are needed to specify the working directory. 
* A GUI for participant data is initialized at script startup. You may wish to add/omit/adjust entries in the code for your experimental purposes.  

### Executing program

* Run `PST.py` from your desired Python environment or in the command line.   
* Enter your participant ID and additional subject demographics into the startup GUI. 

### Setup Advice

Because the PST is temporally sensitve at frame-by-frame level, you may wish to try out the presentation of the stimuli before starting data collection. 
This has been previously tested using a GoPro (or any camera that can record with a 120 Hz refresh rate), 120 Hz monitor, and [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve). Recordings can be viewed by frames to ensure that each stimuli is presented as expected. 


## Experimental Design 

* 1 simultaneous condition, 12 simultaneous-onset-asynchronies (SOAs) 
* 5 experimental blocks (52 trials / block) + 1 practice block (10 trials)
* Responses are recorded as 'c' (= simultaneous onset) or 'm' (= non-simultaneous onset)
* See Falter et al. (2012) for further details. 

### Outputs

A .csv, .log, and frameseries.txt file are generated for each participant. The .csv file is a customized output of the data that is constructed using a PsychoPy DataHandler - **(!) this file is relevant for analysis**. The log file is automatically generated by PsychoPy. The frameseries.txt is a custom log file of the frame-by-frame presentations. The .log and frameseries.txt are relevant for trouble shooting. 

### Language

The PST is available in English and German. 

## Author

Afton Nelson, M.Sc.

## Acknowledgments

A special thanks to Carola Bloch and Dr. Irene Sophia Plank for their roles in troubleshooting the PST. 

## References
Falter, C. M., Elliott, M. A., & Bailey, A. J. (2012). Enhanced visual temporal resolution in autism spectrum disorders. PLoS One, 7(3), e32774.
