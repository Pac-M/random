__author__ = 'Asi'

import re

name = re.search("MOVIE: ([A-Za-z \d]+)(\[\d+]).*(720p|1080p) / (\w+) / (\w+)", 'MOVIE: BBS xiang min de zheng yi [2012] - HDWinG / Blu-Ray / 720p / mkv / x264 / DTS / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=9437 / https://awesome-hd.net/torrents.php?action=download&id=16882 - ')
test = re.search("\d*", "123")

if test:
    print test.groups(0)
if name:
    print name.groups()



#print print_movie("","ahd-announce")