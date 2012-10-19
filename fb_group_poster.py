# TODO
# - Put in Github
# - Replace os.popen3 with subprocess
# - Auto renew access token
#
# HOWTO
#
# Steps:
# 1. Create a config file in project directory named fb_group_poster.yml
#    (See config part below)
# 2. Create your links file. Remember to separate the post message and the
#    link with a message separator.
# 3. Run with python fb_group_poster.py or put in cron.
#
# CONFIG
#
# Description:
#
# message_separator: The character used to separate the post message
#                    and the link
# group_id:          The fb group id
# access_token:      An fb access token with a long expiry duration
# links_file_path:   The absolute file path to the links file
#
# Sample:
#
# message_separator: "|"
# group_id:          "206072162773141"
# access_token:      "SOMEVERYLONGACESSTOKENWITHALONGEXPIRYDURATION"
# links_file_path:   "/path/to/links/links.txt"
#
# REFERENCES
#
# - How to post to an fb group:
#   http://developers.facebook.com/docs/reference/api/group/
# - How to get an access token with a long expiry duration:
#   https://developers.facebook.com/roadmap/offline-access-removal/#extend_token
# - How to run stuff with cron:
#   https://help.ubuntu.com/community/CronHowto

import os
import yaml

def get_message(links_file, message_separator):
    print "-- Getting message"
    link_line = links_file.readline().strip()

    if len(link_line) > 0:
        return link_line.split(message_separator)

def post_message(message, group_url, access_token):
    print "-- Posting message: %s (%s)" % (message[0], message[1])
    command_string = "curl \"%s?access_token=%s\" -d message=\"%s\" -d link=%s" % (group_url, access_token, message[0], message[1])

    return os.popen3(command_string)

def remove_posted_message(links_file):
    print "-- Removing posted message"
    new_content = links_file.read()
    links_file.seek(0)
    links_file.write(new_content)
    links_file.truncate()

def posting_succeeded(result):
    output = result[1].readlines()
    error = None

    if len(output) == 0:
        error = result[2].readlines()[0]
    elif output[0].count("error") > 0:
        error = output[0]

    if not error:
        print "-- Posting succeeded!"
        return True
    else:
        print "-- Posting failed: %s" % error
        return False

def freeze_file_content(links_file):
    links_file.seek(0)
    new_content = "\n" + links_file.read()
    links_file.seek(0)
    links_file.write(new_content)

def load_config(file_path):
    config_file = open(file_path)
    config = yaml.load(config_file)
    config_file.close()

    return config

def main():
    config_file_path = "fb_group_poster.yml"
    config = load_config(config_file_path)

    message_separator = config['message_separator']
    group_url         = "https://graph.facebook.com/%s/feed" % config['group_id']
    access_token      = config['access_token']
    links_file_path   = config['links_file_path']
    links_file        = open(links_file_path, 'r+')

    print "Running FB group poster!"
    message = get_message(links_file, message_separator)
    if message != None:
        result = post_message(message, group_url, access_token)
        if posting_succeeded(result):
            remove_posted_message(links_file)
        else:
            freeze_file_content(links_file)
    else:
        print "-- No links to post today"

    links_file.close()

main()
