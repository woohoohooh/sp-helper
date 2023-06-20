import requests
import json

with open('../skaterty.json', encoding='utf8') as f:
    templates = json.load(f)

    for i in templates:
        b = templates[i]['image_urls'][0]['url']
        p = b[0:2]
        c = 'http://sp.tomica.ru/images/' + p + '/' + b

        p = requests.get(c)
        out = open(f'{b}', 'wb')
        out.write(p.content)
        out.close()
        print(f'спарсили {b}')
