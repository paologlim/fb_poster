FB poster
=========

A python script for posting stuff on facebook.

How To
------

### Steps:

1. Create a config file in project directory named fb_poster.yml. (See config part below)
2. Create your links file. Remember to separate the post message and the link with a message separator.
3. Run with python fb_poster.py or put in cron.

Configuration
-------------

### Description:

* message_separator - The character used to separate the post message and the link
* group_id          - The fb group id
* access_token      - An fb access token with a long expiry duration
* links_file_path   - The absolute file path to the links file

### Sample:

    message_separator: "|"
    group_id:          "206072162773141"
    access_token:      "SOMEVERYLONGACESSTOKENWITHALONGEXPIRYDURATION"
    links_file_path:   "/path/to/links/links.txt"

References
----------

* [How to post to an fb group](http://developers.facebook.com/docs/reference/api/group/)
* [How to get an access token with a long expiry duration](http://developers.facebook.com/docs/reference/api/group/)
* [How to run stuff with cron](https://help.ubuntu.com/community/CronHowto)

Todo
----

* Replace os.popen3 with subprocess
* Auto renew access token
