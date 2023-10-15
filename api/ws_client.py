import datetime
from zeep import Client
from zeep.wsse.signature import BinarySignature
from zeep.wsse.utils import WSU
import xmlsec
# Declare vars for wsse creation
public_key_path = 'pem/publickey.pem'
private_key_path = 'pem/privatekey.pem'
wsdl_url = 'file:///Users/cameron/Projects/trdm-cron-lambda/wsdl/ReturnTableV7.wsdl'

# Create Timestamp
timestamp_token = WSU.Timestamp()
today_datetime = datetime.datetime.today()
expires_datetime = today_datetime + datetime.timedelta(minutes=10)
timestamp_elements = [
    WSU.Created(today_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")),
    WSU.Expires(expires_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"))
]
timestamp_token.extend(timestamp_elements)

# Create zeep client with WSSE and Timestamp configured
client = Client(wsdl=wsdl_url, wsse=BinarySignature(private_key_path, public_key_path, None, xmlsec.Transform.RSA_SHA512, xmlsec.Transform.SHA512))

# Bind ReturnTable service
client_return_table = client.bind('ReturnTable', 'ReturnTableWSSoapHttpPort')

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