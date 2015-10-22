# -*- encoding: utf-8 -*-
#
# File part of "poster.py" script
# Author : Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
# License: MIT
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
t_token = "22940852-t0uDvyXlcx2eJqXZFM6c45DFDnseJwlri5oS8YhMF"
t_token_key = "tpFtD4EvWBcA0EApHZpgl5WE37cCY8NdZRvQQyySO1P7C"
t_con_secret = "qwVuKTU02AdsLS7tJWznIIUQX"
t_con_secret_key = "fbGV2RkJwrfWGJcxZLzNffwRh0hBfPMFbAMgC2HjqmlYVNBGqc"
