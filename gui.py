from tkinter import *
#import add_peer_interface
#import add_server_interface
#import authorize_peer_on_server
#import deauthorize_peer_on_server

window = Tk()
window.title("WireGuard-Helpers")
window.geometry("480x768")

class tkinter_label():
    def __init__(self,master,width,height,text,row,column,rowspan,columnspan):
        self.master = master
        self.width = width
        self.height = height
        self.text = str(text)
        self.row = row
        self.column = column
        self.rowspan = rowspan
        self.columnspan = columnspan

        label = Label(master=master,width=width,height=height,text=text)
        label.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)

class tkinter_button():
    def __init__(self,master,width,height,text,command,row,column):
        self.master = master
        self.width = width
        self.height = height
        self.text = text
        self.command = command
        self.row = row
        self.column = column

        button = Button(master=master,width=width,height=height,text=text,command=command)
        button.grid(row=row,column=column)

tunnel_name = StringVar()
tunnel_name_label = tkinter_label(window,37,1,"Tunnelinterface-Name",0,0,1,1)
tunnel_name_entry = Entry(master=window,width=20,textvariable=tunnel_name)
tunnel_name_entry.grid(row=1,column=0)

tunnel_ip = StringVar()
tunnel_ip_label = tkinter_label(window,27,1,"Tunnelinterface-IP-Adresse",2,0,1,1)
tunnel_ip_entry = Entry(master=window,width=20,textvariable=tunnel_ip)
tunnel_ip_entry.grid(row=3,column=0)

tunnel_subnetmask = StringVar()
tunnel_subnetmask_label = tkinter_label(window,30,1,"Tunnelinterface-IP-Subnetzmaske",4,0,1,1)
tunnel_subnetmask_entry = Entry(master=window,width=20,textvariable=tunnel_subnetmask)
tunnel_subnetmask_entry.grid(row=5,column=0)

tunnel_port = StringVar()
tunnel_port_label = tkinter_label(window,27,1,"Tunnelinterface-Port",6,0,1,1)
tunnel_port_entry = Entry(master=window,width=20,textvariable=tunnel_port)
tunnel_port_entry.grid(row=7,column=0)

tunnel_config_path = StringVar()
tunnel_config_path = tkinter_label(window,35,1,"Speicherort der Konfigurationsdatei",8,0,1,1)
tunnel_config_path = Entry(master=window,width=20,textvariable=tunnel_config_path)
tunnel_config_path.grid(row=9,column=0)

routed_ip_range = StringVar()
routed_ip_range = tkinter_label(window,37,1,"Gerouteter IP-Bereich",0,1,1,1)
routed_ip_range = Entry(master=window,width=20,textvariable=routed_ip_range)
routed_ip_range.grid(row=1,column=1)

routed_ip_subnet = StringVar()
routed_ip_subnet_label = tkinter_label(window,27,1,"Geroutetes Subnetz",2,1,1,1)
routed_ip_subnet_entry = Entry(master=window,width=20,textvariable=routed_ip_subnet)
routed_ip_subnet_entry.grid(row=3,column=1)

peer_ip = StringVar()
peer_ip_label = tkinter_label(window,30,1,"Peer-IP-Adresse",4,1,1,1)
peer_ip_entry = Entry(master=window,width=20,textvariable=peer_ip)
peer_ip_entry.grid(row=5,column=1)

peer_port = StringVar()
peer_port_label = tkinter_label(window,27,1,"Tunnelinterface-Port",6,1,1,1)
peer_port_entry = Entry(master=window,width=20,textvariable=peer_port)
peer_port_entry.grid(row=7,column=1)

tunnel_config_path = StringVar()
tunnel_config_path = tkinter_label(window,35,1,"Speicherort der Konfigurationsdatei",8,0,1,1)
tunnel_config_path = Entry(master=window,width=20,textvariable=tunnel_config_path)
tunnel_config_path.grid(row=9,column=0)






peer_publickey = StringVar()
peer_publickey_label = tkinter_label(window,60,1,"           Public Key des Peers",10,0,1,2)
peer_publickey_entry = Entry(master=window,width=60,textvariable=peer_publickey)
peer_publickey_entry.grid(row=11,column=0,rowspan=1,columnspan=2)

def debug_labelprint():
    label1 = ""
    label2 = ""
    label3 = ""
    label1 = tkinter_label(window,40,1,"Tunnelinterface-IP-Adresse: " + str(tunnel_ip_entry.get()),15,0,1,1)
    label2 = tkinter_label(window, 28, 1, "Tunnelinterface-Name: " + str(tunnel_name_entry.get()),13,0,1,1)
    label2 = tkinter_label(window, 60, 1, "Peer-Public-Key: " + str(peer_publickey_entry.get()),14,0,1,1)

debug_button = tkinter_button(window,7,1,"Debug!",lambda:debug_labelprint(),16,0)

window.mainloop()
