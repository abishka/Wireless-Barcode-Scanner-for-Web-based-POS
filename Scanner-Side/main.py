from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import socket

barcod_scaner_ip = "192.168.25.10"
barcod_scaner_port = 4210
recive_barcod_scaner_port = 4211

MESSAGE = b"udp_receved"


#put your pos url 
my_pos_url='http://localhost'


#put your input_html_id_for_barcode 
input_html_id_for_barcode='scan-barcode-input'


driver = webdriver.Firefox()

driver.get(my_pos_url)

sender_socket = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sender_socket.sendto(MESSAGE, (barcod_scaner_ip, barcod_scaner_port))


reciver_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
reciver_socket.bind(('0.0.0.0', recive_barcod_scaner_port))
while(True):
    data, addr = reciver_socket.recvfrom(128)  # buffer size is 1024 bytes
    print( data.decode('utf-8'))
    sender_socket.sendto(MESSAGE, (barcod_scaner_ip, barcod_scaner_port))
    driver.find_element_by_id(input_html_id_for_barcode).clear()
    driver.find_element_by_id(input_html_id_for_barcode).send_keys(data.decode('utf-8'))
    driver.find_element_by_id(input_html_id_for_barcode).send_keys(Keys.ENTER)
