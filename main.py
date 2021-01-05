import names
import time
import datetime
import json
from random import randint
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Inits or Validates log.json
def getLog():
    try:

        with open('log.json', 'r') as f:
            return True

    except Exception:

        with open('log.json', 'a') as f:
            data = {}
            json.dump(data, f)

        return True

#Getting caps set up
getLog()

with open('log.json', 'r') as f:
    data = json.loads(f.read())

try:
    CATCHALL = data['settings']['catchall']
    PATH = data['settings']['path']

except Exception:
    CATCHALL = input("Enter your catchall domain name: ")
    PATH = input("Enter your Chromedriver Path: ")

    data['settings'] = {'catchall' : CATCHALL, 'path' : PATH}

    with open('log.json', 'w') as f:
        json.dump(data, f)      

#Returns a configed browser w/ custom agent
def driver():

    #Setting options
    options = Options()
    #options.add_argument("--headless")

    #Generating + adding random user agent
    ua = UserAgent()
    user_agent = ua.random 
    options.add_argument(f'user-agent={user_agent}')

    options.add_argument("start-maximized")
    options.add_argument('--log-level=3')
    options.add_argument("--window-size=450,650")
    options.add_argument("--app=https://sypion.com/#signup")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(PATH, options = options)

    return browser

#Returns randomized delay
def delay():
    return randint(1,50)/randint(50,100)

#Main process
def start():
    
    if getLog(): #makes sure logfile exists

        while True: 

            browser = driver() #Gets browser object

            try:
                time.sleep(delay())

                email = browser.find_element_by_id('MERGE0')
                email.click()

                time.sleep(delay())

                #Generating unique email address
                name = names.get_full_name().split(' ')
                number = randint(1990,2021)
                address = f'{name[1]}.{name[0]}{number}@{CATCHALL}'.lower()

                #Entering + submitting address
                email.send_keys(address)

                time.sleep(delay())

                submit = browser.find_element_by_xpath('//*[@id="signup"]/div[1]/div/div/div/div/form/button')
                submit.click()

                time.sleep(delay())

                #Waiting for redirect to clear
                while browser.current_url != 'https://sypion.us20.list-manage.com/subscribe/post':
                    pass
                
                #Getting information for log file + writing to log file
                user_agent = browser.execute_script("return navigator.userAgent;")

                with open('log.json') as f:
                    data = json.loads(f.read())
                
                data[str(address)] = {
                    'agent' : user_agent,
                    'status' : 200,
                    'timestamp' : str(datetime.datetime.now())
                }

                with open('log.json', 'w') as f:
                    json.dump(data, f)
            except Exception as E:
                time.sleep(delay())

            #terminating browser
            browser.quit()

#Starting program
start()