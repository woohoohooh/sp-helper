import csv
import json

import columns as columns
import pandas as pd

with open('skaterty.json', encoding='utf8') as f:
    templates = json.load(f)
    for i in templates:
        b = templates[i]['image_urls'][0]['url']
        p = b[0:2]
        c = 'https://www.engil.ru/img/' + b
        a = templates[i]
        e = str(a['desc'])
        g = [a['id'], a['price'], a['name'], c, e]
        print(a['name'], e)
        print()

        with open('my_file4.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow([a['id'], a['price'], a['name'], c, a['desc']])