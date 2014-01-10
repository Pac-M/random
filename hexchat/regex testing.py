__author__ = 'Asi'

import re

name = re.search("MOVIE: ([A-Za-z \d]+)(\[\d+]).*(720p|1080p) / (\w+) / (\w+)", 'MOVIE: BBS xiang min de zheng yi [2012] - HDWinG / Blu-Ray / 720p / mkv / x264 / DTS / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=9437 / https://awesome-hd.net/torrents.php?action=download&id=16882 - ')

if name:
    #print ("%s %s was released in the following format: %s %s" % name.group(1), name.group(2), name.group(2), name.group(3))
    print "%s%s%s%s" % (name.group(1), name.group(2), name.group(3), name.group(4))



#print print_movie("","ahd-announce")