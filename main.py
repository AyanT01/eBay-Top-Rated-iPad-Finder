from bs4 import BeautifulSoup
import requests
def get_request_and_parse():
    ebay = requests.get("https://www.ebay.com/sch/i.html?_fsrp=1&LH_Savings=1&rt=nc&_from=R40&_nkw=ipads&_sacat=0&LH_ItemCondition=2030")
    ebay_text = ebay.text
    new_soup = BeautifulSoup(ebay_text,"html.parser")
    names = new_soup.find_all("span", role="heading")
    names = [i.getText() for i in names]
    ratings = new_soup.find_all("div", class_="x-star-rating")
    ratings_value = []
    for i in ratings:
        rate_list = i.find("span",class_= "clipped").getText()
        ratings_value.append(rate_list)
    ratings_value = [float(i[0:3]) for i in ratings_value]
    prices = new_soup.find_all("div",class_="s-item__info-section")
    print(prices)
    links = [a.get("href") for div in new_soup.find_all("div", class_="s-item__image") for a in div.find_all("a")]
    print(links)
get_request_and_parse()
"""
def write_to_file():
    with open("items.txt","w") as file:
"""
