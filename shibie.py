import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import cv2 as cv
import time
from threading import Thread  # 创建线程的模块

from PIL import ImageTk

root = tk.Tk()
botton1_flag = False
botton2_flag = False
botton3_flag = False
shibie_flag = False

### 功能逻辑部分 ###

def button1_press():
    global botton1_flag
    botton1_flag = True


def button2_press():
    t = Thread(target=ui_used, name='ui')
    t.start()
    t1 = Thread(target=shibie, name='renlian')
    t1.start()


def button3_press():
    global botton3_flag
    botton3_flag = True


### 界面设计部分 ###

root.geometry("1268x539")
root.title("pingyu")
button1_frame = ttk.Frame(width=74, height=41)
button1 = ttk.Button(button1_frame, text="截图", command=button1_press)
button1.place(x=0, y=0, width=74, height=41)
button1_frame.place(x=581, y=168)
pic1_frame = ttk.Frame(width=552, height=394)
pic1 = ttk.Label(pic1_frame, justify="left")
pic1.place(x=0, y=0, width=552, height=394)
pic1_frame.place(x=6, y=15)
pic2_frame = ttk.Frame(width=552, height=394)
pic2 = ttk.Label(pic2_frame, justify="left")
pic2.place(x=0, y=0, width=552, height=394)
pic2_frame.place(x=677, y=14)
button2_frame = ttk.Frame(width=74, height=41)
button2 = ttk.Button(button2_frame, text="打开摄像头", command=button2_press)
button2.place(x=0, y=0, width=74, height=41)
button2_frame.place(x=581, y=77)
button3_frame = ttk.Frame(width=70, height=45)
button3 = ttk.Button(button3_frame, text="识别", command=button3_press)
button3.place(x=0, y=0, width=70, height=45)
button3_frame.place(x=584, y=253)


### 功能逻辑部分 ###
def ui_used():
    global botton1_flag
    global botton3_flag
    global pic1
    global shibie_flag
    capture = cv.VideoCapture(0)
    while True:
        # root.mainloop()
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # 镜像操作
        #cv.imshow("video", frame)
        cv.imwrite("xianshi.jpg", frame)
        photo = ImageTk.PhotoImage(file="xianshi.jpg")
        pic1.configure(image=photo)

        key = cv.waitKey(50)
        # print(key)
        if key == ord('q'):  # 判断是哪一个键按下
            break
        if botton1_flag:
            cv.imwrite("jietu.jpg", frame)
            botton1_flag = False
        if botton3_flag:
            cv.imwrite("shibie.jpg", frame)
            botton3_flag = False
            shibie_flag = True
    cv.destroyAllWindows()

def shibie():
    global pic2
    global shibie_flag

    faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    while True:
        if shibie_flag:
            img = cv.imread('shibie.jpg')
            imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            face1 = faceCascade.detectMultiScale(imgGray, 1.1, 4)
            for (x, y, w, h) in face1:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #cv.imshow("Result1", img)
            cv.imwrite("shibie.jpg", img)

            photo = ImageTk.PhotoImage(file="shibie.jpg")
            pic2.configure(image=photo)
            shibie_flag = False
        key = cv.waitKey(50)
        if key == ord('q'):  # 判断是哪一个键按下
            break
    cv.destroyAllWindows()



root.mainloop()
