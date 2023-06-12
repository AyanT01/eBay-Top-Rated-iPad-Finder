from bs4 import BeautifulSoup
import requests
import csv

link = requests.get("https://www.ebay.com/sch/i.html?_nkw=ipad&_sacat=0&LH_Savings=1&LH_FS=1&rt=nc&_udlo=150&_udhi=350")
link = link.text
new_link = BeautifulSoup(link,"html.parser")
names = new_link.find_all("span",role="heading")
items_list = []
for i in names:
    if i.getText() == "Shop on eBay":
        continue
    items_list.append(i.getText())

prices= new_link.find_all("span",class_="s-item__price")
prices_list = []
for i in prices:
    if i.getText() == "$20.00":
        continue
    prices_list.append(i.getText()[0:7])

links = [a.get("href") for div in new_link.find_all("div",class_="s-item__info clearfix") for a in div.find_all("a") if a.get("href") != "http://pages.ebay.com/trp/index.html"]
for i in links:
    if i == "https://ebay.com/itm/123456?hash=item28caef0a3a:g:E3kAAOSwlGJiMikD&amdata=enc%3AAQAHAAAAsJoWXGf0hxNZspTmhb8%2FTJCCurAWCHuXJ2Xi3S9cwXL6BX04zSEiVaDMCvsUbApftgXEAHGJU1ZGugZO%2FnW1U7Gb6vgoL%2BmXlqCbLkwoZfF3AUAK8YvJ5B4%2BnhFA7ID4dxpYs4jjExEnN5SR2g1mQe7QtLkmGt%2FZ%2FbH2W62cXPuKbf550ExbnBPO2QJyZTXYCuw5KVkMdFMDuoB4p3FwJKcSPzez5kyQyVjyiIq6PB2q%7Ctkp%3ABlBMULq7kqyXYA":
        links.remove(i)
    elif i.startswith("https://www.ebay.com/p/"):
        links.remove(i)


with open("Ebay_project.csv", "w", newline="") as f:
    writer = csv.writer(f)
    header = ["Names", "Price", "Links"]
    writer.writerow(header)
    for i in range(len(items_list)):
        row = [items_list[i], prices_list[i], links[i]]
        writer.writerow(row)