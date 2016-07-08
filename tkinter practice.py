#-*- encoding=UTF-8 -*-
__author__ = 'Bob'

from tkinter import *
import xml.sax
import xml.dom.minidom
from xml.etree import ElementTree as ET

root = Tk()
root.geometry('400x200')
root.title('Connectivity')

def hello():
    print ("hello")
    
def about():
    w = Label(root, test="Develop list:\nBob Yao\nbob.yao@db.com")
    w.pack(side=TOP)

class Edit_XML_file():
    def __init__(self, path):
        with open(path, 'rt') as f:
            self.tree = ElementTree.parse(f)  #class内部的全局变量以self.开头 
                        
    def read_xml(self, in_path):
        '''''读取并解析XML文件
            in_path: xml路径
            return: ElementTree'''
        self.tree.parse(in_path)
            
    def write_xml(self,out_path):
        '''''将xml文件写出
            tree:xml树
            out_path: 写出路径'''
        self.tree.write(out_path, encoding="utf-8" , xml_declaration=True)
            
    def find_the_node(self, path):
        '''''查找某个路径匹配的第一个节点
            tree: xml树
            path: 节点路径'''
        return self.tree.find(path)
        
    def read_the_node(self, nodelist):
        '''''读取某个节点的文本属性
            nodelist:节点名称'''
        return nodelist.text
        
    def change_node_text(self, nodelist, text):
        '''''更改节点的文本
            nodelist: 节点
            text:文本内容'''
        nodelist.text = text
        


def configWindow():
    top = Toplevel()
    top.title("Usr&pwd config window")
    top.geometry('200x200')
    
    #路径设定
    xml_file_path = 'C:/Users/Bob.Yao/Python/config.xml'
    
    #创建一个对象
    control_xml = Edit_XML_file(xml_file_path)
    
    #找到节点
    account_node = control_xml.find_the_node("./account/text")
    pwd_node = control_xml.find_the_node("./pwd/text")
        
    username = Label(top, text="username : ")
    username.grid(row=0, column=0)
    password = Label(top, text="password : ")
    password.grid(row=1, column=0)
    
    username_box_value=StringVar()
    username_box = Entry(top, textvariable=username_box_value, state=DISABLED)
    username_box.grid(row=0, column=1)
    #读取XML用户名节点文本
    username_box_value.set(control_xml.read_the_node(account_node))
    
    password_box_value=StringVar()
    password_box = Entry(top, textvariable=password_box_value , state=DISABLED)
    password_box.grid(row=1, column=1)
    #读取XML密码节点文本
    password_box_value.set(control_xml.read_the_node(pwd_node))
    
    #修改并且当前界面上的用户名密码
    def edit_config_account_config_pwd():
        edit_account_value = username_box.get()
        print (edit_account_value)
        edit_pwd_value = password_box.get()
        print (edit_pwd_value)
        
        #更改节点文本
        control_xml.change_node_text(account_node, edit_account_value)
        control_xml.change_node_text(pwd_node, edit_pwd_value)
        
        #将xml文件写出
        control_xml.write_xml(xml_file_path)
     
    #修改用户名密码输入框的编辑状态    
    def enable_config_account_config_pwd():
        username_box = Entry(top, textvariable=username_box_value, state=NORMAL)
        username_box.grid(row=0, column=1)
        password_box = Entry(top, textvariable=password_box_value , state=NORMAL)
        password_box.grid(row=1, column=1)
    
    edit_button = Button(top, text='Edit', command=enable_config_account_config_pwd)
    edit_button.grid(row=2, column=0)
    save_button = Button(top, text='Save', command=edit_config_account_config_pwd)
    save_button.grid(row=2, column=1, sticky=W)
    cancel_button = Button(top, text='Cancel', command=top.quit)
    cancel_button.grid(row=2, column=1, sticky=E)

    
menubar = Menu(root)

#create menu File
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#create menu Config
configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="User config", command=configWindow)
menubar.add_cascade(label="Config", menu=configmenu)

#create menu Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

#display menu
root.config(menu=menubar)

#define a insert function
def insert_command():
    print ("text")

#create a control button
btnSer = Button(root, text="Connect", fg="red", command=insert_command, width=7, height=1)
btnSer.pack(side='left')

#create console window
console = Text(root)
console.insert(1.0, 'hello welcome to new console world!\n')
console.insert(2.0, 'please input your orderID:\n')
console.focus_force()
console.pack()

def print_content():
    input = console.get("end-2l", "end-2c")
    print ("the record has been stored as :'%s'" %input)

#triggle by RETURN button
root.bind('<Return>', lambda event: print_content())

#Create a scroll bar
scroll = Scrollbar(root)
scroll.pack(side='right', fill='y')

scroll.config(command=console.yview)
console.config(yscrollcommand=scroll.set)

mainloop()