import requests
import json

def gather_address(url):
    with open("address.csv", "a") as address_file:
        response = requests.get(url)
        data = response.json()
        results = data.get("result")
        address_file.write("Address,Name,Timestamp,Inbound Calls,Outbound Calls\n")
        if results:
            fileMatches = results.get("FileMatches")
            if fileMatches:
                for f in fileMatches:
                    contract = f.get("Contract")
                    if contract:
                        address = contract.get("address")
                        name = contract.get("name")
                        timestamp = contract.get("timestamp")
                        inbound_calls = contract.get("inboundCallCount1Year")
                        outbound_calls = contract.get("outboundCallCount1Year")
                        if address and name and timestamp and inbound_calls and outbound_calls:
                            print(f"Address: {address} Name: {name} Timestamp: {timestamp} Inbound Calls: {inbound_calls} Outbound Calls: {outbound_calls}")
                            address_file.write(f"{address},{name},{timestamp},{inbound_calls},{outbound_calls}\n")
                        


def main():
    url = "https://www.codeslaw.app/api/search?q=chain:ethereum+latestRoundData&sort=inbound-calls-desc" ## Change if scrape something different
    gather_address(url)
main()