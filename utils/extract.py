import bs4


def cbsnews(response) -> dict:
    title = bs4.BeautifulSoup(
        response, features='lxml').find_all("h1")[0].text
    body_element_text_list = []
    for p in bs4.BeautifulSoup(response, features='lxml').find_all("p"):
        body_element_text_list.append(p.text.replace("\n", "").strip())
    body = ", ".join(body_element_text_list)
    return {'title': title, 'body': body}


def thewire(response) -> dict:
    title = bs4.BeautifulSoup(
        response, features='lxml').find_all("h1")[0].text
    body_element_text_list = []
    for p in list(bs4.BeautifulSoup(response, features='lxml').select("div>p")):
        body_element_text_list.append(p.text.replace("\n", "").strip())
    body = ", ".join(body_element_text_list)
    return {'title': title, 'body': body}
