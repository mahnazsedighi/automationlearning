from selenium import webdriver
from selenium.webdriver.common.keys import Keys
base_url = "https://testautomation-playground.herokuapp.com/"
driver = webdriver.Chrome(executable_path="c:\chromedriver.exe")
#driver.get("https://testautomation-playground.herokuapp.com/advanced.html")
#driver.find_elements_by_id('input')
#search_filed = driver.find_element('id','txt_rating')
#search_filed.send_keys("mahnaz")
#search_filed.send_keys(keys.RETURN)
driver.get(f"{base_url}/forms.html")
driver.find_element('id','check_python').click()
check1 = driver.find_element('id','check_validate').text
assert check1 =='PYTHON'
text1 = "hello world"
driver.find_element('id','notes').send_keys(text1)
check2 = driver.find_element('id ','area_notes_validate').text
assert check2 == text1
