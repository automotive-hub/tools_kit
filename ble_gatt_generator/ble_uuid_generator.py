#! /usr/local/bin/python3
import yaml
import os
import itertools


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
    BLE_KEYS = []
    for i in listOfData:
        for key, value in i.items():
            text = '''Uuid {key} = Uuid.parse("{value}");
            '''.format(key=key, value=value)
            BLE_KEYS.append(key)
            geneteuuid += text + "\n"
            if "SERVICE" in key:
                servicesAsList += '''{key},'''.format(key=key)

    servicesUUIDasListExport = '''List<Uuid> deviceServices = [{services}];'''.format(
        services=servicesAsList)
    ble_gatt_generated = output+geneteuuid+"\n" + \
        servicesUUIDasListExport+"\n"+deviceNameDartCode
    ble_gatt_generated += "\n"
    dartEnumList = []
    for text in BLE_KEYS:
        capitalLifeText = ["".join(x.capitalize()) for x in text.split('_')]
        joinedText = "".join(capitalLifeText)
        removeBLEText = joinedText.replace("Ble", "")
        lowerCaseFristLetter = removeBLEText[0].lower() + removeBLEText[1:]
        dartEnumList.append(lowerCaseFristLetter)
    # print(dartEnumList)
    dartEnumList = [x for x in dartEnumList if "service" not in x]
    ble_obd_enum = '''enum BleOBDCheckList ''' + \
        "{" + '''{ble_name}'''.format(ble_name=",".join(dartEnumList)) + "}"
    ble_gatt_generated += ble_obd_enum

    # ble_gatt_char array
    characteristic_uuid = list(filter(
        lambda item: ("SERVICE" not in item), BLE_KEYS))
    characteristic_uuid_keys = ""
    for uuid in characteristic_uuid:
        characteristic_uuid_keys += '''{key},'''.format(key=uuid)
    ble_gatt_char = '''List<Uuid> deviceCharacteristic = [{list}];'''.format(
        list=characteristic_uuid_keys)
    ble_gatt_generated += "\n"
    ble_gatt_generated += ble_gatt_char
    # # gatt_map
    # ble_gatt_service = {}
    # for i in listOfData:
    #     for key, value in i.items():
    #         if "SERVICE" in key:
    #             ble_gatt_service[key] = []
    #         # if "ENGINE"

    # dartMap = '''Map<Uuid,List<Uuid>> BLE_MAP = {
    #     {data}
    # }'''.format(data="")
    # print(characteristic_uuid_keys)
    dartOBDEnumBLEGattSwitchCaseText = dartOBDEnumBLEGattSwitchCase(
        dartEnumList, characteristic_uuid)
    ble_gatt_generated += dartOBDEnumBLEGattSwitchCaseText
    return ble_gatt_generated


def dartOBDEnumBLEGattSwitchCase(listObdEnum, listBle_gatt_uuid):
    listOfCase = []
    for obdEnum, ble_gatt_uuid in zip(listObdEnum, listBle_gatt_uuid):
        ifStatement = '''
        if (characteristicId == {ble_gatt_uuid}) {{
            return BleOBDCheckList.{obdEnum};
        }}
        '''.format(ble_gatt_uuid=ble_gatt_uuid, obdEnum=obdEnum)
        listOfCase.append(ifStatement)
        # print(obdEnum, ble_gatt_uuid)

    template = '''
    BleOBDCheckList getOBDEnmum(Uuid characteristicId) {{
        {cases}
        return BleOBDCheckList.engineAirIntakeTempCharacteristic;
    }}
    '''.format(cases="\n".join(listOfCase))
    # print("\n".join(listOfCase))
    return template


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
