import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
#receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

for path in glob.iglob('./new/receipt-[0-9]*.json'):#receipts
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
