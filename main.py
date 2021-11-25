import mail
import utils
import scraper


def main(links: list, max_price: float):
    for link in links:
        response = scraper.amazon_search_for_item(link)
        price, err = scraper.get_price(response)
        if err != None:
            utils.log_error_get_price()
            continue
        should_send_email = utils.has_price_decreased(price, max_price)
        utils.log_service_logic(price, max_price, should_send_email)
        if should_send_email:
            mail.send_mail(link, price)


if __name__ == "__main__":
    links = [
        "https://www.amazon.de/Samsung-LC49G94TSSUXZG-Gaming-Monitor-schwarz/dp/B08BX69B68/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=Samsung+G9&qid=1637784902&qsid=262-8430737-4268509&sr=8-5&sres=B096GCHVYF%2CB08WJGFDCS%2CB08SWHCZ8T%2CB0859SZJQK%2CB08BX69B68%2CB08SW81TY3%2CB08SVY94MF%2CB08SWJ3G45%2CB08WM54JQQ%2CB08SW6X1V9%2CB07PQ4MPT6%2CB08SWH5NQJ%2CB094DKQPTZ%2CB08SW8HC78%2CB08KNX9YYH%2CB0859SVYN7&srpt=MONITOR",
        "https://www.amazon.de/Samsung-Odyssey-C49G95TSSR-LED-124/dp/B08SWRYY3R/ref=pd_vtp_4/262-8430737-4268509?pd_rd_w=HJwKf&pf_rd_p=4e0c7b51-e41d-4568-8470-6e0da61f6c1d&pf_rd_r=GK5W11F4H26JTMBFGFV9&pd_rd_r=7274fa66-fe42-44af-bc83-c34b24957766&pd_rd_wg=ErACn&pd_rd_i=B08SWRYY3R&psc=1",
        "https://www.amazon.de/Samsung-Odyssey-C49G93TSSR-Monitor-kompatibel/dp/B08SW6P7CH/ref=pd_vtp_2/262-8430737-4268509?pd_rd_w=HJwKf&pf_rd_p=4e0c7b51-e41d-4568-8470-6e0da61f6c1d&pf_rd_r=GK5W11F4H26JTMBFGFV9&pd_rd_r=7274fa66-fe42-44af-bc83-c34b24957766&pd_rd_wg=ErACn&pd_rd_i=B08SW6P7CH&th=1",
        "https://www.amazon.de/Samsung-LC49G94TSSUXZG-Gaming-Monitor-schwarz/dp/B08BX69B68/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=Samsung+G9&qid=1637784902&qsid=262-8430737-4268509&sr=8-5&sres=B096GCHVYF%2CB08WJGFDCS%2CB08SWHCZ8T%2CB0859SZJQK%2CB08BX69B68%2CB08SW81TY3%2CB08SVY94MF%2CB08SWJ3G45%2CB08WM54JQQ%2CB08SW6X1V9%2CB07PQ4MPT6%2CB08SWH5NQJ%2CB094DKQPTZ%2CB08SW8HC78%2CB08KNX9YYH%2CB0859SVYN7&srpt=MONITOR",
    ]
    main(links, 1200)
