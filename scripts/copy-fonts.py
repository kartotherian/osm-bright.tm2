#!/usr/bin/python

# Use this script to copy a subset of the Google Noto fonts into the ./fonts directory.
# The fonts to select are based on the 'scripts' variable below.

import sys, os, inspect, shutil, glob

def dieUsage():
    print 'Usage: python make-fonts.py <NotoSans directory>\n'
    sys.exit(1)

if len(sys.argv) < 2:
    dieUsage()

fontDir = sys.argv[1]
if not fontDir.endswith('/'): fontDir += '/'

files = []
# Thaana = font for Divehi
# ImperialAramaic = font for Aramaic
scripts = ['Armenian', 'Balinese', 'Bengali', 'Cherokee', 'Devanagari', 'Ethiopic', 'Georgian', 'Gujarati', 'Gurmukhi', 'Hebrew', 'ImperialAramaic', 'Javanese', 'Kannada', 'Khmer', 'Lao', 'Malayalam', 'Mongolian', 'Myanmar', 'Oriya', 'Sinhala', 'Tamil', 'Telugu', 'Thaana', 'Thai', 'Tibetan', 'Tifinagh']

rootDir = os.path.abspath(os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe())))) + '/'

def filename(style, script = None, ext = 'ttf'):
    res = fontDir + 'NotoSans'
    if script != None:
        res += script
    return res + '-' + style + '.' + ext

def findFont(style, script):
    fn = filename(style, script, 'ttf')
    if os.path.isfile(fn): return fn
    fn = filename(style, script, 'otf')
    if os.path.isfile(fn): return fn
    return False

for style in ['Regular', 'Bold', 'Italic']:
    fn = filename(style, ext = 'ttf')
    shutil.copy(fn, rootDir + 'fonts')
    for script in scripts:
        fn = findFont(style, script)
        if not fn: continue
        shutil.copy(fn, rootDir + 'fonts')

list = glob.glob(fontDir + 'NotoNaskhArabic*')
list.extend(glob.glob(fontDir + 'LICENSE*'))
for file in list:
    shutil.copy(file, rootDir)
