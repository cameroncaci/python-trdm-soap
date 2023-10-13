import logging
import datetime
from suds.client import Client
from wsse_setup import setup_wsse_x509 

# Vars
public_key_path = 'pem/publickey.pem'
private_key_path = 'pem/pricatekey.pem'

# Setup logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

url = 'file:///Users/cameron/Projects/trdm-cron-lambda/wsdl/ReturnTableV7.wsdl'
client = Client(url)

# Create physicalNameType type (Used in getLastTableUpdate)
physicalName = client.factory.create('physicalNameType')
physicalName = 'LN_OF_ACCT'
# print (physicalName)

# Create ReturnTableInput type (Used in getTable)
input = client.factory.create('ReturnTableInput')
input.TRDM.physicalName = "LN_OF_ACCT"
input.TRDM.returnContent = "true"
input.TRDM.contentUpdatedSinceDateTime = datetime.datetime.now()

# print (input)

# Apply security to client
client = setup_wsse_x509(client, public_key_path, private_key_path)
print (client)

result = client.service.getLastTableUpdate(physicalName)

print (result)
# result = client.service.getLastTableUpdate()
# print (result)

# print(client)