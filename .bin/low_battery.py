#!/usr/bin/python
import os, time

while (True):
    with open("/sys/class/power_supply/BAT1/charge_now") as f:
        charge_now = float(f.read())
    with open("/sys/class/power_supply/BAT1/charge_full") as f:
        charge_full = float(f.read())
    with open("/sys/class/power_supply/BAT1/status") as f:
        status = f.read()

    percent = 100*charge_now/charge_full

    if (status != "Charging"):
        if percent < 15:
            command = "timeout 4 osdbattery"
            os.system(command)
            time.sleep(3)
        else: 
            time.sleep(300)
