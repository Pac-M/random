__author__ = 'PacMan'

__module_name__ = "torelay"
__module_version__ = "1.0"
__module_description__ = "movie announce relay script"

import hexchat
import re

target = "#target"
allowed = ["#ahd-announce", "#HD-Torrents.Announce", "#bithq", "#gftracker-spam"]

print "script loaded"

def is_movie(word):
    if "movie" in word.lower():
        return True
    else:
        return False

def write_file(string):
    f = open("mylog.txt", "a")
    string += "\n"
    f.write(string)
    f.close()


def return_string(word):
    """
    accepts a string and returns unified output for every channel
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
    name = re.search(r"NEW 4::7 ([A-Za-z0-9 .-]*)\b 4::3 (Movies/X264-HD|Movies/XVID|Movies/X264-SD|Movies/DVDR|Movies/BLURAY) 4::3 (\S*)", word)
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
        string = "%s %s" % (name.group(1), name.group(2))
        write_file(string)
        string = "\00304%s \017%s" % (name.group(1), name.group(2))
        return string
    return word


def echo_cb(word, word_eol, user_data):
    cont = hexchat.get_info("channel")
    source = cont
    if cont in allowed and is_movie(word[1]):
        cont = hexchat.find_context(channel=target)
        reg = return_string(word[1])
        #output = reg + " \037\00304was announced on: " + source
        output = "[" + source + "] " + reg
        cont.command("say %s" % output)

hexchat.hook_print("Channel Message", echo_cb)