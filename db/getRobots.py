from db import insertRobots, getDateCrawled, getOneUnchecked
from utils import buildUrl

import requests
import re


# script to append /robots.txt to a url and save it to a database
# urls here come from ther database so no need to check if they exist in db.
def getRobotstxt(url):
    print url,
    # check that the site has not been crawled yet
    if not (getDateCrawled(url)[0]):
        robotsUrl = buildUrl(url)
        req = requests.get(robotsUrl, timeout=30)
        if req.status_code == 200:
            robots = req.content
        else:
            robots = None
        
        insertRobots(url, robots)
        print url, " robots.txt grabbed"
        print robots
    else:
        print " already crawled"

# get an an entry from the db which has not been checked yet.
# naive version, we are at the mercy of mysql's LIMIT 1, so default order is by id field.
# result is a FIFO lookup system.


url = getOneUnchecked()

while (url is not None):
    print 'Checking ', url
    getRobotstxt(url)
    print "Next..."
    url = getOneUnchecked()
print "All done, no unchecked sites left"
