#server that receive the file
import socket, struct,sys,os

def main(port):
    #create new server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind port
    server.bind(('0.0.0.0', int(port)))

    #set max accept rate to 5 conenctions
    server.listen(5)

    #server socket accept the client
    client, address = server.accept()
    content = '';
    print "Receiving package......";
    while(1):

    	#get 4-byte packet
    	package = client.recv(1024);
	#print package;
	size_bytes = package[0:4];

    	#unpack 4-byte packet that determine the size of image
    	size = struct.unpack('<I', size_bytes)[0]

    	#decode the 20-byte that determine the filename and strip the space
	name = package[4:24];
    	filename =  name.decode().lstrip();

    	#get the remaining image bytes from client

	if len(content)<size:
		content = content + package[24::];

		if len(content)== size :
			break;
	else:
		break;
    with open(filename,'wb')as file:
	file.write(content);
    
    # Shutdown the socket and close the server conenction.
    server.shutdown(socket.SHUT_RDWR)
    server.close()
    #print the status
    print('Server has received the data from the client! ')


if __name__ == '__main__':
    try:
        port = sys.argv[1] 
    except IndexError:
        print 'python ftps.py <local-port>'
        sys.exit(2)
    main(port)
