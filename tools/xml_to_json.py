#!/usr/bin/env python3

import sys
from xml.dom import minidom
import json

def convert(element):
  output = dict()

  constant = 0

  entries = element.getElementsByTagName("localized_string");
  for entry in entries:
    output[constant] = entry.getAttribute("Value")
    constant = constant + 1

  return output

def main(argv):
  if not len(sys.argv) == 3:
    print("xml_to_json.py <xml> <json>")
    return

  dom = minidom.parse(sys.argv[1])
  with open(sys.argv[2], 'w') as f:
    f.write(json.dumps(convert(dom), sort_keys=True))

if __name__ == "__main__":
  main(sys.argv)
