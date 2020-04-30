#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = "https://genarod.github.io/blog"
SITELOGO = SITEURL + "/images/genaro-639x639.png"
AUTHOR = "Genaro Díaz"
SITENAME = "La esquina de Genaro"
SITETITLE = "Blog de Genaro"
SITESUBTITLE = "Agile Project Manager"
SITEDESCRIPTION = "Lo que le pasa por la cabeza a Genaro"
# FAVICON = SITEURL + "/images/favicon.ico"

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
ROBOTS = "index, follow"

COPYRIGHT_YEAR = 2020
MAIN_MENU = True
MENUITEMS = (('Archivo', '/blog/archives'),
             ('Categorías', '/blog/categories'),
             ('Tags', '/blog/tags'))

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

# Default theme language.
I18N_TEMPLATES_LANG = "es"

# Your language.
DEFAULT_LANG = "es_ES"

# Match languages for other configs.
OG_LOCALE = "es_ES"
LOCALE = ("es_ES", "es_ES.utf8")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/genarodiaz'),
          ('github', 'https://github.com/genarod'),
          ('rss', '/feeds/all.atom.xml'),
          ('linkedin', 'https://www.linkedin.com/in/genaro-diaz-20b37926/'))

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 175

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/Flex'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
