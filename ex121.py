#   http://py4e-data.dr-chuck.net/comments_42.html

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
url = 'http://py4e-data.dr-chuck.net/comments_42.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)
tags = soup('a')
for tag in tags:
    print(tag.get("comments", None))


# for line in soup:
#     print(line)
    # words = line.decode().split()

    # for word in words:
        # counts[word] = counts.get(word, 0) + 1

# for key, value in counts.items():
#     if 'href="' in key:
#         print(key, value)
