import requests
import time
import random
import pandas as pd


# cookies = {
# }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/nha-sach-tiki/c8322',
    'x-guest-token': 'NrvIUytC9BLbWEi3RHdAKfxG5VZYhFMn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = {
    'limit': '10',
    'sort': 'top_seller',
    'category': '8322',
    'page': '1',
    'urlKey':  'nha-sach-tiki',
}

product_id = []
for i in range(1, 50):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('data'):
            product_id.append({'id': record.get('id')})
    # time.sleep(random.randrange(3, 10))

df = pd.DataFrame(product_id)
df.to_csv('product_id.csv', index=False)