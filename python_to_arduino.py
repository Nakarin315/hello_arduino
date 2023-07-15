import serial.tools.list_ports
import serial
import time

def find_ports():
    # Finds ports for user to select
    serial_plot = serial.tools.list_ports.comports()
    port_dict = {}
    for port in serial_plot:
        if port.serial_number != None:
            port_dict[port.device] = port.serial_number
    return port_dict

def which_port(ID):
    # Finds Serial number for user to select
    serial_plot = serial.tools.list_ports.comports()
    port_dict = {}
    for port in serial_plot:
        if port.serial_number != None:
            port_dict[port.serial_number] = port.device
    return port_dict[ID]

# Initialize Arduino
usb_port = 'COM4'  # Choose the port to interrogate
baud_rate = 115200  # Baud rate for Arduino communication

print("Serial number at " + usb_port + " is: ")
print(find_ports()[usb_port])
arduino_serial = find_ports()[usb_port]  # Find serial number of Arduino when COM port is known
arduino_port = which_port(arduino_serial)  # Find port of Arduino when serial number is known
ser = serial.Serial(arduino_port, baud_rate, timeout=0.1)  # Serial communication between the Arduino board and the computer
time.sleep(2)  # Wait until Arduino has beeen connected

# Say Hello to Arduino
word_send = 'Hello'+'\r'
ser.write(word_send.encode('utf-8'))  # Send the word to Arduino


# Read and print the received data from Arduino
data = ser.readline().decode()
print("Received from Arduino:", data)

ser.close()  # Close the serial connection