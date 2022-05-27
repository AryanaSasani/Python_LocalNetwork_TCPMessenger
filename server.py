from source_server import *


FunctionalMod=int(input("1- Just Client   2 -> Just server  3- Client And Server   4-exit"))
## -----------Get Target Address--------------
serverName='localhost'   #target host Ip 
#serverName='localhost'
serverPort = 1200        #Port number
UserName="username"
UserName=gethostname()
## ----------###################--------------

##------ start  TCP server-------------
serverSocket = socket(AF_INET,SOCK_STREAM)
init_Server(serverSocket,serverPort)   
## ---------###############--------------

##------ connect to server ( TCP connection)-------------
clientSocket = socket(AF_INET,SOCK_STREAM)
##-------------------------------------------------


if(FunctionalMod==1 or FunctionalMod==3):
    rprint("[bold blue]Enter Target [u][bold cyan]HostIp[/bold cyan][/u] [/bold blue] >>")
    serverName=input("\t")   #target host Ip 

t1 = threading.Thread(target=connectThread, args=(clientSocket,serverName,serverPort,UserName,))
t2 = threading.Thread(target=ListinThread, args=(serverSocket,))


if(FunctionalMod==1):
    t1.start()
elif(FunctionalMod==2):
    t2.start()
elif(FunctionalMod==3):
    t2.start()
    time.sleep(5)
    t1.start()
else:
     print("end---------")
     quit()

while True:
    if(FunctionalMod==4):
        print("end--------")
        quit()
       
    if(FunctionalMod==1 or FunctionalMod==3):
        t1.join()
        rprint("[yellow]end of comunication with target server[/yellow]")
        FunctionalMod=int(input("1- Just Client   2 -> Just server  3- Client And Server 4-exit"))
        if(FunctionalMod==1 or FunctionalMod==3):
            rprint("[bold blue]Enter Target [u][bold cyan]HostIp[/bold cyan][/u] [/bold blue] >>")
            serverName=input("\t")   #target host Ip 
            t1 = threading.Thread(target=connectThread, args=(clientSocket,serverName,serverPort,UserName,))
            t1.start()
        
    