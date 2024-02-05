# Import necessary libraries
import bs4
from utils import logger


def cbsnews(response) -> dict:
    """Function to extract article from `CBS News`

    Args:
        response (string): response content got from fetching news article url

    Returns:
        dict: containing title and body
    """
    try:
        title = bs4.BeautifulSoup(
            response, features='lxml').find_all("h1")[0].text
        body_element_text_list = []
        for p in list(bs4.BeautifulSoup(response, features='lxml').find_all("p")):
            body_element_text_list.append(p.text)
        body = ", ".join(body_element_text_list)
        return {'title': title, 'body': body}
    except Exception as e:
        logger.log_message(e.args, level=1)


def thewire(response) -> dict:
    """Function to extract article from `The Wire`

    Args:
        response (string): response content got from fetching news article url

    Returns:
        dict: containing title and body
    """
    try:
        title = bs4.BeautifulSoup(
            response, features='lxml').find_all("h1")[0].text
        body_element_text_list = []
        for p in list(bs4.BeautifulSoup(response, features='lxml').select("div>p")):
            body_element_text_list.append(p.text)
        body = ", ".join(body_element_text_list)
        return {'title': title, 'body': body}
    except Exception as e:
        logger.log_message(e.args, level=1)
