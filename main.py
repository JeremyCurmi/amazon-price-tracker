import mail
import utils
import scraper

def main(link: str, max_price: float):
    response = scraper.amazon_search_for_item(link)
    price = scraper.get_price(response)
    should_send_email = utils.has_price_decreased(price, max_price)
    if should_send_email:
        mail.send_mail(link, price)

if __name__=="__main__":
    link = "https://www.amazon.de/Samsung-LC49G94TSSUXZG-Gaming-Monitor-schwarz/dp/B08BX69B68/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=Samsung+G9&qid=1637784902&qsid=262-8430737-4268509&sr=8-5&sres=B096GCHVYF%2CB08WJGFDCS%2CB08SWHCZ8T%2CB0859SZJQK%2CB08BX69B68%2CB08SW81TY3%2CB08SVY94MF%2CB08SWJ3G45%2CB08WM54JQQ%2CB08SW6X1V9%2CB07PQ4MPT6%2CB08SWH5NQJ%2CB094DKQPTZ%2CB08SW8HC78%2CB08KNX9YYH%2CB0859SVYN7&srpt=MONITOR"
    main(link, 1300)