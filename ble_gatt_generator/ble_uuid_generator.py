#! /usr/local/bin/python3
import yaml
import os

pathTOHeaderFile = "./c/BLE_DESIGN.g.h"
# pathToSerialDebugTool = "./c/BLE_DESIGN.g.h"
pathToDartFile = "./dart/ble_desgin_constants.g.dart"

deviceName = "esp32"


def read_config():
    with open("./ble_uuid_conf.default.yml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # yaml.load()
        # return list of key and value pair
        global deviceName
        deviceName = data["device_info"]["device_name"]
        return(data["gatt_profile"])


def cHeaderFileLimbo(listOfData):
    deviceNameDefine = '''#ifndef DEVICE_NAME\n#define DEVICE_NAME "{value}"\n#endif\n'''.format(
        value=deviceName)
    output = ""
    for i in listOfData:
        for key, value in i.items():
            text = '''#ifndef {key}\n#define {key} "{value}"\n#endif
            '''.format(key=key, value=value)
            output += text + "\n"
    return deviceNameDefine+output


def dartCode(listOfData):
    deviceNameDartCode = '''const String DEVICE_NAME = "{deviceId}";'''.format(
        deviceId=deviceName)
    # import required library
    output = "//Generate in git submodule (ble_devices) -> ble_uuid+generator.py" + \
        "\nimport 'package:flutter_reactive_ble/flutter_reactive_ble.dart';\n// ignore_for_file: non_constant_identifier_names\n"
    servicesAsList = ""
    geneteuuid = ""
    for i in listOfData:
        for key, value in i.items():
            text = '''Uuid {key} = Uuid.parse("{value}");
            '''.format(key=key, value=value)
            geneteuuid += text + "\n"
            if "SERVICE" in key:
                servicesAsList += '''{key},'''.format(key=key)

    servicesUUIDasListExport = '''List<Uuid> deviceServices = [{services}];'''.format(
        services=servicesAsList)
    return output+geneteuuid+"\n"+servicesUUIDasListExport+"\n"+deviceNameDartCode


def generate(fileGenrateCallback, fileLocation):
    text = "//THIS IS GENERATED IN ble_uuid_conf.yml\n"
    text += fileGenrateCallback(read_config())
    os.makedirs(os.path.dirname(fileLocation), exist_ok=True)
    f = open(fileLocation, 'w+')
    f.write(text)
    f.close()


# def gattUUIDTextMapper():


def run():
    generate(dartCode, pathToDartFile)
    generate(cHeaderFileLimbo, pathTOHeaderFile)


# TODO generate serial debug tool for c++
run()
