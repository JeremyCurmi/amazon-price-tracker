import smtplib


def send_mail(link: str, price: float):
    username = 'jeremycurmi13@gmail.com'
    password = 'wjtjgfisystuhjip'


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)

    subject = "Amazon price fell down"
    body = f"Quick, checkout {link}, it has gone down to {price} euros!"
    msg = f"Subject: {subject} \n\n{body}"

    err = server.sendmail(
        from_addr=username,
        to_addrs=username,
        msg=msg
    )

    if err != {}:
        print("Email was not sent due to error: ", err)

    server.quit()