import urllib.request, urllib.parse, urllib.error
import re
# fhand = urllib.request.urlopen('https://decodeit.ru/binary')
# fhand = urllib.request.urlopen.urlencode('https://www.onepetro.org/search?q=annual+meeting&peer_reviewed=&published_between=on&from_year=1982&to_year=1982&sort=&rows=500&s2_parent_title=1982+SEG+Annual+Meeting&dc_publisher_facet=&dc_type=')
# fhand = urllib.request.urlopen('https://instructobit.com/tutorial/110/Python-3-urllib:-making-requests-with-GET-or-POST-parameters')
fhand = urllib.request.urlopen('https://nmap.org/movies/')


counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for key, value in counts.items():
    if 'href="' in key:
        print(key, value)

# for line in fhand:
#     print(line.decode().strip())
