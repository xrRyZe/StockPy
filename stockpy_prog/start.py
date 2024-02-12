import sp_test as sp
import os

import handler.stock_data_file_handler as create_sf
import handler.file_handler as dth
import handler.short_code_handler as sch


STOCK_DATA_INFO = "./stock_info/stock_data_info.json" #constant for path to stock data info file


def get_stock_short_code():
    #integriere failsave!
    short_code:str = input('Type in the short code of the stock you want to analyze (e.g. AAPL for Apple stock):')
    return short_code

def check_for_valid_imput():
    
    is_valid:bool = False
    short_codes:list = sch.get_stock_short_codes()

    while not is_valid:
        
        short_code:str = get_stock_short_code().upper()

        if(short_code in short_codes):
            is_valid = True
        elif(short_code not in short_codes):
            if(sch.append_new_short_code(STOCK_DATA_INFO, short_code)):
                is_valid = True
            else:
                print('Invalid input, please try again.\n')
                is_valid = False
                raise ValueError('Short code is wrong! Exit on fail!')
        else:
            print('Invalid input, please try again.\n')
            is_valid = False   

    return short_code

def main():
    
    data_path:str = ''

    print('\n')
    stock_short_code:str = check_for_valid_imput().upper()
    print(f'shortcode is {stock_short_code}')

    # data_path = get_stock_short_code(stock_short_code)

    if os.path.isfile(data_path):
        print('File already exists!\n')
    else:
        print('File does not exist, creating file... \n')
        create_sf.create_stock_data_file(data_path) 

main()