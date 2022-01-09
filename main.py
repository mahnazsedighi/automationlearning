from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://pro.kilid.com/")
#window_title = driver.title
#print(window_title)
sleep(2)
#driver.refresh()
#driver.quit()
driver.switch_to.new_window('window')
driver.get("https://kilid.com/")
sleep(2)
pro_window = driver.current_window_handle
print('yahoo'+str(pro_window))
all_handel = driver.window_handles
print('all_handel'+str(all_handel))
driver.switch_to.window(all_handel[0])

sleep(3)
#driver.get("https://kilid.com/")
#driver.back()
#sleep(3)
#driver.forward()