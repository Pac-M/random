__author__ = 'Asi'

__module_name__ = "torelay"
__module_version__ = "1.0"
__module_description__ = "movie announce relay script"

import hexchat

target = "#target"
allowed = ["#ahd-announce", "#HD-Torrents.Announce", "#bithq", "#gftracker-spam"]

print "script loaded"


def is_movie(word):
    if "movie" in word.lower():
        return True
    else:
        return False

def print_movie(word, channel):


def echo_cb(word, word_eol, user_data):
    cont = hexchat.get_info("channel")
    source = cont
    if cont in allowed and is_movie(word[1]):
        cont = hexchat.find_context(channel=target)
        output = word[1] + " \037\00304was announced on: " + source
        cont.command("say %s" % (output))


hexchat.hook_print("Channel Message", echo_cb)