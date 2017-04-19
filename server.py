from tkinter import *
import socket, sys

window = Tk()
window.title("Hostsend")
hosts = [] # hosts will be an array of just the host ips
hostnames = [] # an array of hostnames to load into the option menu


message = StringVar()
host = StringVar()
port = 4444
hostip = str()

def sendto(*args):
    message = messageE.get()
    port = int(portE.get())
    print("sending " + message + " to " + hostip + " on port " + str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostip, port))
    s.send(message.encode())
    s.close()

def reloadhosts(*args):
    try:
        hostfile = open('hosts.txt', 'r')
    except IOError:
        print("!! no host file found !!")
        sys.exit()
    print("# loading hosts...")
    state = True
    for i in hostfile:
        i = i.rstrip()
        print(i)
        if(state):
            hostnames.append(i)
            state = False
        else:
            hosts.append(i)
            state = True
    print("done, printing arrays")
    print(hostnames)
    print(hosts)
    print('---------------------------------')

def loadhost(*args):
    print("changed host to " + host.get())
    for i in range(0,len(hosts)):
        if (host.get() == hostnames[i]):
            hostip = hosts[i]
    print("ip is " + hostip)

reloadhosts()

sl = Label(window, text="Message")
sl.grid(row=0, column=0, sticky=E, padx=4)

hs = Label(window, text="Host")
hs.grid(row=1, column=0, sticky=E, padx=4)

pl = Label(window, text="Port")
pl.grid(row=1, column=2, sticky=W, padx=4)

messageE = Entry(window, width=32)
messageE.grid(row=0, column=1)

portE = Entry(window, width=8)
portE.grid(row=1, column=1, sticky=E)

hostselect = OptionMenu(window, host, *hostnames, command=loadhost)
hostselect.config(width=12)
hostselect.grid(row=1, column=1, sticky=W)

sendbutton = Button(window, text="Send", command=sendto)
sendbutton.grid(row=2, column=1, sticky=E)

window.bind('<Return>', sendto)

mainloop()
