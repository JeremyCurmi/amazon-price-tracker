import bs4
import requests
from requests.models import Response



def amazon_search_for_item(url: str) -> Response:
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"}
    response = requests.get(url=url, headers=headers)
    # TODO: check this method
    response.raise_for_status
    return response
    

def scrape_page(get_response: Response) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(get_response.text, 'html.parser')


def get_item_title(soup: bs4.BeautifulSoup) -> str:
    return soup.find(id='productTitle').get_text().strip()


def price_corrector(value: str) -> float:
    if '.' in value:
        return float(value)*1000
    return float(value)


def get_item_price(soup: bs4.BeautifulSoup) -> float:
    price = soup.find(id='corePrice_feature_div').get_text().strip()
    price = price.split('€')[0].split(',')[0]
    return price_corrector(price)
        

def get_item_shipping(soup: bs4.BeautifulSoup) -> float:
    shipping = soup.find(id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE").get_text().strip()
    shipping = shipping.split('€')[0].split(' ')[-1].split(',')[0]
    return price_corrector(shipping)


def get_price(response: Response) -> float:
    soup = scrape_page(response)
    title = get_item_title(soup)
    price = get_item_price(soup)
    shipping = get_item_shipping(soup)
    return price + shipping    
