from __future__ import unicode_literals
import os
import sys
from datetime import date
sys.path.append(os.curdir)
from data import *

AUTHOR = 'Geração H2V'
SITENAME = 'Geração H2V'
SITEURL = 'geracaoh2v.github.io'
SITETITLE = 'Geração H2V'
SITEDESCRIPTION = 'Várias gerações reunidas em torno de um tema: transição energética.'
BLOGKEYWORDS = ['hidrogênio verde', 'esg', 'desenvolvimento sustentável', 'energia renovável', 'energia eólica',
                'energia solar', 'engenharia de energia', 'energia limpa']
CURRENTYEAR = date.today().year
DISCLAIMER = False
COPYRIGHT = f'&copy; Geração H2V, {CURRENTYEAR}'

RELATIVE_URLS = True
THEME = 'theme/v0'

PATH = 'content'
DEPLOY_PATH = 'deploy'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
STATIC_PATHS = [
    'images',
]

#ARTICLE_PATHS = ['blog']
#ARTICLE_URL = 'blog/{category}/{slug}.html'
#ARTICLE_SAVE_AS = 'blog/{category}/{slug}.html'
#ARTICLE_LANG_URL = 'blog/{category}/{slug}-{lang}.html'
#ARTICLE_LANG_SAVE_AS = 'blog/{category}/{slug}-{lang}.html'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"
TAGS_URL = "tags"
TAGS_SAVE_AS = "tags/index.html"

USE_AUTHOR_CARD = True
AUTHOR_CARD_AVATAR = 'images/logo.png'
AUTHOR_CARD_DESCRIPTION = "Meu nome é Kura e eu quebro coisas."
AUTHOR_CARD_SOCIAL = [
    ("""<i class="fa fa-instagram" aria-hidden="true"></i>""", "https://instagram.com/flavialopes.dev"),
    (""" <i class="fa fa-linkedin" aria-hidden="true"></i>""", "https://linkedin.com/in/lopesflavia"),
]

DIRECT_TEMPLATES = [
    'index',
    'categories',
    'tags',
    'archives',
    'search'
]
#
TEMPLATE_PAGES = {
    'index.html': 'index.html',
    'mentorias.html': 'mentorias.html',
    'calendario.html': 'calendario.html',
    'cursos.html': 'cursos.html',
    'sobre.html': 'sobre.html',
    'parceiros.html': 'parceiros.html',
    'vagas.html': 'vagas.html',
    #'blog.html': 'blog.html'
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'tipue-search',
    'related-posts',
    'series',
    'neighbors'
]
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
MENUITEMS = [
    ("Mentorias", "mentorias.html"),
    ("Calendário", "calendario.html"),
    ("Cursos", "cursos.html"),
    ("Sobre Nós", "sobre.html"),
    ("Parceiros", "parceiros.html"),
    ("Vagas", "vagas.html"),
    #("Blog", "blog.html")
]
LOAD_CONTENT_CACHE = False

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-br'

# global metadata to all the contents
DEFAULT_METADATA = {
    'favicon': 'images/ico.ico',
    'avatar': 'images/logo.png'
}
# Dados de redes sociais
SOCIALSHARE = (
    ('twitter',
     'https://twitter.com/share?text={}&url={}&hashtags={}'.format(
         INTRODUCTION[:170].strip(),
         SITEURL.strip(),
         ','.join([f'{"".join(it.split())}' for it in BLOGKEYWORDS])
     )
     ),
    ('facebook', 'https://www.facebook.com/sharer/sharer.php?u={}'.format(SITEURL)),
    ('linkedin', 'https://www.linkedin.com/sharing/share-offsite/?url={}'.format(SITEURL)),
    ('whatsapp', 'https://api.whatsapp.com/send?text={}'.format(SITEURL)),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

MEGA_FOOTER = False