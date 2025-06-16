from parse_sms import parse_sms_xml
from insert_data import insert_messages

file_path = "./Data/modified_sms_v2.xml"

# Step 1: Parse the XML
messages = parse_sms_xml(file_path)

# Step 2: Insert into the database
insert_messages(messages)

print("Data parsing and insertion complete successfully!!")
