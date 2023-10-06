# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import configparser
from datetime import date
from os.path import join, dirname


# -- Project information -----------------------------------------------------

year = date.today().year

rst_prolog = '''
.. |year| replace:: {0}
'''.format(year)

project = u'FSCrawler'
copyright = "%i, David Pilato" % year
author = u'David Pilato'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

config = configparser.ConfigParser()
config.read(join(dirname(__file__), "fscrawler.ini"))

# development versions always have the suffix '-SNAPSHOT'
def read_version(full_version=True):
    raw_version = config.get('FsCrawler', 'Version');
    return raw_version if full_version else raw_version.replace("-SNAPSHOT", "")

version = read_version(full_version=False)
# The full version, including alpha/beta/rc tags.
release = read_version()

downloadUrl = "https://repo1.maven.org/maven2/fr/pilato/elasticsearch/crawler/fscrawler-distribution/%s/fscrawler-%s.zip" % (version, version)

if release.endswith('-SNAPSHOT'):
    downloadUrl = "https://s01.oss.sonatype.org/content/repositories/snapshots/fr/pilato/elasticsearch/crawler/fscrawler-distribution/%s/" % release

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'FSCrawlerdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'FSCrawler.tex', u'FSCrawler Documentation',
     u'David Pilato', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'fscrawler', u'FSCrawler Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'FSCrawler', u'FSCrawler Documentation',
     author, 'FSCrawler', 'Index your binary documents in elasticsearch',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

rst_prolog = rst_prolog + """
.. |Tika| replace:: Tika
.. |ES| replace:: Elasticsearch
.. |Tika_format| replace:: Tika
.. |Tika_version| replace:: Tika {fmt_tika_version}
.. |Tika_configuring| replace:: Configuring Tika
.. |ES_version6| replace:: Elasticsearch {fmt_es_version6}
.. |ES_version7| replace:: Elasticsearch {fmt_es_version7}
.. |ES_version8| replace:: Elasticsearch {fmt_es_version8}
.. |Tiff_version| replace:: jai-imageio-core:{fmt_tiff_version}
.. |JPEG2000_version| replace:: jai-imageio-jpeg2000:{fmt_jpeg_version}
.. |Download_URL| replace:: Sonatype
.. |Maven_Central| replace:: Maven Central
.. |Sonatype| replace:: Sonatype

.. _Tika: https://tika.apache.org/{fmt_tika_version}/
.. _ES: https://www.elastic.co/products/elasticsearch
.. _Tika_format: https://tika.apache.org/{fmt_tika_version}/formats.html#Supported_Document_Formats
.. _Tika_version: https://tika.apache.org/{fmt_tika_version}/
.. _Tika_configuring: https://tika.apache.org/{fmt_tika_version}/configuring.html
.. _ES_version6: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
.. _ES_version7: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
.. _ES_version8: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
.. _Tiff_version: https://repo1.maven.org/maven2/com/github/jai-imageio/jai-imageio-core/{fmt_tiff_version}/
.. _JPEG2000_version: https://repo1.maven.org/maven2/com/github/jai-imageio/jai-imageio-jpeg2000/{fmt_jpeg_version}/
.. _Download_URL: {fmt_downloadUrl}
.. _Maven_Central: https://repo1.maven.org/maven2/fr/pilato/elasticsearch/crawler/fscrawler-distribution/
.. _Sonatype: https://s01.oss.sonatype.org/content/repositories/snapshots/fr/pilato/elasticsearch/crawler/fscrawler-distribution/
""".format(
fmt_tika_version=config.get('3rdParty', 'TikaVersion'),
fmt_es_version6=config.get('3rdParty', 'ElasticsearchVersion6'),
fmt_es_version7=config.get('3rdParty', 'ElasticsearchVersion7'),
fmt_es_version8=config.get('3rdParty', 'ElasticsearchVersion8'),
fmt_tiff_version=config.get('3rdParty', 'TiffVersion'),
fmt_jpeg_version=config.get('3rdParty', 'JpegVersion'),
fmt_downloadUrl=downloadUrl,
fmt_release=release
)
