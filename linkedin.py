from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome("C:/Users/Onur/Desktop/webscraping/chromedriver.exe")
browser.get("https://www.linkedin.com/home")

browser.fullscreen_window()
time.sleep(5)
login =  browser.find_element(By.XPATH,"/html/body/nav/div/a[2]")
login.click()
time.sleep(5)

email = browser.find_element(By.XPATH,"//*[@id='username']")
password= browser.find_element(By.XPATH,"//*[@id='password']")

email.send_keys("#linkedin mailini gir.#")
password.send_keys("Linkedin şifreni gir.")

login_button= browser.find_element(By.CSS_SELECTOR,"#organic-div > form > div.login__form_action_container > button")
login_button.click()
time.sleep(5)
search_bar = browser.find_element(By.XPATH,"//*[@id='global-nav-typeahead']/input")
search_bar.send_keys("#python")
search_bar.send_keys(Keys.RETURN)
time.sleep(10)

contacts = browser.find_elements(By.CSS_SELECTOR,".app-aware-link.global-nav__primary-link")[1]
contacts.click()
time.sleep(5)

contact_button=browser.find_element(By.CLASS_NAME,"mn-community-summary__entity-info")
contact_button.click()
time.sleep(5)

for i in range(1,3):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') #java kodu scroll yapıyor sayfayı aşağı çekerek aşağıdaki bilgileri getiriyor.
    time.sleep(3)

followers = browser.find_elements(By.CLASS_NAME,"mn-connection-card__details")  #bütün elemanları almak için elements kullandık.
fallowerList=[]
for follower in followers:
    fallowerList.append(follower.text) 

with open ("follower.txt","w",encoding= "UTF-8") as file:
    for follower in fallowerList:
        file.write(follower+"/n")
time.sleep(5)

browser.quit()


