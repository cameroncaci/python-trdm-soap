from zeep import Client

# Declare vars for wsse creation
public_key_path = 'pem/publickey.pem'
private_key_path = 'pem/pricatekey.pem'
wsdl_url = 'file:///Users/cameron/Projects/trdm-cron-lambda/wsdl/ReturnTableV7.wsdl'

# Create zeep client with binded service
client = Client(wsdl=wsdl_url)
client_return_table = client.bind('ReturnTable', 'ReturnTableWSSoapHttpPort')

def get_last_table_update(physical_name):
    return client_return_table.getLastTableUpdate(physical_name)

# Convert the received REST call into ReturnTableInput type friendly
def get_table(input_data):
    if 'physicalName' not in input_data:
        raise ValueError('The "physicalName" field is required.')

    # Construct the data structure as required by the WSDL
    data = {
        'TRDM': {
            'physicalName': input_data['physicalName'],
            'contentUpdatedSinceDateTime': input_data.get('contentUpdatedSinceDateTime'),
            'returnContent': input_data.get('returnContent', 'true'),
        }
    }
    print("Constructed Data: ", data)

    return client_return_table.getTable(data)

'''
Operations under ReturnTable -> ReturnTableWSSoapHttpPort
         Operations:
            getLastTableUpdate(physicalName: ns0:physicalNameType) -> lastUpdate: ns0:lastUpdate, status: ns0:status
            getTable(input: ns0:ReturnTableInput) -> output: ns0:ReturnTableOutput, attachment: xsd:base64Binary
            
Used Global Types:
     ns0:ReturnTableInput (Used in GetTable)
     (TRDM: {
     physicalName: ns0:physicalNameType, returnContent: ns0:returnContent, 
     contentUpdatedSinceDateTime: ns0:contentUpdatedSinceDateTime, returnRowStatus: ns0:returnRowStatus, 
     returnMetadata: ns0:returnMetadata, returnLastUpdate: ns0:returnLastUpdate, returnColumns: {column: ns0:column[]}, 
     columnFilterMatchesCriteria: ns0:columnFilterMatchesCriteria, columnFilters: {columnFilter: ns0:columnFilter[]}
     })
'''