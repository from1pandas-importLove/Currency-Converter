import requests
import json

currency_you_have = input().lower()

query = f'http://www.floatrates.com/daily/{currency_you_have}.json'
query_usd = f'http://www.floatrates.com/daily/usd.json'
query_eur = f'http://www.floatrates.com/daily/eur.json'

r = requests.get(query)
r_usd = requests.get(query_usd)
r_eur = requests.get(query_eur)

# json_str = json.dumps(r.json(), indent=4)
# print(json_str)

# print(r_usd.json())

cache = {
    'usd' : r_usd.json(),
    'eur' : r_eur.json(),
    currency_you_have: r.json()
}

# print(json.dumps(cache, indent=4))


while True:
    currency_to_convert = input().lower()
    if currency_to_convert == '':
        break
    currency_to_convert_value = float(input())
    print('Checking the cache...')
    if currency_to_convert in cache.keys():
        print('Oh! It is in the cache!')
        converted_amount = round(currency_to_convert_value * cache[currency_you_have][currency_to_convert]['rate'], 2)
        print(f'You received {converted_amount} {currency_to_convert.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        dynamic_query = f'http://www.floatrates.com/daily/{currency_to_convert}.json'
        r_dynamic = requests.get(dynamic_query)
        cache[currency_to_convert] = r_dynamic.json()
        converted_amount = round(currency_to_convert_value * cache[currency_you_have][currency_to_convert]['rate'], 2)
        print(f'You received {converted_amount} {currency_to_convert.upper()}.')

