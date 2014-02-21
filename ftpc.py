#client that send the file 
import os, struct, socket, sys,time


def main(host,port,inputfile):
    
    # create client socket.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect client socket to server
    client.connect((host, int(port)));

    #prepare the packet to be sent
    file1 =  open(inputfile, 'rb');
    m=0;
    # get the size of the image and pack it to 4-byte
    size = struct.pack('<I', os.path.getsize(inputfile))

    #format the filename to 20-byte and encode it
    filename = inputfile.rjust(20).encode();
    
    while (1):
    
	data = file1.read(1000);

	if len(data)==1000 :
		packet = size + filename+data;
		client.sendall(packet)
		time.sleep(0.000005);
        elif len(data)<1000:
		packet = size + filename+data;
		
		client.sendall(packet)

		break;
    	

    #properly shutdown the client
    client.shutdown(socket.SHUT_RDWR)
    #close the client socket
    client.close()

if __name__ == '__main__':
    try:
        host = sys.argv[1] #remote host
        port = sys.argv[2] #port used by the server
        inputfile = sys.argv[3] #local filename
    except IndexError:
        print 'python ftpc.py <remote-IP> <remote-port> <local-file-to-transfer>'
        sys.exit(2)
    main(host,port,inputfile)
