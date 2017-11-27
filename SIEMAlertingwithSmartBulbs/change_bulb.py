import argparse, sys
from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='IP of smart bulb')
parser.add_argument('--state', help='Change state to on or off')
parser.add_argument('--color', help='Change color of bulb')
args=parser.parse_args()
print(args.ip)
bulb = SmartBulb(args.ip)
print(bulb.hsv)
if args.state == "off":
   bulb.state = "OFF"
if args.state == "on":
   bulb.state = "ON"
if args.color == "red":
   if bulb.is_color:   
      bulb.hsv = (0, 100, 100) # set to red
if args.color == "orange":
   if bulb.is_color:   
      bulb.hsv = (12, 100, 100) # set to orange
if args.color == "yellow":
   if bulb.is_color:   
      bulb.hsv = (60, 100, 100) # set to yellow
if args.color == "blue":
   if bulb.is_color:   
      bulb.hsv = (209, 100, 100) # set to blue
