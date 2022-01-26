#!/usr/bin/env python3
# python3.7で動作確認済み

import serial
import json
import re
import datetime
import os

def logging(path, name, data):
	timestamp = datetime.datetime.now()
	filename = name + "_" + timestamp.strftime("%Y-%m-%d") + ".csv"
	write_str = timestamp.strftime("%Y/%m/%d %H:%M:%S") + "," + data
	path = path + "/" + name + "/"

	os.makedirs(path, exist_ok=True)
	f = open(path + filename, mode="a")
	f.write(write_str + "\n")
	f.close()

# 設定値読み込み
f = open("/home/pi/work/logger_twelite/config.json", "r")
conf = json.loads(f.read())
f.close()

path = conf["basedir"] + "/" + conf["logdir_name"]

readSer = serial.Serial(
conf["serial_port"], conf["serial_rate"], timeout=3)

while True:
	raw = readSer.readline().decode().replace('\n', '')

	for device in conf["devices"]:
		if device["sensor_id"] in re.split("[:=]",raw):
			print(raw)
			logging(path, device["sensor_name"], raw)
			break

