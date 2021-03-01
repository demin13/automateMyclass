from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
from time import sleep


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=".chromedriver.exe")
    
    try:
        driver.get("https://myclass.lpu.in")
        driver.find_element_by_name("i").send_keys("11803983")
        password = driver.find_element_by_name("p").send_keys("@Deminshekhar4321");
        driver.find_element_by_tag_name("button").click()
        driver.find_element_by_link_text("View Classes/Meetings").click()
        #driver.find_element_by_class_name("fc-icon-chevron-right").click()
        #wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='9:00 - 10:00']"))).click()
        st = 'INT332'
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@title,'{}')]".format(st)))).click()
        #driver.find_element_by_xpath('//a[contains(@href,"href")]')
        driver.find_element_by_link_text("Join").click()
        #wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Listen only']"))).click()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Listen only')]"))).click()
        driver.switch_to.default_content()
        #wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label,'Users and messages toggle')]"))).click()
        #wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Public Chat')]"))).click()
        #driver.find_element_by_id("message-input").send_keys("Good Afternoon Sir")
        #wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Send message')]"))).click()
        
        #driver.find_element_by_tag_name("button").click()
        
    except Exception as e:
        print(e)
    
