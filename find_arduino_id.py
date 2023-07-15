import serial.tools.list_ports  # For listing available serial ports
import serial  # For serial communication

def find_ports():
    # Finds ports for user to select
    serial_plot = serial.tools.list_ports.comports()
    port_dict = {}
    for port in serial_plot:
        if port.serial_number != None:
            port_dict[port.device] = port.serial_number
    return port_dict

usb_port = 'COM4' #choose the port to interogate
print("Serial number at "+usb_port +" is: ")
print(find_ports()[usb_port])

x = input()