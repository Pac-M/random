__author__ = 'Asi'

import re



def print_shit(word):
    name = re.search(r"MOVIE: (.*) (\[\d{4}\]) - (\S*) / (Blu-Ray|WEB-DL) / (\S*).*(x264|h.264 Remux|VC-1 Remux|MPEG2 Remux) /.* - (\b\S*\b)", word)
    if name:
        string = "%s %s %s %s %s %s" % (name.group(1)[:len(name.group(1))-1], name.group(2), name.group(4), name.group(5), name.group(3), name.group(7))
        return string

    



print print_shit("MOVIE: Flandersui gae [2000] - EbP / Blu-Ray / 720p / mkv / x264 / AC-3 - https://awesome-hd.net/torrents.php?id=9438 / https://awesome-hd.net/torrents.php?action=download&id=16885 - ")
print print_shit("MOVIE: La grande bellezza [2013] - PublicHD / Blu-Ray /  / mkv / x264 /  / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=9455 / https://awesome-hd.net/torrents.php?action=download&id=16942 -")
print print_shit("MOVIE: Choke [2008] - KRaLiMaRKo / Blu-Ray / 1080p / mkv / x264 / DTSHD-MA / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=6691")