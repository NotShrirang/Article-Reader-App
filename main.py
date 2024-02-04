# Import necessary libraries
import json
import requests
from utils import fetch, loader, logger
from utils.extract import *
import timeit


# Main function
def main():
    """Main Function
    """
    try:
        logger.log_message("EXEC: Process Started", level=0)
        start_time = timeit.default_timer()
        json_data: list = loader.load_json("config.json")
        logger.log_message("config.json loaded.", level=0)

        final_data = {}
        # Loop through URLs
        for link in json_data:
            logger.log_message(f"Fetching data from: '{link}'...", level=0)

            # Get source name from the link
            function_name = fetch.fetch_source_name(link=link)

            # Fetch data from the website
            response = requests.get(link)

            # Call the function of the name same as the source name.
            data = eval(function_name+"(response.content)",
                        globals(), locals())

            final_data[link] = data
            logger.log_message("Fetching done!", level=0)
        logger.log_message("Dumping data into output.json...", level=0)
        # Dump data into output.json
        with open("output.json", 'w') as f:
            json.dump(final_data, f, indent=4)
        time_diff = timeit.default_timer() - start_time
        logger.log_message(
            f"Process completed in: {time_diff} seconds.", level=0)
    except NameError as e:
        logger.log_message(
            f"Source name not supported. {e.args}", level=1)
    except Exception as e:
        print(type(e))
        logger.log_message(e.args, level=1)


if __name__ == '__main__':
    main()
