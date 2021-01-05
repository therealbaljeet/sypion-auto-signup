# sypion-auto-signup
An auto-signup for Sypion AIO. (They give away a key a day to a random person who signs up, at least they say they do)

## How to use

### Via source code
First, download the repo locally. 

Next, make sure you have the following installed:

- Python 3.9
- Google Chrome
- Chromedriver (whether for Windows, Mac, or Linux)

**Your Chromedriver MUST match your Chrome Browser version. To do this, head over here: chrome://version** 
**on your Chrome browser and find the version at the top. Then head over** [here](https://chromedriver.chromium.org/downloads)
**to grab the respective file. Make sure you save the path - you'll need it later!**

Then, make sure you have the following Python Modules:

- json
- names
- datetime
- random
- fake_useragent
- selenium

Run the ``main.py`` file. On first use, it will create a ``log.json`` in the same directory as ``main.py``.\
\

It will ask for 2 things to setup the program:
- ``catchall`` : your catchall domain [see this for help](https://www.namecheap.com/support/knowledgebase/article.aspx/310/2214/how-to-set-up-a-catchall-wildcard-email-address/)
- ``path`` - your Chromedriver Path (eg. *C:/Chromedriver.exe*)
This will be stored under the settings key in ``log.json``, so you can just start the program after inital setup.
**Note the headless option has been commented out in the driver() method. This is because there are issues with the site in headless mode. Feel free to uncomment this out, it just might not work!**

### Via binary
First, download the binary locally. 

Next, make sure you have the following installed:

- Google Chrome
- Chromedriver (for Windows)

**Your Chromedriver MUST match your Chrome Browser version. To do this, head over here: chrome://version** 
**on your Chrome browser and find the version at the top. Then head over** [here](https://chromedriver.chromium.org/downloads)
**to grab the respective file. Make sure you save the path - you'll need it later!**

Run the binary (``.exe``) file. On first use, it will create a ``log.json`` in the same directory as ``main.py``.\
\
It will ask for 2 things to setup the program:
- ``catchall`` : your catchall domain [see this for help](https://www.namecheap.com/support/knowledgebase/article.aspx/310/2214/how-to-set-up-a-catchall-wildcard-email-address/)
- ``path`` - your Chromedriver Path (eg. *C:/Chromedriver.exe*)
This will be stored under the settings key in ``log.json``, so you can just start the program after inital setup.