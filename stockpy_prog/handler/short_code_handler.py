import datetime
import handler.file_handler as dth
import handler.stock_data_file_handler as sdfh

def get_stock_short_codes():
    data = dth.read_json_file_as_dict('./stock_info/stock_data_info.json')
    return_list:list = []
    for key in data:
        return_list.append(key)
    return return_list

def append_new_short_code(path:str, short_code:str):
    val:str = dth.read_json_file_as_string(path)
    if short_code not in val:
        new_item:dict = {
        short_code:{   
            "retreavel_date": f"{datetime.date.today().strftime("%Y-%m-%d")}",
            "retreavel_time": f"{datetime.datetime.now().strftime("%H:%M:%S")}",
            "name": f"Company name of {short_code}",
            "symbol": f"{short_code}",
            "path": f"./stock_data/{short_code}.csv"
            }
        }
        
        dth.append_to_json_file(path, new_item) #fix richtig einfügen
        sdfh.create_stock_data_file(short_code, new_item[short_code]['retreavel_date'])
        return True
    else:
        raise ValueError('Short code already exists in file.')
        return False