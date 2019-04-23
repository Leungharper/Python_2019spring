# -*- coding: utf-8 -*-

# 2019.4.23 ————录音————
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 8 #录音秒数
WAVE_OUTPUT_FILENAME = "Oldboy.wav"
FilePath = 'F:/Programs/python_all/' # 后加的【左划线避免出现转义字符】
# FilePath = r'F:\Programs\python_all\' # 后加的【r表示原始字符，不转义】

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("开始录音,请说话......")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("录音结束,请闭嘴!")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(FilePath + WAVE_OUTPUT_FILENAME, 'wb') # 后改
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


