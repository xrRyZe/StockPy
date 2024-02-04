import sp_test as sp
import os

import create_stock_data_file as create_sf

def get_stock_short_code():
    #integriere failsave!
    short_code:str = input('hallo, gib den kürzel der aktie ein, für die du eine bewertung möchtest: ')
    return short_code

def main():

    print('\n')
    stock_short_code:str = get_stock_short_code().capitalize()
    print(f'shortcode is {stock_short_code}')

    if os.path.isfile(f"./stock_data/{stock_short_code}.csv"):
        print('File already exists!\n')
    else:
        print('File does not exist, creating file... \n')
        create_sf.create_stock_data_file(stock_short_code)

main()