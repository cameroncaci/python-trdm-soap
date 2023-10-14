import xml.etree.ElementTree as ET

def print_envelope(envelope):
    xml_string = ET.tostring(envelope, encoding="unicode")
    print("\nPrinting XML string of provided envelope...\n")
    print(xml_string, "\n")