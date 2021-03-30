#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from python_imagesearch.imagesearch import imagesearch
from pyautogui import leftClick
import pyautogui
from time import sleep
from PyQt5 import QtWidgets,QtGui
import random
import sys
import webbrowser
import datetime
kullanıcı_adı = pyautogui.prompt(text='Kullanıcı adınızı girin', title='NRB SECURİTY' , default='')
sifre = pyautogui.password(text='Şifrenizi giriniz.', title='NRB SECURİTY' , mask="*")
pyautogui.alert(text='Canlı ders moduna almadan önce tarayıcılarınızda neu uzem hesabınızdan çıkış yaptığınızdan emin olun !', title='NRB SECURİTY', button="Kontrol ettim")
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazı_alanı = QtWidgets.QLabel("Arhez1402")
        self.buton = QtWidgets.QPushButton("Çevre Eğitimi")
        self.buton2 = QtWidgets.QPushButton("Canlı ders modu")
        self.buton3 = QtWidgets.QPushButton("Aktif değil")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.buton2)
        v_box.addWidget(self.buton3)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click2)
        self.show()

    def click(self):
        def loading():
            if imagesearch("back.PNG")[0] > 0:
                leftClick(imagesearch(image="back.PNG")[0], imagesearch(image="back.PNG")[1])
                sleep(1)
                leftClick(imagesearch(image="cevre_egitimi.PNG")[0], imagesearch(image="cevre_egitimi.PNG")[1])
                sleep(3)
                leftClick(imagesearch(image="subat1.PNG")[0], imagesearch(image="subat1.PNG")[1])
                sleep(8)
                webbrowser.open("https://uzaktanegitim.erbakan.edu.tr/course/view.php?id=16350&section=2", new=2,autoraise=True)
                sleep(5)
                leftClick(imagesearch(image="start.PNG")[0], imagesearch(image="start.PNG")[1])
                sleep(2)
                leftClick(imagesearch(image="kayitlari_goster.PNG")[0],imagesearch(image="kayitlari_goster.PNG")[1])
                sleep(3)
                leftClick(1119, 412)
                pyautogui.press("space")
                sleep(2)
                leftClick(imagesearch(image="opss.PNG")[0],imagesearch(image="opss.PNG")[1]+23)
                sleep(10)
                leftClick(imagesearch(image="kaydi_oynat.PNG")[0],imagesearch(image="kaydi_oynat.PNG")[1])
                sleep(10)
                if imagesearch(image="close.PNG")[0] > 0:
                    leftClick(imagesearch(image="close.PNG")[0], imagesearch(image="close.PNG")[1])





            else:
                sleep(1)
                leftClick(imagesearch(image="cevre_egitimi.PNG")[0], imagesearch(image="cevre_egitimi.PNG")[1])
                sleep(3)
                leftClick(imagesearch(image="subat1.PNG")[0], imagesearch(image="subat1.PNG")[1])
                sleep(8)
                webbrowser.open("https://uzaktanegitim.erbakan.edu.tr/course/view.php?id=16350&section=2", new=2,autoraise=True)
                sleep(5)
                leftClick(imagesearch(image="start.PNG")[0], imagesearch(image="start.PNG")[1])
                sleep(2)
                leftClick(imagesearch(image="kayitlari_goster.PNG")[0],imagesearch(image="kayitlari_goster.PNG")[1])
                sleep(3)
                leftClick(1119, 412)
                pyautogui.press("space")
                sleep(2)
                leftClick(imagesearch(image="opss.PNG")[0], imagesearch(image="opss.PNG")[1]+23)
                sleep(15)
                leftClick(imagesearch(image="kaydi_oynat.PNG")[0], imagesearch(image="kaydi_oynat.PNG")[1])
                sleep(10)
                if imagesearch(image="close.PNG")[0]>0:
                    leftClick(imagesearch(image="close.PNG")[0],imagesearch(image="close.PNG")[1])



        #START

        webbrowser.open("https://uzaktanegitim.erbakan.edu.tr/my/",new=0,autoraise=True)
        sleep(15)
        if imagesearch(image="kullanici_adi.PNG",)[0]>0:
            leftClick(imagesearch(image="kullanici_adi.PNG")[0],imagesearch(image="kullanici_adi.PNG")[1])
            pyautogui.typewrite(kullanıcı_adı, interval=0.05)
            sleep(0.05)
            leftClick(imagesearch(image="sifre.PNG")[0],imagesearch(image="sifre.PNG")[1])
            pyautogui.typewrite(sifre,interval=0.05)
            sleep(0.05)
            leftClick(imagesearch(image="giris.PNG")[0],imagesearch(image="giris.PNG")[1])
            sleep(5)
            if imagesearch(image="hatali_giris.PNG")[0]>0:
                sleep(0.05)
                pyautogui.alert(text='Hatalı giriş!!!', title='NRB SECURİTY', button="Çıkış")
            else:
                loading()
                sleep(3600)
        else:
            loading()
            sleep(3600)
    def click2(self):
        messages=["Yarın yılın tembel bir kadına hitap eden tek günü","Bu kadar tembel olmak zorunda mısın ? :/","Ahahahah işlemcim bile senden daha çalışkan :D","Bu kadar tembel olmak zorunda mısın?","Anladık bilgisayar çağı ama az sende uğraş beeee :(","Tamamdır. Yarın senin yerine derse giriyorum :)","Hiç havamda değilim :/","O saaatte nasıl uyanacammm :')","Söz vermiyorum ama derse yetişmeye çalışacam."]
        sleep(2)
        ay = pyautogui.prompt(text="Ders yılın kaçıncı ayında ? (ör. Nisan=4)",title="NRB SECURİTY",default="")
        gün = pyautogui.prompt(text="Ders ayın kaçıncı gününde ? ",title="NRB SECURİTY",default="")
        saat = pyautogui.prompt(text="Ders saat kaçta ? (başında sıfır kullanmadan)",title="NRB SECURİTY",default="")
        dakika = pyautogui.prompt(text="Ders kaçıncı dakikada ? (başında sıfır kullanmadan",title="NRB SECURİTY",default="")
        sleep(2)
        pyautogui.alert(text=messages[random.randint(0, 9)], title='NRB SECURİTY', button="Tamam")
        while True:
            month = datetime.datetime.now()
            day = datetime.datetime.now()
            hour = datetime.datetime.now()
            minute = datetime.datetime.now()
            second = datetime.datetime.now()
            if month.month==int(ay) and day.day==int(gün) and hour.hour==int(saat) and minute.minute == int(dakika):
                webbrowser.open("https://uzaktanegitim.erbakan.edu.tr/my/", new=0, autoraise=True)
                sleep(15)
                if imagesearch(image="kullanici_adi.PNG", )[0] > 0:
                    leftClick(imagesearch(image="kullanici_adi.PNG")[0], imagesearch(image="kullanici_adi.PNG")[1])
                    pyautogui.typewrite(kullanıcı_adı, interval=0.05)
                    sleep(0.05)
                    leftClick(imagesearch(image="sifre.PNG")[0], imagesearch(image="sifre.PNG")[1])
                    pyautogui.typewrite(sifre, interval=0.05)
                    sleep(0.05)
                    leftClick(imagesearch(image="giris.PNG")[0], imagesearch(image="giris.PNG")[1])
                    sleep(5)
                    if imagesearch(image="hatali_giris.PNG")[0] > 0:
                        sleep(0.05)
                        pyautogui.alert(text='Hatalı giriş!!!', title='NRB SECURİTY', button="Çıkış")
                    else:
                        webbrowser.open("https://uzaktanegitim.erbakan.edu.tr/mod/adobeconnect/view.php?id=292231",new=2,autoraise=True)
                        sleep(5)
                        leftClick(imagesearch(image="toplantiya_katil.PNG")[0],imagesearch(image="toplantiya_katil.PNG")[1])
                        sleep(20)
                        if imagesearch(image="new1.PNG")[0] > 0:
                            leftClick(imagesearch(image="new1.PNG")[0], imagesearch(image="new1.PNG")[1])
                            sleep(2)
                            if imagesearch(image="new2.PNG")[0] > 0:
                                leftClick(imagesearch(image="new2.PNG")[0], imagesearch(image="new2.PNG")[1])
                                sleep(2)
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    sleep(2)
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    sleep(2)
                                    pyautogui.press("f11")
                                    while True:
                                        try:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                                        except:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                            else:
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    sleep(2)
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    sleep(2)
                                    pyautogui.press("f11")
                                    while True:
                                        try:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                                        except:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                        else:
                            if imagesearch(image="new2.PNG")[0] > 0:
                                leftClick(imagesearch(image="new2.PNG")[0], imagesearch(image="new2.PNG")[1])
                                sleep(2)
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    sleep(2)
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    sleep(2)
                                    pyautogui.press("f11")
                                    while True:
                                        try:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                                        except:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                            else:
                                if imagesearch(image="new3.PNG")[0] > 0:
                                    sleep(2)
                                    leftClick(imagesearch(image="new3.PNG")[0], imagesearch(image="new3.PNG")[1])
                                    sleep(2)
                                    pyautogui.press("f11")
                                    while True:
                                        try:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
                                        except:
                                            if imagesearch(image="merhaba_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya"))
                                                sleep(1)
                                                pyautogui.typewrite("Merhaba hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="evet_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("Evet hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            elif imagesearch(image="tamamdır_hocam.PNG")[0] > 0:
                                                sleep(2)
                                                leftClick(imagesearch(image="buraya_yazin.PNG")[0],imagesearch(image="buraya_yazin.PNG")[1])
                                                sleep(1)
                                                pyautogui.typewrite("tamamdır hocam", interval=0.05)
                                                sleep(0.05)
                                                pyautogui.press("enter")
                                                sleep(600)
                                            else:
                                                sleep(300)
            else:
                print("{}:{}:{}".format(hour.hour,minute.minute,second.second))
                sleep(1)

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
