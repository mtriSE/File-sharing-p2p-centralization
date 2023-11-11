import os
import socket
import threading
import sys
import cmd

LOCK = threading.Lock()     


class Server(cmd.Cmd):
    intro = "Server started, waiting for command"
    prompt = "Server> "
    
    def __init__(self,hostname, port,**kwargs):
        super(Server,self).__init__(**kwargs)
        self.__HOSTNAME = hostname
        self.__PORT = port
        
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clients = dict()
        # Each element format: {"username" : tuple(socket, list of files<[]>) }
        
    
    def __handle_client(self, connection, client_address):
        """
        A thread that handles communication with an individual client.
        """
        try:
            # Blocking call: wait for user input their username
            username = connection.recv(1024).decode()
            
            # Find user with username has been received above
            # user: list
            user = self.__clients.get(username)

            if (user is None):
                # Accept user, because username isnt existed in __clients => update list of clients
                self.__clients.update({username:(connection,[])})
                connection.sendall("200 OK".encode())   
            else:
                # username is duplicate => refused
                
                connection.close()
                return False
                
            while True: 
                msg = connection.recv(1024).decode()
                if not msg:
                    break
                command = msg.split()[0]
                
                # publish lname fname
                if command == "publish":  
                    lname = msg.split()[1]
                    fname = msg.split()[2]
                    self.handlePublish(connection, addr, lname, fname)

                # fetch fname
                elif command == "fetch":
                    fname = msg.split()[1]
                    self.handleFetchReq(connection,addr,fname)
                else: 
                    connection.sendall("400 Bad Command".encode())
                    
            # End connection => remove user's record
            print(username,"has been disconnected")
            return True

        except Exception as e:
            print(e.strerror)
            self.__close()
    
    
    def __start(self):
        """
        A thread to handle server
        """
        self.__server_socket.bind((self.__HOSTNAME,self.__PORT))
        self.__server_socket.listen()    
        while True:
            try:
                # Blocking here until there're a client connect
                connection, addr = self.__server_socket.accept()              

                # Create a thread for handling connection
                handleConnectionThread = threading.Thread(target=self.__handle_client, args=(connection,addr),daemon=True)  
                handleConnectionThread.start()  
                                                    
            except Exception as e: 
                print(e.strerror)


    
    def __discover(self, client, hostname):
        """ 
        Responds to a discover command for a specific client.
        """
        pass
    
    def __ping(self,client,hostname):
        """
        Responds to a ping command for a specific client.
        """
        pass
    
    def __close(self):
        pass
    
    def do_start(self, args):
        """
        start: Start server
        """
        # Starts the server's loop for accepting client connections.
        try: 
            threading.Thread(target=self.__start__,daemon=True).start()
        except Exception as e: 
            print(f"[Exception]: {e.strerror}")
   
        
    def do_ping(self, args):
        # args: hostname 
        """
        ping <hostname>: live check the host named <hostname>
        """
       
    
    def do_discover(self,args):
        # args: hostname
        """
        discover <hostname>: discover the list of local files of the host named <hostname>
        """
        pass
    
    def do_EOF(self,args):
        """
        Type Ctrl + Z to exit
        """
        self.__close()
        return True
    
def main():
    server = Server("127.0.0.1",2000)

    server.cmdloop()


if __name__=="__main__":    
    main()