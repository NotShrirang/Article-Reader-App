# Import necessary libraries
import re
import json
import requests
from utils import loader, logger
from utils.extract import *


# Main function
def main():
    """Main Function
    """
    json_data: list = loader.load_json("config.json")
    final_data = {}
    # Loop through URLs
    for link in json_data:
        func_name = re.findall(
            r"[a-zA-Z0-9]+\.[a-zA-Z]+/", link)
        func_name = func_name[0].split(".")[0]
        response = requests.get(link)
        data = eval(func_name+"(response.content)", globals(), locals())
        final_data[link] = data
    with open("output.json", 'w') as f:
        json.dump(final_data, f, indent=4)


if __name__ == '__main__':
    main()
