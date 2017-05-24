import requests
import sys


def get_ticker(output_filename):
    if not isinstance(output_filename, str):
        raise TypeError('output filename must be a text string')

    r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=100')
    json_response = r.json()

    n_currencies = len(json_response)

    # output_filename = '/Users/mharvill/Desktop/crypto_currency_data.tsv'

    with open(output_filename, 'w') as f:
        f.write('symbol\tname\tprice (USD)\t1-hour change (%)\t24-hour change (%)\t7-day change (%)\t\n')

    for currency_index in range(n_currencies):
        current_json_response = json_response[currency_index]
        symbol = current_json_response['symbol']
        name = current_json_response['id']
        price = current_json_response['price_usd']
        change_1hr = current_json_response['percent_change_1h']
        change_24hr = current_json_response['percent_change_24h']
        change_7d = current_json_response['percent_change_7d']
        with open(output_filename, 'a') as f:
            f.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(symbol, name, price, change_1hr, change_24hr, change_7d))

if __name__ == "__main__":
    get_ticker(sys.argv[1])
