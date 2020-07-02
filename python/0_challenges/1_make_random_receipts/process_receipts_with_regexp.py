import glob
import os
import shutil
import json
import re

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts which are even numbered
receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') if re.match('./new/receipt-[0-9]*[02468].json', f)]
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f) ##convert from json format to python format
        subtotal += float(content['value'])
    #name = path.split('/')[-1]
    #destination = f"./processed/{name}"
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)# move the file else it will get accumulate
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: ${round(subtotal, 2)}")
#print("Receipt subtotal: $%.2f" % subtotal)
