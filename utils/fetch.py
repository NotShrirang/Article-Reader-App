# Import necessary libraries
import re


def fetch_source_name(link: str) -> str:
    """Function for fetching source name from the link

    Args:
        link (str): link of the source

    Returns:
        str: source name
    """
    func_name = re.findall(
        r"[a-zA-Z0-9]+\.[a-zA-Z]+/", link)
    func_name = func_name[0].split(".")[0]
    return func_name
