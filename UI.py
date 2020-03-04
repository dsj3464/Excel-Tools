#coding=gbk
import tkinter as tk
import xlwings as xw
from tkinter import filedialog
import threading
import Main
import time
from PIL import Image

from PIL import ImageTk
def select_main_table():
    global main_tabel_file
    main_tabel_file = filedialog.askopenfilename(filetypes=[('excel file(.*xlsx)','.xlsx')]) #���ѡ��õ��ļ�
    main_tabel_file = main_tabel_file.replace('/','\\')
    L1.config(text='�����ǣ�'+main_tabel_file)
    button1['text'] = '����ѡ������'
    return main_tabel_file

def select_sub_table():
    global  sub_table_file_list
    sub_table_file_list = filedialog.askopenfilenames(filetypes=[('excel file (.*xlsx)','.xlsx')])
    namelist = []
    str = ''
    for name in sub_table_file_list:
        name = name.replace('/','\\')
        namelist.append(name)
        str = str + name + '\n'
    sub_table_file_list = namelist
    #���ԭ��������
    t.delete('1.0','end')
    t.insert('insert','�ӱ�: \n' + str)
    t.update()
    t['height'] = min(len(sub_table_file_list)+1,15)
    button2['text'] = '����ѡ���ӱ�'
    return namelist
def call_main_begin():
    global main_tabel_file , sub_table_file_list  ,window
    button3.pack_forget()
    label2 = tk.Label(window, text='���ںϲ�')
    label2.pack()
    Main.begin(main_tabel_file,sub_table_file_list)
    label2.config(text='�ϲ����')
    button3.pack()
def begin():
    thread1 = threading.Thread(target=call_main_begin)
    thread1.start()

        #��ʼ�����ڴ�С
window = tk.Tk()
window.title('this is a window')
window.geometry('700x700')

main_tabel_file = ''
sub_table_file_list = []
        #ѡ������İ�ť�Լ���ǩ


L1 = tk.Label(window,text='��ѡ������',font=('Arial',14))
L1.pack()
button1 = tk.Button(window,text='ѡ������',command = select_main_table,bg='#F0FFFF')
button1.pack()

        #ѡ���ӱ�İ�ť���ı�
t = tk.Text(window,height = 5,font=('Arial',14))
t.insert('insert','�ӱ�:\n')
t.pack()
button2 = tk.Button(window,text='ѡ���ӱ�',command=select_sub_table,bg='#F0FFFF')
button2.pack()

button3 = tk.Button(window,text='��ʼ�ϲ�',command = begin)
button3.pack()


window.mainloop()