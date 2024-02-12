import sp_test as sp
import os

import create_stock_data_file as create_sf
import stockpy_prog.handler.file_handler as dt

STOCK_DATA_INFO = "./stock_list/stock_data_info.json" #constant for path to stock data info file


def get_stock_short_code():
    #integriere failsave!
    short_code:str = input('Type in the short code of the stock you want to analyze (e.g. AAPL for Apple stock):')
    return short_code

def check_for_valid_imput():
    
    is_valid:bool = False
    short_codes:list = get_stock_short_codes()

    while not is_valid:
        
        short_code:str = get_stock_short_code().upper()

        if(short_code in short_code_db):
            short_code_db.append(short_code)
            is_valid = True
        else:
            print('Invalid input, please try again.\n')
            is_valid = False    

def main():
    
    data_path:str = ''

    print('\n')
    stock_short_code:str = get_stock_short_code().upper()
    print(f'shortcode is {stock_short_code}')

    data_path = get_stock_short_code(stock_short_code)

    if os.path.isfile(data_path):
        print('File already exists!\n')
    else:
        print('File does not exist, creating file... \n')
        create_sf.create_stock_data_file(data_path) 

main()