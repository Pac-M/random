__author__ = 'Asi'

import re



def print_shit(word):
    name = re.search("MOVIE: ([A-Za-z \d]+)\[(\d+)] - (\w+).*(Blu-Ray|WEB-DL).*(720p|1080p) / (\w+) / (\w+)", word)
    if name:
        string = "%s %s %s %s %s %s" % (name.group(1), name.group(2), name.group(4), name.group(5), name.group(7), name.group(3))
        print string
        return
    name = re.search("New Torrent by .* \[Movie/(Remux|Blu-Ray|720p|1080p/i)] (.*)(\d{4}) (720p|1080p).*- ?([a-zA-Z0-9]*)", word)
    if name:
        string = "%s %s %s %s %s" % (name.group(2), name.group(3), name.group(1), name.group(4), name.group(5))
        print string
        return
    print word


print print_shit("New Torrent by dragon80 [Movie/Remux] The Place Promised in Our Early Days 2004 1080p JPN Bluray Remux AVC LPCM - BluDragon (19.93 GB) uploaded! Download: https://hdts.ru/download.php?id=7a2b411cd5d9cdab9862f27e52e024cf19217614")
print print_shit("MOVIE: Flandersui gae [2000] - EbP / Blu-Ray / 720p / mkv / x264 / AC-3 - https://awesome-hd.net/torrents.php?id=9438 / https://awesome-hd.net/torrents.php?action=download&id=16885 - ")