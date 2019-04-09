# Speak with style : a demo
Demo of a synthesized utterance with different styles with controllable intensities.

Also see this working [here](http://noetits.com/speak-with-style-demo/) in javascript.

## What it is
This demo plays samples of the result of a work on controllable expressive speech synthesis. This repository does not contain the model itself.

We developed of a multi-style TTS system with the possibility to control the intensity of style categories. It is a modified version of [DCTTS](https://github.com/Kyubyong/dc_tts) that takes an encoding of the category at the input of the decoder. During training, a simple one-hot encoding is used. The size of the code is the number of different styles. At synthesis stage, we can modify the intensity of a style category by inputting other codes. 

In this demo, we interpolate between neutral and each style. 

Only the number corresponding to neutral and the category with which we interpolate are non-zero. The sum of the numbers of a code is one. 

Example:

Let's assume we have three categories (neutral, happy, angry). A code to have "quite angry" speech could be 

[0.3, 0, 0.7]

## How to use

You need git and python. In a prompt:
```
git clone https://github.com/numediart/speak_with_style_demo/
pip install -r requirements.txt
```

Then launch the demo:
```
python demo_set_of_codes.py
```

A polar plot with axes appears. If you click on the plot, an audio file of an utterance will be played.
The program will select the style of the closest axis. The intensity corresponds to the distance from the center. The center is neutral, and the furthest you are, the more stylish it is.
