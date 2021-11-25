import logging

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def has_price_decreased(price: float, max_price: float):
    return price < max_price


def log_service_logic(price: float, max_price: float, send_email: bool):
    if send_email:
        logging.info(
            f"Price: {price} is less than the set threshold: {max_price}!, Sending mail"
        )
    else:
        logging.info(f"Price: {price} is not less than the set threshold: {max_price}")


def log_error_get_price():
    logging.warning("Could not get price!")
