import requests
from bs4 import BeautifulSoup
import time


def get_current_price():
    headers = {"Connection": "keep-alive",
                "DNT": "1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Dest": "document",
                "Referer": "https://www.google.com/",
                "Accept-Encoding": "gzip, deflate, br"}

    # Example product
    url = "https://www.amazon.com/dp/B0C73VBPQY/?coliid=I26RDD5LPIPHEB&colid=3ADYLDR16DU9H&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it"
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, 'lxml')
    results = soup.find("span", {"class":"a-price"}).find("span").text
    print(results)

    current_price = float(results[1:])


    return current_price


def main():
    previous_price = None
    change_price = 0
    run = True

    while run:
        current_price = get_current_price()
        if previous_price is None:
            previous_price = current_price

        if current_price == previous_price:
            change_price = 0

        if current_price != previous_price:
            change_price = previous_price - current_price

        print(f"Previous Price: ${previous_price}")
        print(f"Current Price: ${current_price}")
        print(f"Change in Price: ${change_price}")
        previous_price = current_price

        time.sleep(3600*6)


main()





