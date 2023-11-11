# File-sharing-p2p-centralization

## Define function:
### 1. Function: Client Registers Local Files with the Server

**Communication Protocol:**
- **Request Format:** `publish lname fname`
- **Server Response Format:** `ACK` or `ERROR`

**Description:**
- The client initiates a connection with the server and sends a `publish` command along with the local file's name (`lname`) and the desired file name (`fname`) on the server.
- The server acknowledges the successful registration with an `ACK` response or sends an `ERROR` message if there are issues (e.g., file not found).

### 2. Function: Client Requests a File from Another Client

**Communication Protocol:**
- **Request Format:** `fetch fname`
- **Server Response Format:** `LIST [client1, client2, ...]` or `NOT FOUND`

**Description:**
- The client sends a `fetch` command to the server, requesting a file with the given file name (`fname`).
- The server responds with a list of clients (`client1`, `client2`, ...) that have the requested file. If the file is not available, it sends an `NOT FOUND` message.

### 3. Function: Client Downloads a File from Another Client

**Communication Protocol:**
- Direct communication between clients (e.g., peer-to-peer protocols such as TCP or UDP)

**Description:**
- The client, having received the list of potential sources from the server, establishes a direct connection (potentially using TCP or UDP) with the selected source client.
- The client requests and downloads the file directly from the source client **without requiring further server intervention.**

### 4. Function: Server Discovers Local Files of a Specific Client

**Communication Protocol:**
- **Request Format:** `discover hostname`
- **Server Response Format:** `LIST [file1, file2, ...]` or `ERROR`

**Description:**
- The server receives a `discover` command with a specific client's hostname (`hostname`).
- The server was responded with a list of files (`file1`, `file2`, ...) that belong to the specified client. If the client is not found or not reachable, it sends an `ERROR` message.

### 5. Function: Server Pings a Specific Client

**Communication Protocol:**
- **Request Format:** `ping hostname`
- **Server Response Format:** `SUCCESS` or `FAILURE`

**Description:**
- The server receives a `ping` command with a specific client's hostname (`hostname`).
- The server attempts to ping the specified client and responds with `SUCCESS` if the client is reachable or `FAILURE` if it is not responsive.

## Class used:
### 1. **Client Class:**

   - **Attributes:**
     - `server_address`: The address of the server.
     - `client_socket`: The client's socket for communication.
     - `username`: A unique identifier for the client.

   - **Methods:**
     - `__init__(self, server_address)`: Initializes the client with the server address and establishes a connection.
     - `publish(self, lname, fname)`: Sends a publish command to the server.
     - `fetch(self, fname)`: Sends a fetch command to the server.
     - `start(self)`: Starts the client's main loop for user interaction and command processing.
     - `close(self)`: Closes the client's socket and cleans up resources.

### 2. **Server Class:**

   - **Attributes:**
     - `__HOSTNAME`: server's hostname or ip
     - `__PORT`: server's port for waiting connection from clients
     - `__server_socket`: The server's socket for accepting client connections.
     - `__clients`: A dictionary to keep track of connected clients.
     - `__file_repository`: An instance of the `FileRepository` class to manage file information.

   - **Methods:**
     - `__init__(self, server_address)`: Initializes the server with the server address and sets up the server socket.
     - `__start(self)`: Starts the server's main loop for accepting client connections.
     - `__handle_client(self, connection, client_address)`: A thread that handles communication with an individual client.
     - `__discover(self, client, hostname)`: Resquest a discover command to a specific client.
     - `__ping(self, client, hostname)`: Request a ping command to a specific client.
     - `__close(self)`:Close the server, called when user use keysrtoke `Ctrl + Z`.
     - `do_start(self, args)`: Start server. *override from base class cmd.Cmd()*
     - `do_ping(self, args)`: ping ***hostname*** (args): live check the host named ***hostname*** (args). *override from base class cmd.Cmd()*
     - `do_discover(self,args)`: discover ***hostname*** (args): discover the list of local files of the host named ***hostname*** (args). *override from base class cmd.Cmd()*
     - `do_EOF(self,args)`: Provide user keystroke: `Ctrl + Z` to exit. *override from base class cmd.Cmd()*
    

### 3. **FileSharingProtocol Class:**

   - **Attributes:**
     - None (mainly a utility class for defining protocols).

   - **Methods:**
     - `serialize(self, data)`: Converts data into a format suitable for transmission.
     - `deserialize(self, data)`: Converts received data back into its original format.
     - `publish_request(self, lname, fname)`: Generates the protocol message for a publish request.
     - `fetch_request(self, fname)`: Generates the protocol message for a fetch request.
     - `discover_request(self, hostname)`: Generates the protocol message for a discover request.
     - `ping_request(self, hostname)`: Generates the protocol message for a ping request.

### 4. **FileRepository Class:**

   - **Attributes:**
     - `__client_files`: A dictionary to map clients to their respective files.

   - **Methods:**
     - `add_file(self, client, file)`: Adds a file to the repository for a specific client.
     - `get_files(self, client)`: Retrieves the list of files for a specific client.
     - `get_all_files(self)`: Retrieves the list of all files across all clients.

### 5. **ClientFileRepository Class:**

   - **Attributes:**
     - `local_files`: A list of files stored locally on the client.

   - **Methods:**
     - `add_local_file(self, lname, fname)`: Adds a local file to the client's repository.
     - `get_local_files(self)`: Retrieves the list of local files on the client.
     - `get_file_path(self, fname)`: Retrieves the file path for a given file name.

<!-- ### 6. **ConnectionManager Class:**

   - **Attributes:**
     - None (handles connections and threading).

   - **Methods:**
     - `establish_connection(self, address)`: Establishes a connection to the specified address.
     - `close_connection(self, socket)`: Closes a connection.
     - `start_thread(self, target, args)`: Starts a new thread for a specified target function with arguments. -->

