#!/usr/bin/env python3

# File: nospace.py
# Author: Harrison Inocencio
# Date: 1-17-20
# Purpose: Removes spaces from provided file name(s) and replaces them with '_'

import os
import string
import argparse

# Constants
REPLACE_CHAR = '_'

"""
FUNC parse_args:
Initialize parser and export command line arguments.

PARAMS: None

RETURNS: user arguments (dict)
"""
def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('files', help='Target file name(s)', nargs="+")
	return parser.parse_args()

"""
CLASS nospace:
Main executable class for nospace script.

ATTR: 
	- fnames: Target file names (list of string)

FUNC:
	- run
	- convert
"""
class nospace:
	
	"""
	FUNC __init__:
	Initializes attributes based on passed arguments

	PARAMS: arguments (dict)

	RETURNS: None
	"""
	def __init__(self, args):
		self.fnames = args.files

	"""
	FUNC run:
	Converts each provided file name to "nospace" version using os.rename

	PARAMS: None {uses self attributes}

	RETURNS: None
	"""
	def run(self):
		for fname in self.fnames:
			new_name = self.convert(fname)
			print(f"{fname}->{new_name}")

	"""
	FUNC convert:
	Removes whitespace from passed file name and replace with REPLACE_CHAR

	PARAMS: unconverted file name (string)

	RETURNS: converted "nospace" file name (string)
	"""
	def convert(self, fname):
		new_name = ""
		for c in fname:
			if c not in string.whitespace:
				new_name += c
			else:
				new_name += REPLACE_CHAR

		return new_name

# Execution code
if __name__ == '__main__':
	args = parse_args()
	class_obj = nospace(args)
	class_obj.run()
