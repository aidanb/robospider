from db import insertNewSite, getDateCrawled


# utility script to insert starter list from a text file.

with open('list.txt') as f:
    for line in f:
        url = line.strip().translate(None, '/')
        print url
