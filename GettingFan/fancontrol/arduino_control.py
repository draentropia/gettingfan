# First import serial (pip install pyserial)
import serial, time

def send_order(switch):
    arduino = serial.Serial('/dev/ttyACM0', 9600)

    # Give some time to the board to connect
    time.sleep(2)

    # Print the order taking the value of the switch
    arduino.write(switch.encode('ascii'))

    # Close arduino connection
    arduino.close()
    print(switch+'hola')

