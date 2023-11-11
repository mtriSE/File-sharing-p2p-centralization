import os
import socket
import threading
import sys
import cmd
from threading import Lock      # Mutex lock

class Server(cmd.Cmd):
    intro = "Server started, waiting for command"
    prompt = "Server> "
    
    def __init__(self,**kwargs):
        super(Server,self).__init__(**kwargs)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        
    def start(self):
        # Starts the server's main loop for accepting client connections.
        pass
    
    def handle_client(self, client_socket, client_address):
        # Handles communication with an individual client.
        pass
    
    def discover(self, client, hostname):
        # Responds to a discover command for a specific client.
        pass
    
    def ping(self,client,hostname):
        # Responds to a ping command for a specific client.
        pass
    
    def close(self):
        pass
        
    def do_ping(self, line):
        """
        ping <hostname>: live check the host named <hostname>
        """
        pass
    
    def do_discover(self,line):
        """
        discover <hostname>: discover the list of local files of the host named <hostname>
        """
        pass
    
    def do_EOF(self,line):
        """
        Type Ctrl + Z to exit
        """
        return True
    
def main():
    server = Server().cmdloop()

if __name__=="__main__":    
    main()