#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
__license__   = 'GPL v3'
__copyright__ = '2010, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'

'''
Contains various tweaks that affect calibre behavior. Only edit this file if
you know what you are dong. If you delete this file, it will be recreated from
defaults.
'''


# The algorithm used to assign a new book in an existing series a series number.
# Possible values are:
# next - Next available number
# const - Assign the number 1 always
series_index_auto_increment = 'next'
