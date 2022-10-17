#! /usr/local/bin/python3
import os
from pickle import FALSE
import serial
import time
import random
import sys
import uuid
# its win32, maybe there is win64 too?
is_windows = sys.platform.startswith('win')

PORT = "/dev/tty.usbserial-A50285BI"

if is_windows:
    PORT = "COM5"

arduino = serial.Serial(port=PORT,
                        baudrate=115200, timeout=.1)
counter = 0
key = 0
text = ""


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def getUUID():
    totalByte = 22
    return uuid.uuid4().hex[0:totalByte]


def emulator(pid_id, data):
    global text
    key = pid_id
    if data == None:
        num = random.randrange(1500, 2000)
    else:
        num = data
    formatedText = '''{key}:{counter}'''.format(key=key, counter=num)
    text = formatedText


def runner():
    print(text)
    time.sleep(0.2)
    arduino.write(bytes(text, 'utf-8'))
    time.sleep(0.5)


obd_pids = {
    "CALCULATED_ENGINE_LOAD": 4,
    "ENGINE_COOLANT_TEMPERATURE": 5,
    "ENGINE_RPM": 12,
    "VEHICLE_SPEED": 13,
    "AIR_INTAKE_TEMPERATURE": 15,
    "DISTANCE_TRAVELED_WITH_MIL_ON": 33,
    "DISTANCE_TRAVELED_SINCE_CODES_CLEARED": 49,
    "ENGINE_OIL_TEMPERATURE": 92,
    "TIME_SINCE_TROUBLE_CODES_CLEARED": 78,
}


sensor_table_v2 = {v: k for k, v in obd_pids.items()}


def keyNotNull(textInput):
    return (textInput != "") and (sensor_table_v2.get(int(textInput)) != None)


while 1:
    print("Type in sensor number to emulate over ble")
    print("-----------")
    for pid_key in sensor_table_v2:
        pid_value = sensor_table_v2[pid_key]
        formattedString = '''[{key}] \t : {value}'''.format(
            key=pid_key, value=pid_value)
        print(formattedString)
    print("-----------")
    textInput = input("type in number : ")
    isMode1 = ":" in textInput
    if isMode1:
        pid_id = textInput.split(":")[0]
        data = textInput.split(":")[1]
        if keyNotNull(pid_id):
            emulator(pid_id, data)
            runner()
        else:
            print("Wrong format")
            time.sleep(1.5)
    if isMode1 == False:
        if keyNotNull(textInput):
            emulator(textInput, None)
            runner()
        else:
            print("Wrong format")
            time.sleep(1.5)
    clear()
