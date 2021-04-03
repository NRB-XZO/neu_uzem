#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import speech_recognition as sr
from python_imagesearch.imagesearch import imagesearch
from playsound import playsound
from gtts import gTTS
import os
from time import sleep
from pyautogui import leftClick
import webbrowser
from datetime import datetime
import pyautogui
import random
import sys
name = " en ar bi"
def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Anlayamadım")
        except sr.RequestError:
            print("Sistem çalışmıyor")
        return voice
def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,1000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
saat = pyautogui.prompt(text="Ders saat kaçta ? (başında sıfır kullanmadan)",title="NRB SECURİTY",default="")
dakika = pyautogui.prompt(text="Ders kaçıncı dakikada ? (başında sıfır kullanmadan",title="NRB SECURİTY",default="")
url = pyautogui.prompt(text="Olası bir soruna karşın açık sayfanın urlsini giriniz",title="NRB SECURİTY",default="")
while True:
            hour = datetime.now()
            minute = datetime.now()
            if hour.hour==int(saat) and minute.minute == int(dakika):
                while True:
                    if imagesearch(image="toplantiya_katil.PNG")[0] > 0:
                        leftClick(imagesearch(image="toplantiya_katil.PNG")[0],
                                  imagesearch(image="toplantiya_katil.PNG")[1])
                        sleep(30)
                        if imagesearch(image="new1.PNG")[0] > 0:
                            leftClick(imagesearch(image="new1.PNG")[0], imagesearch(image="new1.PNG")[1])
                            sleep(10)
                            if imagesearch(image="new2.PNG")[0] > 0:
                                leftClick(imagesearch(image="new2.PNG")[0], imagesearch(image="new2.PNG")[1])
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    leftClick(imagesearch("new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    break
                                else:
                                    break
                            else:
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    break
                                else:
                                    break

                        else:
                            if imagesearch(image="new2.PNG")[0] > 0:
                                leftClick(imagesearch(image="new2.PNG")[0], imagesearch(image="new2.PNG")[1])
                                if imagesearch(image="new3.PNG")[0]>0:
                                    leftClick(imagesearch(image="new3.PNG")[0],imagesearch(image="new3.PNG")[1])
                                    break
                                else:
                                    break
                            else:
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    break
                                else:
                                    break
                    else:
                        webbrowser.open(url,new=0,autoraise=True)
                        sleep(15)
            else:
                os.system("cls")
                print(""""
                
                
                
                
                
                
                
                                      ONUR BUDAK YAPAY ZEKA ANONİM LİMİTED ŞİRKETİ
                
                
                
                
                
                
                
                """)
                sleep(1)
