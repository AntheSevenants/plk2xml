import sys
import os

from plk2xml.plk import plk
from plk2xml.plk2xml import plk2xml
from plk2xml.plk2json import plk2json

if len(sys.argv) < 3:
	raise Exception("Usage: plk2xml.py input_file output_file")

plk_file = plk(sys.argv[1])

out_filename, out_extension = os.path.splitext(sys.argv[2])

if out_extension == ".xml":
	output = plk2xml(plk_file)
elif out_extension == ".json":
	output = plk2json(plk_file, indent=4)
else:
	raise ValueError("Only .xml and .json output are supported")

with open(sys.argv[2], "wt") as writer:
	writer.write(output)