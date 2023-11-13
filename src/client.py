import os
import socket
import threading
import sys
import cmd
from threading import Lock      # Mutex lock

from app_utils import *

class Client:
    def __init__(self, server_address, username, file_repository):
        self.server_address = server_address
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.file_repository = file_repository

        try:
            self.client_socket.connect(self.server_address)
            print(f"Connected to the server at {self.server_address}")
            self.connected = True
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            self.client_socket.close()

    def publish(self, lname, fname):

        self.file_repository.add_local_file(lname, fname)
        command = f"publish {lname} {fname}"
        self.send_command(command)

    def fetch(self, fname):
        command = f"fetch {fname}"
        self.send_command(command)

    def send_command(self, command):
        try:
            self.client_socket.send(command.encode())
            # Handle server response here
        except Exception as e:
            print(f"Error sending command to the server: {e}")

    def start(self):
        try:
            while True:
                user_input = input("Enter command: ")
                if user_input.lower() == "exit":
                    break
                elif user_input.startswith("publish"):
                    _, lname, fname = user_input.split()
                    self.publish(lname, fname)
                elif user_input.startswith("fetch"):
                    _, fname = user_input.split()
                    self.fetch(fname)
                else:
                    print("Invalid command. Please enter 'publish' or 'fetch'")
        finally:
            self.client_socket.close()

def main():
    server_address = ("127.0.0.1",2000)
    username = input("Enter your username: ")
    file_repository = ClientFileRepository()
    client = Client(server_address, username, file_repository)

    if client.connected:
        client_thread = threading.Thread(target=client.start)
        client_thread.start()

if __name__=="__main__":
    main()