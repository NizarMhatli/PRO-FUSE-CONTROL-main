
#!/usr/bin/env python3
import socket


###################### SET UP Functions###########################
def UUID_get():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('192.168.20.99', 5000))
            s.send(bytes([0]))
            data = s.recv(1024)
            s.close()
        except:
            print('UUID cant be accessed')
    if data == b'\xfe':
        print('UUID not accessed correctly')
    return(data)




def Z_Homing ():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            data = UUID_get()
            s.connect(('192.168.20.99', 5000))
            s.send(data +b'\04')
            data3 = s.recv(1024)
            s.close()
        except:
            print('the command was not excuted')
        if data3 == b'\xff':
            print('the command was not excuted correctly')
        elif data3 == b'\xfd':
            print('the command sent is not correct')
    return (data3,data)



#################### ACTION FUNCTIONS#####################################

def PRO_SCREW_pik():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       try:
                if data == b'\x01':
                    s.connect(('192.168.20.99', 5000))
                    s.send(UUID +b'\01' + b'\00\00\00\01')
                    data1 = s.recv(1024)
                    s.close()
                else:
                    print('No command was sent')
       except:
           print('the command was not excuted')
       if data1 == b'\xff':
               print('the command was not excuted correctly')
       elif data1 == b'\xfd':
               print('the command sent is not correct')


def PRO_SCREW_in():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\02' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')




def PRO_SCREW_out():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\03' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')



################################ ACTION AND RETURN FUNCTIONS######################################################

def PRO_SCREW_pik_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       try:
                if data == b'\x01':
                    s.connect(('192.168.20.99', 5000))
                    s.send(UUID +b'\01' + b'\00\00\00\01')
                    data1 = s.recv(1024)
                    s.close()
                else:
                    print('No command was sent')
       except:
           print('the command was not excuted')
       if data1 == b'\xff':
               print('the command was not excuted correctly')
       elif data1 == b'\xfd':
               print('the command sent is not correct')

    return (data1)

def PRO_SCREW_in_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\02' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)


def PRO_SCREW_out_RE():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + b'\03' + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)

###################################PARAMETER SETTING########################

def PRO_PARA_IN():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + bytes([0x0c]) + b'\00\00\00\01')
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)




def PRO_CANCEL_C():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5100))
                s.send(UUID + bytes([0x01]))
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')

    return (data1)


def PRO_DATA_IN():
    data,UUID = Z_Homing()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            if data == b'\x01':
                s.connect(('192.168.20.99', 5000))
                s.send(UUID + bytes([0x1b]) + bytes([1])+ bytes([15]))
                data1 = s.recv(1024)
                s.close()
            else:
                print('No command was sent')
        except:
            print('the command was not excuted')
        if data1 == b'\xff':
            print('the command was not excuted correctly')
        elif data1 == b'\xfd':
            print('the command sent is not correct')
    return (data1)