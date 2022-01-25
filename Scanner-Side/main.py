from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#put your pos url 
my_pos_url='http://localhost'

#put your input_html_id_for_barcode 
input_html_id_for_barcode='scan-barcode-input'


driver = webdriver.Firefox()

driver.get(my_pos_url)
while(True):
    a=input("ENTER pr_cod:")
    b=input("ENTER number:")
    b=int(b)
    driver.find_element_by_id(input_html_id_for_barcode).send_keys(a)
    for i in range(b):
        driver.find_element_by_id(input_html_id_for_barcode).send_keys(Keys.ENTER)
