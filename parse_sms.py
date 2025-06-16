# This script parses the XML data.

import xml.etree.ElementTree as ET  # Library used to read and parse data.
import re  # Library use to work with regex expressions.
from datetime import datetime

def parse_sms_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    messages = [] # A list that will contain the parsed data (list of dictionnaries).

    for sms in root.findall('sms'): # Find all sms tags and go throught each one of them.
        body = sms.get('body', '').lower()
        date = int(sms.get('date', 0))
        readable_date = sms.get('readable_date', '')
        address = sms.get('address', '')
        contact_name = sms.get('contact_name', '')
        category = categorize_sms(body)

        amount = extract_amount(body)
        balance = extract_balance(body)

        messages.append({
            'date': datetime.fromtimestamp(date / 1000),
            'readable_date': readable_date,
            'address': address,
            'body': sms.get('body'),
            'amount': amount,
            'balance': balance,
            'category': category,
            'contact_name': contact_name
        })

    return messages

# A function that extracts the amount sent from the 'body' text
def extract_amount(text):
    match = re.search(r'([0-9,.]+)\s*rwf', text)
    if match:
        return int(match.group(1).replace(',', ''))
    return None

# A function that extracts the balance from the 'body' text
def extract_balance(text):
    match = re.search(r'new balance[: ]+([0-9,.]+)\s*rwf', text)
    if match:
        return int(match.group(1).replace(',', ''))
    return None

# A function that categories the messages according to the content of the 'body' text
def categorize_sms(text):
    text = text.lower()
    if "you have received" in text:
        return "Incoming Money"
    elif "payment of" in text and "to" in text:
        return "Payments to Code Holders"
    elif "transferred to" in text:
        return "Transfers to Mobile Numbers"
    elif "bank deposit" in text:
        return "Bank Deposits"
    elif "to airtime" in text:
        return "Airtime Bill Payments"
    elif "to mtn cash power" in text:
        return "Cash Power Bill Payments"
    elif "by direct payment" in text or "external transaction id" in text:
        return "Transactions Initiated by Third Parties"
    elif "withdrawn" in text:
        return "Withdrawals from Agents"
    elif "bank transfer" in text:
        return "Bank Transfers"
    elif "interineti" in text or "internet" in text:
        return "Internet and Voice Bundle Purchases"
    return "Uncategorized"
