global browser, PATH, PROFILE, DOMAIN, DELAY, HEADERS, PROXY
browser = "None"
PATH = None
PROFILE = None
DOMAIN = None
DELAY = None
HEADERS = None
PROXY = None

try:
    import setup
    import json
    import names
    import time
    from random import randint
    from fake_useragent import UserAgent
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import InvalidSelectorException
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys

except Exception:
    print("Invalid Formatting, Quitting...")
    quit()

if setup.config() == False:
    print("Quitting...")
    quit()

def browser():
    options = Options()
    options.add_argument("--headless")
    if PROFILE:
        dirPath = "user-data-dir=" + PROFILE
        options.add_argument(dirPath)
    ua = UserAgent()
    user_agent = ua.random 
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("start-maximized")
    options.add_argument('--log-level=3')
    options.add_experimental_option("detach", True)
    options.add_argument("--app=https://www.google.com")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(PATH, chrome_options = options)
    return browser

def settings():
    with open('config.json', 'r') as f:
        data = json.loads(f.read())
    
    PATH = data['chromedriver']
    
    try:
        PROFILE = data['profile']
    except Exception:
        pass

    DOMAIN = data['catchall-domain']
    DELAY = data['delay']
    HEADERS = data['swap-headers']
    PROXY = data['proxy']

def main():
    settings()
    while True:
        driver = browser()
        driver.get('https://sypion.com/#signup')
        email = driver.find_element_by_xpath('//*[@id="MERGE0"]')
        email.click()
        name = names.get_full_name().split(' ')
        number = randint(1990,2021)
        address = f"{name[1]}.{name[0]}{number}@{DOMAIN}"
        email.send_keys(address)
        submit = driver.find_element_by_xpath('//*[@id="signup"]/div[1]/div/div/div/div/form/button')
        submit.click()
        while driver.current_url != "https://sypion.us20.list-manage.com/subscribe/post":
            pass
        time.sleep(DELAY)
        driver.quit()

main()