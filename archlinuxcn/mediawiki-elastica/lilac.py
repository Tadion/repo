from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'Elastica',
    _G.newver,
    'Provides base elasticsearch functionality',
    'GPL2',
  )

def post_build():
  mediawiki_post_build()
