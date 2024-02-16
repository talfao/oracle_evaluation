import subprocess
import time
def run_slither(detector: str):
    lines = []
    with open("address.csv", "r") as addresses:
        i = 0
        for line in addresses:
            # if i < 4:
            #     i+=1
            #     continue
            elements = line.split(",")
            address = elements[0].strip()
            if address.lower() == "Address".lower():
                write_to_result_file(str(line.strip()) + ", Slither Output" + "\n") 
                continue
            print(f"Running slither for {address}")
            command = f"slither {address} --detect {detector}"
            output = None
            try:
                output = subprocess.run(command, shell=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running slither for {address}: {e}")
            output = str(line.strip()) + "," + str(output.stderr) + "\n"
            write_to_result_file(output)
            time.sleep(5)

def write_to_result_file(line):
    with open("result.csv", "a") as result_file:
        result_file.write(line)

def main():
    run_slither("oracle-data-validation")

main()