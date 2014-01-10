__author__ = 'Asi'

__module_name__ = "torelay"
__module_version__ = "1.0"
__module_description__ = "movie announce relay script"

#import hexchat
import re

target = "#target"
allowed = ["#ahd-announce", "#HD-Torrents.Announce", "#bithq", "#gftracker-spam"]

print "script loaded"


def is_movie(word):
    if "movie" in word.lower():
        return True
    else:
        return False

def return_string(word, channel):
    name = re.search("MOVIE: ([A-Za-z \d]+)(\[\d+]).*(720p|1080p) / (\w+) / (\w+)", word)
    if name:
        string = "%s %s %s %s %s" % (name.group(1), name.group(2), name.group(3), name.group(4), name.group(5))
        return string
    name =




def echo_cb(word, word_eol, user_data):
    cont = hexchat.get_info("channel")
    source = cont
    if cont in allowed and is_movie(word[1]):
        cont = hexchat.find_context(channel=target)
        output = word[1] + " \037\00304was announced on: " + source
        cont.command("say %s" % (output))


hexchat.hook_print("Channel Message", echo_cb)