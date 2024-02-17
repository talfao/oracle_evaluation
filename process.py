import json
import ast
def process_raw_data(filename: str):
    i = 0
    headline_inserted = False
    with open(filename, "r") as f:
        for line in f.readlines():
            if i == 0:
                i+=1
                continue
            address = line.split(",")[0].strip()
            data = line.split(",")[1::]
            data = ",".join(data).strip()
            json_string = json.dumps(ast.literal_eval(data))
            json_object = json.loads(json_string)
            contract_data = json_object.get(address).get("address")
            headline = "Address,"
            if contract_data.get("type") == "contract":
                line = f"{address},"
                for key in contract_data.keys():
                    if key in ("contract_code_hex", "type"):
                               continue
                    headline += key + ","
                    line += str(contract_data.get(key)) + ","
                if not headline_inserted:
                    with open("statistics/ProcessedRawData.csv", "a") as f2:
                        f2.write(headline + "\n")
                    headline_inserted = True
                with open("statistics/ProcessedRawData.csv", "a") as f2:
                    f2.write(line + "\n")


def main():
    process_raw_data(filename="statistics/EthereumAddressRawData.csv")


main()