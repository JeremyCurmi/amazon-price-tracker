import scraper

def main(item: str):
    response = scraper.amazon_search_for_item(item)
    price = scraper.get_price(response)
    print(price)

if __name__=="__main__":
    url = "https://www.amazon.de/Samsung-LC49G94TSSUXZG-Gaming-Monitor-schwarz/dp/B08BX69B68/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=Samsung+G9&qid=1637784902&qsid=262-8430737-4268509&sr=8-5&sres=B096GCHVYF%2CB08WJGFDCS%2CB08SWHCZ8T%2CB0859SZJQK%2CB08BX69B68%2CB08SW81TY3%2CB08SVY94MF%2CB08SWJ3G45%2CB08WM54JQQ%2CB08SW6X1V9%2CB07PQ4MPT6%2CB08SWH5NQJ%2CB094DKQPTZ%2CB08SW8HC78%2CB08KNX9YYH%2CB0859SVYN7&srpt=MONITOR"
    # url = 'https://www.amazon.de/Apple-Magic-Keyboard-Neuestes-Modell/dp/B09BTHFP3G/ref=pd_rhf_ee_s_bmx_gp_ml6e6lno_2/262-8430737-4268509?pd_rd_w=eOCbl&pf_rd_p=a6601c68-7d25-4845-99ca-b77969c12089&pf_rd_r=MQ6FDCNG6VATGRBN6XER&pd_rd_r=78b11d57-6f34-4f28-b9ee-09de6d44fba7&pd_rd_wg=nahkO&pd_rd_i=B09BTHFP3G&psc=1'
    main(url)