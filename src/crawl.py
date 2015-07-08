import sys, re, urllib, random
from utils import stripUrl, buildUrl
from db import getSite, insertNewSite


def cleanLink(link):
    return re.sub('/.*$', '', link)

# checks if a url is a subdomain of an existing domain
# only checks the existing list, so only works for subdomains
#   on the same page
def subdomain(url, domains):
    for domain in domains:
        if domain in url and domain != url:
            #print 'subdomain skipped: ', domain, ' in ', url
            return 1
    for domain in allDomains:
        if domain in url and domain != url:
            #print 'subdomain skipped: ', domain, ' in ', url
            return 1

    return 0    


# returns a random, properly formatted link from the list
def getNewLink(domains):
    # 3 seems to bea deecent number, just based on intuition here.
    if len(domains) > 3:
        print 'getting random domain...'
        url = random.choice(domains)
        domains.remove(url)
        allDomains.remove(url)
        url = 'http://' + url
        return url
    else:
        print 'getting random domain from master list...'
        url = random.choice(allDomains)
        allDomains.remove(url)
        url = 'http://' + url
        return url







if not (len(sys.argv) == 2):
    print "Usage:", sys.argv[0], "www.seedwebsite.com"
    sys.exit()

url = sys.argv[1]

# maintain path so we can backtrack if required
path = []
allDomains = []

while (url):
    
    domains = []
    path.append(url)

    # we only target TLDs for the database
    # initial implementation will skip from TLD to TLD, ignore subpages
    match = re.compile('"(https?://.*?)"')

    try:
        website = urllib.urlopen(url)
    except IOError:
        print 'IOError: ' + url
        url = getNewLink(domains)
        next;

    html = website.read()
    links = re.findall(match, html)

    for link in links:
        link = stripUrl(link)
        # check the url isn't in the database, if not, add it
        # are subdomains more or less common than existing sites?
        if not getSite(link) and not subdomain(link, domains):
            #insertNewSite(link)
            domains.append(link)
      

    # remove duplicates and empty strings
    domains = list(set(domains))
    domains = filter(None, domains)

    print url, len(domains)
    #print domains 

    for domain in domains:
        if domain not in allDomains and not subdomain(domain, allDomains):
            allDomains.append(domain)
    # pick a random(?) new url to check.
    url = getNewLink(domains)