from tkinter import *

root = Tk()
root.geometry('600x400')
root.title('Разовые команды')

def click_exit(event):
    root.destroy()

def click_send(event):
    receipt_0['fg'] = 'red'


receipt_0 = Label(text='первая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_0.place(x = 20, y = 20)

receipt_1 = Label(text='вторая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_1.place(x = 20, y = 60)

receipt_2 = Label(text='третья квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_2.place(x = 20, y = 100)

receipt_3 = Label(text='четвертая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_3.place(x = 20, y = 140)

receipt_4 = Label(text='пятая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_4.place(x = 20, y = 180)

receipt_5 = Label(text='шестая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_5.place(x = 20, y = 220)

receipt_6 = Label(text='седьмая квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_6.place(x = 20, y = 260)


bt_recv_kvit = Button(root,text='status request',width=10,height=1,bg='gray',fg='black',font='arial 12')
bt_recv_kvit.place(x = 50, y = 350)
bt_recv_kvit.bind()

bt_send_cmd = Button(root,text='send command',width=10,height=1,bg='gray',fg='black',font='arial 12')
bt_send_cmd.place(x = 300, y = 350)
bt_send_cmd.bind('<Button-1>',click_send)

bt_exit = Button(root,text='Exit',width=3,height=1,bg='gray',fg='black',font='arial 12')
bt_exit.place(x = 530, y = 350)
bt_exit.bind('<Button-1>',click_exit)

cmd_1 = Checkbutton(root,text=u'Первая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_1.place(x = 300, y = 20)

cmd_2 = Checkbutton(root,text=u'Вторая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_2.place(x = 300, y = 60)

cmd_3 = Checkbutton(root,text=u'Третья команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_3.place(x = 300, y = 100)

cmd_4 = Checkbutton(root,text=u'Четвертая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_4.place(x = 300, y = 140)

cmd_5 = Checkbutton(root,text=u'Пятая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_5.place(x = 300, y = 180)

cmd_6 = Checkbutton(root,text=u'Шестая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_6.place(x = 300, y = 220)

cmd_7 = Checkbutton(root,text=u'Седьмая команда',variable=1,onvalue=1,offvalue=0,font='arial 12')
cmd_7.place(x = 300, y = 260)


root.mainloop()

