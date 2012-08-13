# -*- coding: utf-8 -*-
#
#  Copyright (c) 2012 Ole Krause-Sparmann
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
#  and associated documentation files (the "Software"), to deal in the Software without restriction, 
#  including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
#  and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial 
#  portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
#  LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import xml.dom.minidom as dom
import codecs
import re
import os

BROWN_POS_PATH = "/Path/On/Your/Disk/Where/All/The/Brown/POS/Files/Are/Brown/"

# The separator you want to use in the generated brown.pos
TAG_TOKEN_SEPARATOR = "#!#"

out  = open("brown.pos","w")
tokens_pattern = re.compile('(\s*[(.+)/(.+)]\s+)*')

files = os.listdir(BROWN_POS_PATH)

sentence_lines = []

for filename in files:
    if len(filename)==4 and filename[0] == 'c':
        print 'Parsing '+filename+'...'
        file = open(BROWN_POS_PATH+filename)
        ignore_sentence = False
        while 1:
            lines = file.readlines(100000)
            if not lines:
                break
            for line in lines:
                tokens = line.split(' ')
                if len(tokens)>4:
                    for token_str in tokens:
                        parts = token_str.split('/')
                        if len(parts)!=2:
                           continue
                        token = parts[0].strip()
                        tag = parts[1].strip()
                        if tag == "``" or tag == "''":
                            continue

                        if tag.endswith('-nc') or tag.endswith('+vb') or tag.endswith('+ppss') or tag.endswith('+cs'):
                            ignore_sentence = True
                        if tag[:2] == 'fw' or tag.endswith('-hl'):
                            tag = 'fw'
                        if tag.endswith('-tl'):
                            tag = tag[:-3]

                        token_already_added = False

                        if tag.endswith('+ber'):
                            sentence_lines.append(token.replace("'re","") + TAG_TOKEN_SEPARATOR + tag[:-4] + "\n")
                            sentence_lines.append("are" + TAG_TOKEN_SEPARATOR + "ber" + "\n")
                            token_already_added = True

                        if tag.endswith('+bem'):
                            sentence_lines.append(token.replace("'m","") + TAG_TOKEN_SEPARATOR + tag[:-4] + "\n")
                            sentence_lines.append("am" + TAG_TOKEN_SEPARATOR + "bem" + "\n")
                            token_already_added = True

                        if not token_already_added:
                            sentence_lines.append(token + TAG_TOKEN_SEPARATOR + tag + "\n")

                if len(sentence_lines)>0 and not ignore_sentence:
                    out.write(''.join(sentence_lines))
                    out.write('\n')

                ignore_sentence = False
                sentence_lines = []

out.close()


