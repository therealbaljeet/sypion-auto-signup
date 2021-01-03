# sypion-auto-signup
An auto-signup for Sypion AIO. (They give away a key a day to a random person who signs up)

## How to use

### Via source code
First, download the repo locally. 

Next, make sure you have the following installed:

- Python 3.9
- Google Chrome
- Chromedriver (whether for Windows, Mac, or Linux)

**Your Chromedriver MUST match your Chrome Browser version. To do this,
head over ** [here](chrome://version) **on your Chrome browser and find
the version at the top. Then head over ** [here](https://chromedriver.chromium.org/downloads)
** to grab the respective file. Make sure you save the path - you'll 
need it later!**

Then, make sure you have the following Python Modules:

- json
- names
- time
- random
- fake_useragent
- selenium

Open the config.json file and fill out the information. Below is a reference
for what you need to set each value to:


"chromedriver" : ``str`` (the path to your ``chromedriver.exe`` file, use two backslashes)
"profile" : ``str`` (the path to your ``chromedriver.exe`` file, use two backslashes)
"catchall-domain" : ``str`` (the domain where you've setup a catchall email server)
"delay" : ``int`` (how long (seconds) to wait between entries)
"swap-headers" : ``bool`` (whether or not to randomize user agents to avoid detection)
"proxy" : ``bool`` *or* ``list``
    - if False, no proxy will be used
    - if list, each proxy in the list will be used in a rotating fashion
**use http proxies in the form: ** ``ip:port:user:pass``
**Proxies aren't supported yet, might be in a new version.**
**To find your Chrome Profile, go** [here](chrome://version)
**on your Chrome browser and find the** ``Profile Path`` 
**(it's right before the long list of variations).**

*Here is a sample config.json (this won't work for you, fill it out with your own data!)*

{
    "chromedriver" : "C://chromedriver.exe",
    "profile" : "C://Users//sam//AppData//Local//Google//Chrome//User Data//Default",
    "catchall-domain" : "sam.tech",
    "delay" : 15,
    "swap-headers" : true,
    "proxy" : false
}

Then, run the ``main.py`` file.

### Via binary
First, download the binary locally. 

Next, make sure you have the following installed:

- Google Chrome
- Chromedriver (for Windows)

**Your Chromedriver MUST match your Chrome Browser version. To do this,
head over ** [here](chrome://version) **on your Chrome browser and find
the version at the top. Then head over ** [here](https://chromedriver.chromium.org/downloads)
** to grab the respective file. Make sure you save the path - you'll 
need it later!**

Open the config.json file and fill out the information. Below is a reference
for what you need to set each value to:

"chromedriver" : ``str`` (the path to your ``chromedriver.exe`` file, use two backslashes)
"profile" : ``str`` (the path to your ``chromedriver.exe`` file, use two backslashes)
"catchall-domain" : ``str`` (the domain where you've setup a catchall email server)
"delay" : ``int`` (how long (seconds) to wait between entries)
"swap-headers" : ``bool`` (whether or not to randomize user agents to avoid detection)
"proxy" : ``bool`` *or* ``list``
    - if False, no proxy will be used
    - if list, each proxy in the list will be used in a rotating fashion
**use http proxies in the form: ** ``ip:port:user:pass``
**Proxies aren't supported yet, might be in a new version.**
**To find your Chrome Profile, go** [here](chrome://version)
**on your Chrome browser and find the** ``Profile Path`` 
**(it's right before the long list of variations).**

*Here is a sample config.json (this won't work for you, fill it out with your own data!)*

{
    "chromedriver" : "C://chromedriver.exe",
    "profile" : "C://Users//sam//AppData//Local//Google//Chrome//User Data//Default",
    "catchall-domain" : "sam.tech",
    "delay" : 15,
    "swap-headers" : true,
    "proxy" : false
}

Then, run the binary (``.exe``) file.