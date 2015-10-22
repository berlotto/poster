POSTER
======

This program is a Twitter poster. This will retrieve all information from a
rss feed that you configure and then will post at your twitter timeline
as long time you set.

The Code
--------

In the code have 2 big processes:

1. The process that retrieve and store in a simple SQLite3 database the data
from rss feed

2. The process that read from database a random data and post it in the Twitter

This two processes run as threads in the system, so we can determine different
times do be the actions, precisely becouse read the feed of the site and post
the links on the twitter not be performed at the same time.

Configuration
-------------

This program need to be configured in the `"config.py"` file. This is the
options:

<table>
<tr><td>FEED_URL</td><td>The feed URL</td></tr>
<tr><td>DBFILE</td><td>The name of the database file</td></tr>
<tr><td>TABLENAME</td><td>The name of the table in the database</td></tr>
<tr><td>BEGIN_TWITTER_TEXT</td><td>A text that will be posted at BEGIN of twitt</td></tr>
<tr><td>FIXED_TWITTER_TEXT</td><td>A text that will be posted at END of twitt</td></tr>
<tr><td>PAUSE_TIME_FEED_READER</td><td>Time of the database updater will run, in seconds</td></tr>
<tr><td>PAUSE_TIME_TWITTER</td><td>Time of the twitter posts will be posted, in seconds</td></tr>
<tr><td>TAG_MAX_LENGTH</td><td>Max size of tag term to post it, tags given from RSS</td></tr>
<tr><td>TAGS_QTD</td><td>Max number of tags to post in twitt</td></tr>
<tr><td>MIN_POST_REPETITION</td><td>Minimal number of posts to permit repeat posts</td></tr>
<tr><td colspan=2>Twitter app configuration (http://apps.twitter.com)</td></tr>
<tr><td>t_token</td><td>Access token</td></tr>
<tr><td>t_token_key</td><td>Access Token Secret</td></tr>
<tr><td>t_con_secret</td><td>Consumer Key</td></tr>
<tr><td>t_con_secret_key</td><td>Consumer Secret</td></tr>
</table>

Run information
----------------

Libs:

- feedparser - https://feedparser.readthedocs.org
- dataset - https://dataset.readthedocs.org
- twitter - https://pypi.python.org/pypi/twitter
- multiprocessing - https://pymotw.com/2/multiprocessing/

Python version: 3.4.3

You can run this script with only one of the partes running:

    $ python poster.py [all|update|post]

License
-------

This code is licensed under the GPLv3, like you can read in the `license.txt`
or in this url: http://www.gnu.org/licenses/gpl-3.0-standalone.html

Author
------

Sérgio Berlotto Jr <sergio.berlotto@gmail.com>
