"""
Module provide helper function 
"""

class FileSharingProtocol:
    def serialize(self,data):
        """
        Converts data into a format suitable for transmission.
        """
        
    def deserialize(self,data):
        """
        Converts received data back into its original format.
        """
        pass
    def publish_request(self,lname,fname):
        """
        Generates the protocol message for a publish request.
        """
        pass
    def fetch_request(self,fname):
        """
        Generates the protocol message for a fetch request.
        """
        pass
    def discover_request(self,hostname):
        """
        Generates the protocol message for a discover request.
        """
        pass
    def ping_request(self,hostname):
        """
        Generates the protocol message for a ping request.
        """
        pass

class FileRepository:
    __client_files = dict()
    # {"username": list of files}
    
    def add_file(self, client, file):
        """
        Adds a file to the repository for a specific client.
        """
        
        self.__client_files[client].append(file)
        return True
        
    def get_files(self, client):
        """
        Retrieves the list of files for a specific client.
        """
        
    def get_all_files(self):
        """
        Retrieves the list of all files across all clients.
        """
        pass

class ClientFileRepository:
    def add_local_file(self):
        """
        Adds a local file to the client's repository.
        """
        pass
    def get_local_files(self):
        """
        Retrieves the list of local files on the client.
        """
        pass
    def get_file_path(self):
        """
        Retrieves the file path for a given file name.
        """
        pass