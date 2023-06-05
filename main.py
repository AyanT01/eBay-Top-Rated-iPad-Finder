from bs4 import BeautifulSoup
import requests
def get_request_and_parse():
    ebay = requests.get("https://www.ebay.com/sch/i.html?_fsrp=1&LH_Savings=1&rt=nc&_from=R40&_nkw=ipads&_sacat=0&LH_ItemCondition=2030")
    ebay_text = ebay.text
    new_soup = BeautifulSoup(ebay_text,"html.parser")
    names = new_soup.find_all("span", role="heading")
    names = [i.getText() for i in names]
    del names[0]
    ratings = new_soup.find_all("div", class_="x-star-rating")
    ratings_value = []
    for i in ratings:
        rate_list = i.find("span",class_= "clipped").getText()
        ratings_value.append(rate_list)
    ratings_value = [float(i[0:3]) for i in ratings_value]
    prices = new_soup.find_all("div",class_="s-item__info-section")
    links = [a.get("href") for div in new_soup.find_all("div", class_="s-item__image") for a in div.find_all("a")]
    prices = new_soup.find_all("span", class_="s-item__price")
    del prices[0]
    prices_list = []
    for i in prices:
        prices_list.append(i.getText())
    prices_list = [i.split()[0] for i in prices_list if len(i) > 6]
    info_dict = {}
    print(len(names))
    print(len(ratings_value))
    print(names)
    print(ratings_value)
    """for index,value in enumerate(names):
        empty_dict = {
            "Name:":names[index],
            "Ratings:":ratings_value[index],
            "Prices":prices_list[index],
            "Links":links[index]
        }
        info_dict[index] = empty_dict
    return info_dict
    """
get_request_and_parse()

"""
listt = get_request_and_parse()
print(listt)
def write_to_file():
    pass
    #with open("items.txt","w") as file:
"""
