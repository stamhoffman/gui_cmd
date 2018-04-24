import socket
from tkinter import *

HOST_IP = "193.1.1.1"
HOST_PORT = 1111

CLIENT_IP = "193.1.1.61"
CLIENT_PORT = 2222    

root = Tk()
root.geometry('600x750')
root.title('Разовые команды')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST_IP, HOST_PORT))


def click_exit(event):
    root.destroy()

def recv_kvit(event):
    socket_udp()

def click_send(event):

    byte_0 = 0
    byte_1 = 0
    byte_2 = 0
    byte_3 = 0

    remote_power_rls = bytearray([byte_0, byte_1, byte_2, byte_3])

    byte_0 = 0
    byte_1 = 0
    byte_2 = 0
    byte_3 = 0

    remote_power_rls = bytearray([byte_0, byte_1, byte_2, byte_3])

    sock.sendto(remote_power, (CLIENT_IP, CLIENT_PORT))
    print("Включить")



    if cmd_1 == 1:
        sock.sendto(remote_power, (CLIENT_IP, CLIENT_PORT))
        print("Включить питание")

    if cmd_1 == 0:
        sock.sendto(remote_power, (CLIENT_IP, CLIENT_PORT))
        print("Включить питание")

    
###########################################################################################
receipt_0 = Label(text='1 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_0.place(x = 20, y = 20)

receipt_1 = Label(text='2 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_1.place(x = 20, y = 60)

receipt_2 = Label(text='3 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_2.place(x = 20, y = 100)

receipt_3 = Label(text='4 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_3.place(x = 20, y = 140)

receipt_4 = Label(text='5 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_4.place(x = 20, y = 180)

receipt_5 = Label(text='6 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_5.place(x = 20, y = 220)

receipt_6 = Label(text='7 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_6.place(x = 20, y = 260)

receipt_7 = Label(text='8 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_7.place(x = 20, y = 300)

##############################################################################################

receipt_8 = Label(text='9 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_8.place(x = 20, y = 340)

receipt_9 = Label(text='10 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_9.place(x = 20, y = 380)

receipt_10 = Label(text='11 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_10.place(x = 20, y = 420)

receipt_11 = Label(text='12 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_11.place(x = 20, y = 460)

receipt_12 = Label(text='13 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_12.place(x = 20, y = 500)

receipt_13 = Label(text='14 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_13.place(x = 20, y = 540)

receipt_14 = Label(text='15 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_14.place(x = 20, y = 580)

receipt_15 = Label(text='16 квитанция',width=25,height=1,bg='gray',fg='black',font='arial 12')
receipt_15.place(x = 20, y = 620)
##############################################################################################


bt_recv_kvit = Button(root,text='status request',width=15,height=1,bg='gray',fg='black',font='arial 12')
bt_recv_kvit.place(x = 60, y = 700)
bt_recv_kvit.bind('<Button-1>',recv_kvit)

bt_send_cmd = Button(root,text='send command',width=15,height=1,bg='gray',fg='black',font='arial 12')
bt_send_cmd.place(x = 350, y = 700)
bt_send_cmd.bind('<Button-1>',click_send)

bt_exit = Button(root,text='Exit',width=3,height=1,bg='gray',fg='black',font='arial 12')
bt_exit.place(x = 530, y = 700)
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



def socket_udp():

    byte_0 = 0
    byte_1 = 0
    byte_2 = 0
    byte_3 = 0


    codogram = bytearray([byte_0, byte_1, byte_2, byte_3])
    sock.sendto(codogram, (CLIENT_IP, CLIENT_PORT))
 
    data = sock.recvfrom(1024)

    data_0_2_bit_0 = (data[0][2] >> 7)& 0b00000001
    data_0_2_bit_1 = (data[0][2] >> 6)& 0b00000001 
    data_0_2_bit_2 = (data[0][2] >> 5)& 0b00000001 
    data_0_2_bit_3 = (data[0][2] >> 4)& 0b00000001
    data_0_2_bit_4 = (data[0][2] >> 3)& 0b00000001
    data_0_2_bit_5 = (data[0][2] >> 2)& 0b00000001
    data_0_2_bit_6 = (data[0][2] >> 1)& 0b00000001
    data_0_2_bit_7 = (data[0][2]) & 0b00000001

    data_0_3_bit_0 = (data[0][3] >> 7)& 0b00000001
    data_0_3_bit_1 = (data[0][3] >> 6)& 0b00000001 
    data_0_3_bit_2 = (data[0][3] >> 5)& 0b00000001 
    data_0_3_bit_3 = (data[0][3] >> 4)& 0b00000001
    data_0_3_bit_4 = (data[0][3] >> 3)& 0b00000001
    data_0_3_bit_5 = (data[0][3] >> 2)& 0b00000001
    data_0_3_bit_6 = (data[0][3] >> 1)& 0b00000001
    data_0_3_bit_7 = (data[0][3]) & 0b00000001


    
###########################################################################

    if data_0_2_bit_0 == 0:
         receipt_0['fg'] = 'green'
         receipt_0['text'] = ''
    else:
         receipt_0['fg'] = 'red'
         receipt_0['text'] = ''
       
    if data_0_2_bit_1 == 0:
         receipt_1['fg'] = 'green'
         receipt_1['text'] = ''
    else:
         receipt_1['fg'] = 'red'
         receipt_1['text'] = ''
         
    if data_0_2_bit_2 == 0:
         receipt_2['fg'] = 'red'
         receipt_2['text'] = ''
    else:
         receipt_2['fg'] = 'green'
         receipt_2['text'] = ''

    if data_0_2_bit_3 == 1:
         receipt_3['fg'] = 'green'
         receipt_3['text'] = ''
    else:
         receipt_3['fg'] = 'red'
         receipt_3['text'] = ''

    if data_0_2_bit_4 == 1:
         receipt_4['fg'] = 'green'
         receipt_4['text'] = ''
    else:
         receipt_4['fg'] = 'red'
         receipt_4['text'] = ''

    if data_0_2_bit_5 == 1:
         receipt_5['fg'] = 'green'
         receipt_5['text'] = ''
    else:
         receipt_5['fg'] = 'red'
         receipt_5['text'] = ''


    if data_0_2_bit_6 == 1:
         receipt_6['fg'] = 'green'
         receipt_6['text'] = ''
    else:
         receipt_6['fg'] = 'red'
         receipt_6['text'] = ''


    if data_0_2_bit_7 == 0:
         receipt_7['fg'] = 'green'
         receipt_7['text'] = ''
    else:
         receipt_7['fg'] = 'red'
         receipt_7['text'] = ''

#######################################################################
    
    if data_0_3_bit_7 == 1:
         receipt_8['fg'] = 'green'
         receipt_8['text'] = ''
    else:
         receipt_8['fg'] = 'red'
         receipt_8['text'] = ''
       
    if data_0_3_bit_6 == 0:
         receipt_9['fg'] = 'green'
         receipt_9['text'] = ''
    else:
         receipt_9['fg'] = 'red'
         receipt_9['text'] = ''
         
    if data_0_3_bit_5 == 1:
         receipt_10['fg'] = 'green'
         receipt_10['text'] = ''
    else:
         receipt_10['fg'] = 'red'
         receipt_10['text'] = ''

    if data_0_3_bit_4 == 0:
         receipt_11['fg'] = 'green'
         receipt_11['text'] = ''
    else:
         receipt_11['fg'] = 'red'
         receipt_11['text'] = ''

    if data_0_3_bit_3 == 1:
         receipt_12['fg'] = 'green'
         receipt_12['text'] = ''
    else:
         receipt_12['fg'] = 'red'
         receipt_12['text'] = ''

    if data_0_3_bit_2 == 1:
         receipt_13['fg'] = 'red'
         receipt_13['text'] = ''
    else:
         receipt_13['fg'] = 'green'
         receipt_13['text'] = ''


    if data_0_3_bit_1 == 1:
         receipt_14['fg'] = 'green'
         receipt_14['text'] = ''
    else:
         receipt_14['fg'] = 'red'
         receipt_14['text'] = ''


    if data_0_3_bit_0 == 0:
         receipt_15['fg'] = 'green'
         receipt_15['text'] = ''
    else:
         receipt_15['fg'] = 'red'
         receipt_15['text'] = ''


root.mainloop()







    
