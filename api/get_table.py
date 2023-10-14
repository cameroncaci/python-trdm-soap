from .ws_client import client_return_table

# Convert the received REST call into ReturnTableInput type friendly
def get_table(input_data):
    # Construct the data structure as required by the WSDL
    data = {
        'TRDM': {
            'physicalName': input_data.get('physicalName'),
            'contentUpdatedSinceDateTime': input_data.get('contentUpdatedSinceDateTime'),
            'returnContent': input_data.get('returnContent', 'true'),
        }
    }
    print("Constructed Data: ", data)

    return client_return_table.getTable(data)