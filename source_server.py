
from warnings import catch_warnings
from HeaderFiles import *


def progressBar_Delay():
    time.sleep(0.002)

def progressBar():
    for n in track(range(100), description="[cyan]Starting Server... "):
        progressBar_Delay()

def init_Server(mySocket,ServerPot):
    #creat socket and start server
    mySocket.bind(('',ServerPot))
    rprint("[bold yellow]start server [/bold yellow] >>")
    progressBar()


def ListinThread(serverSock):
    serverSock.listen(1)
    rprint("[bold magenta]Server is Ready to [red]service...[/red] [/bold magenta]!") 

    # while Section....
    while True:
        connectionSocket, addr = serverSock.accept()  #connect to new client
        RecMessage=connectionSocket.recv(1024).decode()
        while (RecMessage!="close" and len(RecMessage)>0):     #comunicate with client
            rprint("[magenta]Recived[/magenta]:, [bold blue]{}[/bold blue]!".format(RecMessage))
            RecMessage=connectionSocket.recv(1024).decode()
            if(RecMessage=='close'):
                connectionSocket.send("End..".encode()) 
                connectionSocket.close()
                break
                

def connectThread(clientSock,servName,servPort,UserName):
    try:
        clientSock.connect((servName,servPort))
        ## --------Send Message------------------
        message=input("")
        while True:
            
            clientSock.send(("[magenta]"+UserName+"[/magenta]: "+message).encode())
            if(message=='close'):
                break
            message=input("")
            
    
    except sock.error as er:
        print("connection error : %s"%er)
    ## ---------###############--------------
    time.sleep(0.05)
    clientSock.close()