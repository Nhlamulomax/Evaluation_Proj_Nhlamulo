from selenium import webdriver

try:
    br = webdriver.Chrome()
    br.get('https://slashdot.org/login.pl')
    username = br.find_element_by_id('unickname')
    username.send_keys('Nhlamulomax')
    password = br.find_element_by_id('upasswrd')
    password.send_keys('nhlamulo@Slashdot')
    password.submit()
except:
    print("Headling")
finally:
    print("I am in")