//THIS IS GENERATED IN ble_uuid_conf.yml
//Generate in git submodule (ble_devices) -> ble_uuid+generator.py
import 'package:flutter_reactive_ble/flutter_reactive_ble.dart';
// ignore_for_file: non_constant_identifier_names
Uuid BLE_SERVICE_ENGINE_UUID = Uuid.parse("8A40E28C-E92A-4406-874E-4F71A21F69DB");
            
Uuid BE_ENGINE_RPM_CHARACTERISTIC = Uuid.parse("821B25CA-37A9-4E20-940C-170496C9446D");
            
Uuid BLE_ENGINE_SPEED_METER_CHARACTERISTIC = Uuid.parse("B3BAD50B-91E6-4AE2-8ED6-9E35EE5D258D");
            
Uuid BLE_ENGINE_AIR_INTAKE_TEMP_CHARACTERISTIC = Uuid.parse("AD667745-DD87-470D-A76A-976F68500C5B");
            
Uuid BLE_ENGINE_LOAD_CHARACTERISTIC = Uuid.parse("D7C50612-A2F4-4D35-B7FA-1B9F26968FD1");
            
Uuid BLE_ENGINE_COOLANT_TEMPERATURE_CHARACTERISTIC = Uuid.parse("A78BDDC4-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_ENGINE_OIL_TEMPERATURE = Uuid.parse("A78BE094-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_SERVICE_VEHICLE_UUID = Uuid.parse("A78BE2BA-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_VEHICLE_SPEED_CHARACTERISTIC = Uuid.parse("A78BE42C-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_VEHICLE_TIME_RUN_WITH_MIL_ON_CHARACTERISTIC = Uuid.parse("A78BE8E6-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_VEHICLE_TIME_SINCE_CODES_CLEARED_CHARACTERISTIC = Uuid.parse("A78BEA44-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_VEHICLE_DISTANCE_TRAVELED_WITH_MIL_ON__CHARACTERISTIC = Uuid.parse("A78BEB84-4D02-11ED-BDC3-0242AC120002");
            
Uuid BLE_SERVICE_GENERIC_UUID = Uuid.parse("8A40E28C-E92A-4406-874E-4F71A21F69CC");
            
Uuid BLE_SERVICE_OTA_UUID = Uuid.parse("1d14d6ee-fd63-4fa1-bfa4-8f47b42119f0");
            
Uuid BLE_CHARACTERISTIC_OTA_CONTROL = Uuid.parse("f7bf3564-fb6d-4e53-88a4-5e37e0326063");
            
Uuid BLE_CHARACTERISTIC_OTA_WRITE_NO_RSP = Uuid.parse("e984227f3-34fc-4045-a5d0-2c581f81a153");
            
Uuid BLE_SERVICE_BATTERY = Uuid.parse("180F");
            
Uuid BLE_CHARACTERISTIC_BATTERY_LEVEL = Uuid.parse("2A19");
            

List<Uuid> deviceServices = [BLE_SERVICE_ENGINE_UUID,BLE_SERVICE_VEHICLE_UUID,BLE_SERVICE_GENERIC_UUID,BLE_SERVICE_OTA_UUID,BLE_SERVICE_BATTERY,];
const String DEVICE_NAME = "ESP32-OBD2-BLE";