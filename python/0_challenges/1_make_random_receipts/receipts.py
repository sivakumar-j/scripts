import random
import os
import json

##the challenge is to create a n ( in this case file_count) files with random words and numbers

count = int(os.getenv("FILE_COUNT") or 10)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]


for identifier in range(count): ##create a list with range up to count
    amount = random.uniform(1.0, 1000) ##gen float bw 1 ~ 1000
    content = {
        'topic': random.choice(words), #pick a random word from words file
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{identifier}.json', 'w') as f: ##creates a new file
        json.dump(content, f)
