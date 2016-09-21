#!/usr/bin/env python

import argparse
import sys
import temperature

parser = argparse.ArgumentParser()
parser.add_argument("-c2k", "--celsiustokelvin", type=int, help="insert a conversion")
args = parser.parse_args()

print("The temperature in Kelvin is: " + str(temperature.celsius_to_kelvin(args.celsiustokelvin)))
