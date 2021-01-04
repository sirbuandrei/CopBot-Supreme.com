from selenium import webdriver, common
import time, datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

seen = []


class Item(object):
    def __init__(self, coat, kw1, kw2, colour, size, name, email, tel, address, city, postcode, country, card_type,
                 card_number, card_month, card_year, card_val):
        self.coat = coat
        self.kw1 = kw1
        self.kw2 = kw2
        self.colour = colour
        self.size = size
        self.search_string = self.kw1 + ' ' + self.kw2
        self.name = name
        self.email = email
        self.tel = tel
        self.address = address
        self.city = city
        self.postcode = postcode
        self.country = country
        self.card_type = card_type
        self.card_number = card_number
        self.card_month = card_month
        self.card_year = card_year
        self.card_val = card_val

    def buy(self):
        driver = webdriver.Chrome("D:\\FInalProject\\driver\\chromedriver.exe")
        product_link = 'https://www.supremenewyork.com/shop/all/' + self.coat
        driver.get(product_link)
        #time.sleep(180)
        #element_name = WebDriverWait(driver).until(lambda d: d.find_elements_by_partial_link_text(self.search_string))
        element_name = driver.find_elements_by_partial_link_text(self.search_string)
        while not element_name:
            driver.refresh()
            element_name = driver.find_elements_by_partial_link_text(self.search_string)
        element_colour = driver.find_elements_by_partial_link_text(self.colour)
        print(datetime.datetime.now())
        for name in element_name:
            seen.append(str(name.get_attribute('href')))
        for colour in element_colour:
            if str(colour.get_attribute('href')) in seen:
                colour.click()
                break

        time.sleep(0.5)
        again = 1
        while again:
            again = 0
            try:
                driver.find_element_by_name('commit').click()
            except common.exceptions.NoSuchElementException:
                again = 1
                time.sleep(0.1)
        time.sleep(0.5)
        again = 1
        while again:
            again = 0
            try:
                driver.find_elements_by_partial_link_text('checkout')[0].click()
            except IndexError:
                again = 1
                time.sleep(0.1)
        driver.find_element_by_id('order_billing_name').send_keys(self.name)
        driver.find_element_by_id('order_email').send_keys(self.email)
        driver.find_element_by_id('order_tel').send_keys(self.tel)
        driver.find_element_by_name('order[billing_address]').send_keys(self.address)
        driver.find_element_by_id('order_billing_city').send_keys(self.city)
        driver.find_element_by_id('order_billing_zip').send_keys(self.postcode)
        driver.find_element_by_id('order_billing_country').send_keys(self.country + Keys.ENTER)
        #driver.find_element_by_id('credit_card_type').send_keys(self.card_type + Keys.ENTER)
        driver.find_element_by_id('cnb').send_keys(self.card_number)
        driver.find_element_by_id('credit_card_month').send_keys(self.card_month + Keys.ENTER)
        driver.find_element_by_id('credit_card_year').send_keys(self.card_year + Keys.ENTER)
        driver.find_element_by_id('vval').send_keys(self.card_val)
        driver.find_elements_by_class_name('icheckbox_minimal')[1].click()
        #time.sleep(3)
        driver.find_element_by_name('commit').click()
        print(datetime.datetime.now())
        time.sleep(180)


if __name__ == '__main__':
    item = Item('sweatshirts', 'Eyelet', 'Hooded', 'Black', 0, 'Andrei Sirbu', 'andreisirbu03@yahoo.com', '0737867094', 'str.Burebista nr.12 ap.4', 'Timisoara', '300678', 'R', 'visa', '4493 9100 0080 7723', '10', '2023', '179')
    item.buy()
