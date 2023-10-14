from .ws_client import client, client_return_table
from .print_envelope import print_envelope

# Convert the received REST call into ReturnTableInput type friendly
def get_table(input_data):
    # Construct the data structure as required by the WSDL
    data = {
        'TRDM': {
            'physicalName': input_data.get('physicalName'),
            'contentUpdatedSinceDateTime': input_data.get('contentUpdatedSinceDateTime'),
            'returnContent': input_data.get('returnContent')
        }
    }

    print("Constructed Data: ", data)
    
    node = client.create_message(client_return_table, 'getTable', input=data)
    print("Node: ", node)
    
    print_envelope(node)