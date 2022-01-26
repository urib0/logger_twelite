#!/usr/bin/env python3
# python3.7で動作確認済み

import serial
import json
import re

# 設定値読み込み
f = open("/home/pi/work/logger_twelite/config.json", "r")
conf = json.loads(f.read())
f.close()

path = conf["basedir"] + "/" + conf["logdir_name"]


readSer = serial.Serial(
conf["serial_port"], conf["serial_rate"], timeout=3)
raw = readSer.readline().decode().replace('\n', '')


for device in conf["devices"]:
	if device["sensor_id"] in re.split("[:=]",raw):
		print(raw)

