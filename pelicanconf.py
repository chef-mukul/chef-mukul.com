#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'chef-mukul'
SITENAME = u'chef-mukul'
SITESUBTITLE = u'Programming Stuff'
SITEURL = 'https://chef-mukul.com'
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

#MENUITEMS = LINKS

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS  = ['images',]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TYPOGRIFY  = True
THEME = "./pelican-themes/pelican-octopress-theme"
#TWITTER_USERNAME='_serafeim_'
#TWITTER_TWEET_BUTTON=True
#GOOGLE_ANALYTICS='UA-44750952-1'
#GOOGLE_UNIVERSAL_ANALYTICS='UA-44750952-1'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    #'a-plugin',
    'sitemap',
    #'pelican_jsfiddle',
    #'ipynb.markup',
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

MARKUP = ('rst', 'md', 'ipynb', )
#MARKUP = ('rst', 'md', )
IGNORE_FILES = ['.ipynb_checkpoints']