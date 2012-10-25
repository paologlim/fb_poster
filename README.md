FB poster
=========

A python script for posting stuff on facebook.

How To
------

### Steps:

1. Create a YAML config file. (See configuration part below)
2. Create your links file. Remember to separate the post message and the link with a message separator. (See links file below)
3. Run with python `fb_poster.py <config file path>`.

Configuration
-------------

### Description:

* message_separator - The character used to separate the post message and the link
* user_id           - The fb user id (the group id for a group, or "me" for your profile)
* access_token      - An fb access token with a long expiry duration
* links_file_path   - The absolute file path to the links file

### Sample:

    message_separator: "|"
    user_id:           "206072162773141"
    access_token:      "SOMEVERYLONGACESSTOKENWITHALONGEXPIRYDURATION"
    links_file_path:   "/path/to/links/links.txt"

Links File
----------

You will have to create a file for the messages and links you want to post. This is just a plain text file.

The script posts one item from the file for each run. It will read the first line from the file and post it. If the posting is successful, it removes the line from the file. But if the posting fails, the script "freezes" the content in the file so that no content will be lost.

Each line will be composed of three parts (1) a status message (2) a separator character (3) the link to the file

### Sample:

    This is a cool script!|https://github.com/paologlim/fb_poster
    A badass song|http://tinysong.com/M4xV
    Sleep, sleep, sleep|http://www.dextronet.com/blog/why-you-cant-sleep/

References
----------

* [How to post to an fb group](http://developers.facebook.com/docs/reference/api/group/)
* [How to get an access token with a long expiry duration](http://developers.facebook.com/docs/reference/api/group/)

Todo
----

* Replace os.popen3 with subprocess
* Auto renew access token
