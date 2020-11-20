############################
#        server.py         #
#    made by Emma Darbois  #
############################

from bluetooth import *

def enable() :
    server_socket=BluetoothSocket( RFCOMM )

    server_socket.bind(("", 3 ))
    server_socket.listen(1)

    client_socket, address = server_socket.accept()

    data = client_socket.recv(1024)

    print "received [%s]" % data

    return server_socket


def disable(server_socket, client_socket):
    client_socket.close()
    server_socket.close()
    return 0
