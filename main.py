from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pickle
import datetime
from time import sleep


def get_credentials():
   
    if not path.exists("credentials.p"):
        username = "11803983"
        password = "#Deminshekhar4321"
        
        pickle.dump({'username': username, 'password': password},
                    open("credentials.p", "wb"))
        return username, password
    credentials = pickle.load(open("credentials.p", "rb"))
    return credentials['username'], credentials['password']


def get_time_table(driver, username, password):
    

    def extract_time_table():
        driver.get("https://ums.lpu.in/lpuums/")
        driver.find_element_by_class_name("input_type").send_keys(username)
        driver.find_element_by_class_name("login_box").click()
        sleep(3)
        driver.find_element_by_class_name(
            "input_type_pass").send_keys(password)
        Select(driver.find_element_by_id(
            "ddlStartWith")).select_by_index(1)
        driver.find_element_by_id("iBtnLogins").click()
        table = driver.find_element_by_class_name("table-hover")
        rows = table.find_elements_by_tag_name("tr")
        time_table = {}
        for row in rows:
            _data = row.find_elements_by_tag_name("td")
            time, course = _data[0].text, _data[1].text
            time_table[time] = course

        time_table['date'] = datetime.date.today()
        pickle.dump(time_table, open("timetable.p", "wb"))
        return time_table

    if path.exists("timetable.p"):
        time_table = pickle.load(open("timetable.p", "rb"))
        if time_table['date'] == datetime.date.today():
            return time_table
    return extract_time_table()


def get_current_class(time_table):
    #print("Getting current class...")
    now = datetime.datetime.now()
    hour = now.hour
    if hour != 12:
        hour = hour % 12
    for time, course in time_table.items():
        if time != "date":
            if int(time[:2]) < hour+0.5 < int(time[3:5]):
                #print(f"\nCURRENT CLASS: {course} {(time)}\n")
                return course

def getclass():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    try:
        username, password = get_credentials()
        time_table = get_time_table(driver, username, password)
        course = get_current_class(time_table)
        print(course)
        #return course
        
    except Exception as e:
        print(e)
    finally:
        driver.close()
getclass()
