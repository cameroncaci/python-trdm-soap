from .ws_client import client_return_table

def get_last_table_update(input_data):
    physical_name = input_data.get('physicalName')
    print("Constructed Data: ", physical_name)
    return client_return_table.getLastTableUpdate(physical_name)