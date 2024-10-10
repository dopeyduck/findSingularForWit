import re
from lxml import etree

# Define the namespace
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Get the witnesses from the user
witnesses_input = input("Please enter witnesses: ")

# Split the input strings by commas, tabs, and spaces, strip any leading or trailing whitespace from each witness, and convert the list of witnesses to a set
witnesses = set(witness.strip() for witness in re.split('[, \t]+', witnesses_input))

# Get the path of the XML file from the user
xml_file_path = input("Please enter the path of the XML file: ")

# Open and parse the XML file
with open(xml_file_path, 'r') as file:
    tree = etree.parse(file)

# Initialize a counter
counter = 0

# Iterate over all 'app' elements
for app in tree.xpath('//tei:app', namespaces=ns):
    rdgs = app.xpath('.//tei:rdg', namespaces=ns)

    # Initialize the 'A' text
    a_text = None

    # Check if any wit attribute contains 'A'
    for rdg in rdgs:
        if 'A' in rdg.get('wit', '').split():
            a_text = rdg.text
            break

    # Check if any wit attribute contains exactly one witness from the set and no other witnesses from the set
    for rdg in rdgs:
        wit = set(rdg.get('wit', '').split())
        intersection = wit & witnesses
        if len(intersection) == 1 and not (wit - intersection):
            # If so, print the 'n', 'from', 'to' attributes of the 'app', the 'n' attribute of the 'rdg', and the text of the 'rdg'
            print(f"{app.get('n')}\t{app.get('from')}\t{app.get('to')}\t{rdg.get('n')}\t{rdg.text}")
            counter += 1
            break