import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from mutagen.mp3 import MP3
from PIL import Image,ImageTk
import pygame
import os.path
import glob
def music():

    pygame.init()
    pygame.mixer.init()
    def play_current_song(*args):
        """ 播放当前列表歌曲 """
        indexs = play_list.curselection()
        selectindex = int(indexs[0])
        pygame.mixer.music.load(file_list[selectindex])
        pygame.mixer.music.play()
    def play():
        pygame.mixer.music.unpause()
    def pause():
        pygame.mixer.music.pause()

    window = tk.Tk()
    window.title("播放音乐")
    window.geometry("300x500")
    #导入本地歌曲
    realpath = os.path.realpath(__file__) #当前绝对路径
    dirname = os.path.dirname(realpath)
    extension = 'mp3'
    file_list = glob.glob('*.'+extension) #返回所有MP3文件
    #播放列表可视化
    play_list = tk.Listbox(window,width=30,height=20)
    for i in file_list:
        play_list.insert('end',i)

    play_list.bind("<<ListboxSelect>>",play_current_song)#点击列表,播放对应歌曲
    play_list.pack()

    play_button = tk.Button(window, text='▶', font=('Arial', 10), width=2, height=1,command = play)#播放按钮
    play_button.place(x=150,y=380)
    pause_button = tk.Button(window, text='⏸', font=('Arial', 10), width=2, height=1,command = pause)#暂停按钮
    pause_button.place(x=100,y=380)
