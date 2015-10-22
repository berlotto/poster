#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# "poster.py" script - See README.MD for more information
# Author : Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
# License: GPLv3
#
import feedparser
import dataset
from twitter import *
import time
import multiprocessing
import random
import sys
from config import *

# ========================= DO NOT CHANGE AFTER HERE ==========================


def get_last_id(db):
    result = db.query('SELECT MAX(id) id FROM {table}'.format(table=TABLENAME))
    for row in result:
        if row['id']:
            return int(row['id']) + 1
        else:
            return 1


def do_db_update():
    #
    # Conenct to the simple database
    #
    db = dataset.connect('sqlite:///%s' % DBFILE)
    table = db[TABLENAME]

    while True:
        print("Update DB: Working...")
        #
        # get latest id from table + one
        #
        last_id = get_last_id(db)
        #
        # get the feed data from the url
        #
        feed = feedparser.parse(FEED_URL)

        for post in feed.entries:
            # if post is already in the database, skip it
            post_url = post.links[0]['href']
            already = table.find_one(url=post_url)
            if not already:
                title = post.title
                tags = ','.join([t['term'] for t in post.tags])

                table.insert({
                    "id": last_id,
                    "title": title,
                    "url": post_url,
                    "tags": tags,
                    })
                last_id += 1
        print("Update DB: Sleeping...")
        time.sleep(PAUSE_TIME_FEED_READER)


def do_post_twitter():
    print("PostTwitter: Begin")
    repetition = []
    #
    # Connect to twitter with the credencials
    #
    t = Twitter(
        auth=OAuth(t_token, t_token_key, t_con_secret, t_con_secret_key)
    )
    #
    # Connect to the database
    #
    db = dataset.connect('sqlite:///%s' % DBFILE)
    table = db[TABLENAME]
    #
    # Read a randomized line of table and post it to Twitter
    #
    while True:
        print("PostTwitter: Working...")
        #
        # Read the last id from the table
        #
        last_id = get_last_id(db)
        print("LastId:", last_id)
        #
        # Select randomly one post from database
        #
        rand_id = 0
        while True:
            rand_id = random.randint(1, last_id)
            if rand_id not in repetition:
                break
        # Control to not repeat the last MIN_POST_REPETITION ids of posts
        repetition.insert(0, rand_id)
        if len(repetition) > MIN_POST_REPETITION:
            repetition.pop()
        #
        post = table.find_one(id=rand_id)
        if post:
            post['begin'] = BEGIN_TWITTER_TEXT
            post['fixed'] = FIXED_TWITTER_TEXT
            print("Posting:", post['title'])
            try:
                post_text = "{begin}{title}, em: {url}{fixed}".format(
                    **dict(post)
                )
                tagct = 0
                for tag in post['tags'].split(","):
                    if not tagct >= TAGS_QTD:
                        if len(tag) <= TAG_MAX_LENGTH:
                            post_text += "#{tag} ".format(tag=tag)
                            tagct += 1
                t.statuses.update(status=post_text)
            except Exception as e:
                print("ERRO:", e)

            print("PostTwitter: Sleeping...")
            time.sleep(PAUSE_TIME_TWITTER)


def main():
    #
    # Start the Threads to update database and to post on social networks
    #

    DO_ALL = True
    DO_UPDATE = False
    DO_POST = False
    if len(sys.argv) > 1 and sys.argv[1] in ("all", "update", "post"):
        arg = sys.argv[1]
        DO_ALL = arg == "all"
        DO_UPDATE = arg == "update"
        DO_POST = arg == "post"

    if DO_ALL or DO_UPDATE:
        p_db = multiprocessing.Process(target=do_db_update, args=())
        p_db.start()

    if DO_ALL or DO_POST:
        p_tw = multiprocessing.Process(target=do_post_twitter, args=())
        p_tw.start()

if __name__ == '__main__':
    main()
