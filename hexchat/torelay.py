__author__ = 'Asi'

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

def return_string(word):
    name = re.search("MOVIE: ([A-Za-z \d]+)\[(\d+)] - (\w+).*(Blu-Ray|WEB-DL).*(720p|1080p) / (\w+) / (\w+)", word)
    if name:
        string = "%s %s %s %s %s %s" % (name.group(1), name.group(2), name.group(4), name.group(5), name.group(7), name.group(3))
        return string
    name = re.search("New Torrent by .* \[Movie/(Remux|Blu-Ray|720p|1080p/i)] (.*)(\d{4}) (720p|1080p).*- ?([a-zA-Z0-9]*)", word)
    if name:
        string = "%s %s %s %s %s" % (name.group(2), name.group(3), name.group(1), name.group(4), name.group(5))
        return string
    return word



def echo_cb(word, word_eol, user_data):
    cont = hexchat.get_info("channel")
    source = cont
    if cont in allowed and is_movie(word[1]):
        cont = hexchat.find_context(channel=target)
        reg = return_string(word[1])
        output = reg + " \037\00304was announced on: " + source
        cont.command("say %s" % (output))


hexchat.hook_print("Channel Message", echo_cb)