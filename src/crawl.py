import sys, re, urllib
from utils import stripUrl


def cleanLink(link):
    return re.sub('/.*$', '', link)




if not (len(sys.argv) == 2):
    print "Usage:", sys.argv[0], "www.seedwebsite.com"
    sys.exit()

url = sys.argv[1]

# we only target TLDs for the database
# initial implementation will skip from TLD to TLD, ignore subpages
match = re.compile('"(https?://.*?)"')

website = urllib.urlopen(url)
html = website.read()
links = re.findall(match, html)

for link in links:
    link = stripUrl(link)
    print link

# check the url isn't in the database


# add url to the database

# pick a random(?) new url to check.

