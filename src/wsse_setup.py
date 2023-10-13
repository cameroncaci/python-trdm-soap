from suds.wsse import Security, BinaryToken

def setup_wsse_x509(client, public_key_path, private_key_path):
    # Create a WSSE security token
    security = Security()

    # Create a binary token with the certificate
    with open(public_key_path, 'rb') as cert_file:
        cert_data = cert_file.read()
        token = BinaryToken(cert_data)
        security.tokens.append(token)

    client.options.ssl.keyfile = private_key_path

    client.set_options(wsse=security)

    return client