from db import insertRobots

import requests
import re


# script to append /robots.txt to a url and save it to a database
def getRobotstxt(url):
    
    # should perform check here to ensure url is correct syntax

    robotsUrl = buildUrl(url)
    robots = requests.get(robotsUrl).content
    insertRobots(url, robots)


# checks url has the correct syntax
def buildUrl(url):
    if not re.search('http://', url):
        url = 'http://' + url
    url = url + '/robots.txt'
    return url


getRobotstxt('www.google.com')
