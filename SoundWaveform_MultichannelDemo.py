# -*- coding: utf-8 -*-

# 2019.4.23 ————读取wav文件[多通道]，显示波形————
 
import wave
import matplotlib.pyplot as plt
import numpy as np
import os
 
filepath = "F:/Programs/python_all/" #添加路径
filename = "Oldboy.wav"
f = wave.open(filepath+filename,'rb')
# filepath = "./data/" #添加路径
# filename= os.listdir(filepath) #得到文件夹下的所有文件名称  
# f = wave.open(filepath+filename[0],'rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
waveData = np.reshape(waveData,[nframes,nchannels])
f.close()
# plot the wave
time = np.arange(0,nframes)*(1.0 / framerate)
plt.figure()
plt.subplot(5,1,1)
plt.plot(time,waveData[:,0])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-1 wavedata")
plt.grid('on')#标尺，on：有，off:无。
plt.subplot(5,1,3)
plt.plot(time,waveData[:,1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-2 wavedata")
plt.grid('on')#标尺，on：有，off:无。

# 下面为3通道的显示
# plt.subplot(5,1,5)
# plt.plot(time,waveData[:,2])
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Ch-3 wavedata")
# plt.grid('on')#标尺，on：有，off:无。

plt.show()


