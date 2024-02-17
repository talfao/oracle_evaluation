from dotenv import load_dotenv
import os
import requests
import time
import json
load_dotenv()

def main():
    api_key = os.getenv("blockchairAPIKey")
    # https://api.blockchair.com/ethereum/dashboards/address/0x3282791d6fd713f1e94f4bfd565eaa78b3a0599d?limit=1&offset=0
    i = 0
    with open("statistics/EthereumAddressRawData.csv", "a") as address_file:
        address_file.write(f"Address, raw data\n")
    with open("statistics/LatestRoundDataEthereum.csv", "r") as f:
        for line in f.readlines():
            # i += 1
            # if i <= 2008:
            #     continue
            address = line.split(",")[1].strip()
            # print(address)
            response = requests.get(f"https://api.blockchair.com/ethereum/dashboards/address/{address}?limit=1&offset=0&contract_details=true&key={api_key}")
            if response.status_code != 200:
                time.sleep(10)
                response = requests.get(f"https://api.blockchair.com/ethereum/dashboards/address/{address}?limit=1&offset=0&contract_details=true&key={api_key}")
                if response.status_code != 200:
                    print(f"Error getting data for {address}")
                    time.sleep(30)
                    continue
            data = response.json().get("data")
            info = data.get(address).get("address")
            type_of_address = info.get("type")
            if type_of_address == "contract":
                with open("statistics/EthereumAddressRawData.csv", "a") as address_file:
                    address_file.write(f"{address}, {data}\n")

        
main()