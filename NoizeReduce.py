# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1arNfVlx_BrqAkA7MlYSPc8DnjHEIRUYO
"""

colab_requirements = [
    "pip install tensorflow-gpu==2.0.0-beta0",
    "pip install librosa",
    "pip install noisereduce",
    "pip install soundfile",

]
import sys, subprocess

def run_subprocess_command(cmd):
    # run the command
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    # print the output
    for line in process.stdout:
        print(line.decode().strip())

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    for i in colab_requirements:
        run_subprocess_command(i)

import matplotlib.pyplot as plt
from google.colab import files
import noisereduce as nr
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

upload = False
import urllib.request
import soundfile as sf
import io

files.upload()
upload = True

if upload:
  rate, data = wavfile.read("Before.wav")
else:
  url = "https://github.com/aracdo/NoizeReduceTestPY/blob/main/Before.wav?raw=true"
  response = urllib.request.urlopen(url)
  data, rate = sf.read(io.BytesIO(response.read()))
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)
print(data)

if upload:
  noizeRate, noizeData = wavfile.read("noize.wav")
else:
  url = "https://github.com/aracdo/NoizeReduceTestPY/blob/main/noize.wav?raw=true"
  response = urllib.request.urlopen(url)
  noizeData, noizeRate = sf.read(io.BytesIO(response.read())) 
fig, ax = plt.subplots(figsize=(20,3))
ax.plot(noizeData)
print(noizeData)

noisy_part = noizeData[0:175000]
print(noisy_part,'\n',data)

reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=noisy_part, verbose=True)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(reduced_noise)

import IPython
IPython.display.Audio(data=reduced_noise, rate=rate)