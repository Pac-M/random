__author__ = 'Asi'

import re
from time import sleep

def clear_log():
    open('mylog.txt', 'w').close()

def write_file(string):
    f = open("mylog.txt", "a")
    string = string + "\n"
    f.write(string)
    f.close()


def return_string(word):
    """
    accepts a string and return unified output for every channel
    """
    #AHD
    name = re.search(
        r"MOVIE: (.*) \[(\d{4})\] - (\S*) / (Blu-Ray|WEB-DL) / (\S*).*(x264|h.264 Remux|VC-1 Remux|MPEG2 Remux) /.* - (\b\S*\b)",
        word)
    if name:
        string = '{0:s} \017{1:s} {2:s} {3:s} {4:s} {5:s}'.format(name.group(1), name.group(2),
                                                              name.group(4), name.group(5), name.group(3),
                                                              name.group(7))
        write_file(string)
        string = '\00304{0:s} \017{1:s} {2:s} {3:s} {4:s} {5:s}'.format(name.group(1), name.group(2),
                                                              name.group(4), name.group(5), name.group(3),
                                                              name.group(7))
        return string
    #HDT
    name = re.search(
        r"New Torrent by .* \[Movie/(Remux|Blu-Ray|720p|1080p/i)] (.*)\(?(\d{4})\)? [A-Z a-z0-9-]*[- ]([a-zA-Z0-9]*)\b .*(http.*)",
        word)
    if name:#HD-T
        string = "%s %s %s %s %s" % (name.group(2), name.group(3), name.group(1), name.group(4), name.group(5))
        write_file(string)
        string = "\00304%s \017%s %s %s %s" % (name.group(2), name.group(3), name.group(1), name.group(4), name.group(5))
        return string
    #GFT
    name = re.search(r"NEW :: ([A-Za-z0-9 .-]*)\b :: (Movies/X264-HD|Movies/XVID) :: (\S*)\b", word)
    if name: #gft
        string = "%s %s" % (name.group(1), name.group(3))
        write_file(string)
        string = "\00304%s \017%s" % (name.group(1), name.group(3))
        return string
    #BitHQ
    name = re.search(r"(DVD-R/Movies|DVD-R/Asian Cinema|High Quality) - (.*) \((\d{4})\) ([a-zA-Z0-9 /]+\b)  - (.*)",
                     word)
    if name:
        string = "%s %s %s %s" % (name.group(2), name.group(3), name.group(4), name.group(5))
        write_file(string)
        string = "\00304%s \017%s %s %s" % (name.group(2), name.group(3), name.group(4), name.group(5))
        return string
    #TSH
    name = re.search(r"Movies/\S* :: (.*) :: (http\S*)", word)
    if name:
        string = "\00304%s \017%s" % (name.group(1), name.group(2))
        write_file(string)
        string = "\00304%s \017%s" % (name.group(1), name.group(2))
        return string
    return word


clear_log()


print return_string(
    "New Torrent by tearofthesun [Movie/1080p/i] Midsummer&#039;s Equation 2013 720p BluRay x264-WiKi (5.51 GB) uploaded! Download: https://hdts.ru/download.php?id=b14873b90363b1b192524bf339adfccc8860d2a2")
print return_string(
    "MOVIE: Flandersui gae [2000] - EbP / Blu-Ray / 720p / mkv / x264 / AC-3 - https://awesome-hd.net/torrents.php?id=9438 / https://awesome-hd.net/torrents.php?action=download&id=16885 - ")
print return_string(
    "MOVIE: La grande bellezza [2013] - PublicHD / Blu-Ray /  / mkv / x264 /  / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=9455 / https://awesome-hd.net/torrents.php?action=download&id=16942 -")
print return_string(
    "MOVIE: Choke [2008] - KRaLiMaRKo / Blu-Ray / 1080p / mkv / x264 / DTSHD-MA / AHD Gold / DXVA - https://awesome-hd.net/torrents.php?id=6691")