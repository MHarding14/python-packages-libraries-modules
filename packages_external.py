# External packages need to be installed
    # You can find packages in pypi.org
    # Lets look at the package of 'requests'

#Install using pip or your interpreter

import requests
# package for making http requests

sparta_home_page = requests.get('https://www.spartaglobal.com/')

print(sparta_home_page)

print(sparta_home_page.status_code)

print(sparta_home_page.content)

print(sparta_home_page.headers)

