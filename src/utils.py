import re

# misc. utility functions

# checks url has the correct syntax
# http://www.website.com.nl/robots.txt
def buildUrl(url):
    if not re.search('www\.', url):
        url = 'www.' + url
    if not re.search('http://', url):
        url = 'http://' + url
    url = url + '/robots.txt'
    return url


# breaks a url down
# removes http:// and www and /*
def stripUrl(url):
    url = re.sub('^http://', '', url)
    url = re.sub('^https://', '', url)
    url = re.sub('^www\.', '', url)
    url = re.sub('#.*', '', url)
    url = re.sub('\?.*', '', url)
    # remove slash and anything after it
    url = re.sub('\/.*$', '', url)
    return url

