# -*- encoding: utf-8 -*-
#
# File part of "poster.py" script, rename to: config.py
# Author : Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
# License: GPLv3
#
FEED_URL = 'http://blog.programadorlivre.com/feed/'
DBFILE = 'posts.db'
TABLENAME = "posts"
BEGIN_TWITTER_TEXT = "Acompanhe: "
FIXED_TWITTER_TEXT = ""  # At each twitt this will be inserted at end
PAUSE_TIME_FEED_READER = 86400  # Database updater, in seconds
PAUSE_TIME_TWITTER = 3600  # Twitter posts, in seconds
TAG_MAX_LENGTH = 5  # Max size of tag term to post it
TAGS_QTD = 3  # Max number of tags to post
MIN_POST_REPETITION = 5  # Minimal number of post to permit repeat posts
# Twitter Credencials
t_token = ""  # Twitter App Access Token
t_token_key = ""  # Twitter App Access Token Secret
t_con_secret = ""  # Twitter App Consumer Key
t_con_secret_key = ""  # Twitter App Consumer Secret
