This simple test framework is written in Python and uses BDD concept with Selenium Webdriver.
Currently it supports only Linux environment.
Required packages are:
- Python >= 3.6
- behave >= 1.2.6
- Selenium >= 3.8.0
You can install those packages from:
- Python [https://www.python.org/downloads/]  
- behave (using 'pip install behave' or [https://behave.readthedocs.io/en/latest/install.html]) 
- Selenium (using 'pip install selenium' or [http://selenium-python.readthedocs.io/installation.html]) (There is no need to download webdrivers)

Besides required software there is no need to configure anything.
Just type: 'behave' in your console, and tests will execute with default parameters.
Framework accepts two optional parameters:
- browser - To choose on which browser to run test. Default is Chrome. Supported options are: 'chrome' and 'firefox'
- timeout - Sets the default time which tests will wait for animation to finish, open of a new window, etc. Default is 10 seconds.
To run tests with those options pass them in command line.
Example usages:
behave -D timeout=5
behave -D browser=firefox
behave -D browser=firefox -D timeout=5 (it is not advised to use timeout below 5 seconds)
