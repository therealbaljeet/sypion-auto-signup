def config():
    BLANK_DATA = {
                    "chromedriver" : "C:\\PATH\\TO\\chromedriver.exe",
                    "profile" : "C:\\PATH\\TO\\Google\\Chrome\\User Data\\Default",
                    "catchall-domain" : "domain.com",
                    "delay" : 15,
                    "swap-headers" : True,
                    "proxy" : False
                }

    #Checking for missing packages
    try:
        import json
        from fake_useragent import UserAgent
        import names
        import selenium
        import random
        from colorama import init
        init()
        from colorama import Fore, Back, Style
        print(Fore.CYAN + "200: All Dependencies Present")

    except Exception:
        print(Fore.RED + "FATAL ERROR: Missing Dependencies")
        return False

    #Checking for config.json
    try:
        with open('config.json', 'r') as f:
            data = json.loads(f.read()) 
        print(Fore.CYAN + "200: Found Config")

    except Exception:
        print(Fore.RED + "400: No Config Found - Creating...")
        with open('config.json', 'w') as f:
            json.dump(BLANK_DATA, f)

        print(Fore.CYAN + "200: Created Config - Enter Settings & Restart")
        return False

    #Validating config.json
    keys = list(data.keys())
    correctKeys = ["chromedriver", "profile", "catchall-domain", "delay", "swap-headers", "proxy"]
    if correctKeys == keys:
        print(Fore.CYAN + "200: Validated Config")
    else:
        print(Fore.RED + "400: Invalid Config - Formatting")
        with open('config.json', 'w') as f:
            json.dump(BLANK_DATA, f)
        print(Fore.CYAN + "200: Formatted Config - Enter Settings & Restart")
        return False
    
    return True