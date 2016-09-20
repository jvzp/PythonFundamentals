#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--module", type=str, help="Name of the module to be tested")
args = parser.parse_args()

imports = "import unittest\nimport {}\n".format(args.module)
print(imports)

import importlib, inspect
mod_to_test = importlib.import_module(args.module)
dict_of_functions = inspect.getmembers(mod_to_test, inspect.isfunction)

print("class Test_{}(unittest.TestCase):".format(args.module))

import types
for k,v in dict_of_functions:
	if isinstance(v, types.FunctionType):
		print("\t# Test function for the function {} of module {}".format(k,args.module))
		function_head = "\tdef test_{}(self):\n".format(k)
		print(function_head)
		function_body = "\t\tresult = {}.{}(1)\n\t\tself.assertTrue(result)\n".format(args.module,k)
		print(function_body)
		print("\n")

print("unittest.main()")
