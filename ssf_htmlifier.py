#!/usr/bin/env python
import os
import sys
import codecs
import re
import locale

import SSF

class ssf_htmlifier:
    
    def __init__(self, inp):
        # read the file containing the sentence
        fileName = inp
        self.S = SSF.Document(inp)
        self.xml = self.raw_parse()
        

    def css(self, s=None):
        # returns the associated css
        foo = 1
        # read the css file: css/xmltree.css


    def html_markup(self, s=None):
        # returns the associated html_markup
        if s != None:
            with open('input.txt','w') as fp:
                fp.write(s)
            self.S = SSF.Document('input.txt')
            self.xml = self.raw_parse()
        html = "<body><p>%s</p></body>" %(self.xml)
	os.remove('input.txt')
	print html
            

    def scripts(self, s=None):
        # returns the associated scripts string
	   foo = 1
       # read the js files: javascript/xmltree.js, custom.js

	
    def raw_parse(self):
        # returns the raw XML parse of the sentence
        for k in self.S.nodeList:
            if k.__class__.__name__=="ChunkNode":
            	foo=1
            if k.__class__.__name__=="Sentence":
            	return k.getXML()
            if k.__class__.__name__=="Node":
            	foo = 1

    def render(self):
        # Returns the full stand alone CSS + HTML + JS as a string, 
        # which can be embedded in any HTML page
        # template.html
        with open('out.xml','w') as fp:
		fp.write(self.xml)
        html = "<head><link rel='stylesheet' type='text/css' href='css/xmltree.css' />\n<script src='http://code.jquery.com/jquery-1.10.2.min.js'></script>\n<script src='javascript/xmltree.js'></script>\n<script src='javascript/custom.js'></script>\n<script type='text/javascript'>\n$(function() { new XMLTree({fpath: '%s', container: '#tree', startExpanded: true,}); </script>\n<title></title></head>\n<body><!--<span style='float:right'><b>Search</b><input type='text' id='search_input' tabindex='-1' ></span>-->\n<br/><div id='tree'></div></body>" %('out.xml')
	os.remove('out.xml')
        print html


ssf_html_object = ssf_htmlifier(sys.argv[1])
ssf_html_object.html_markup()
#ssf_html_object.html_markup(ssf_str)
ssf_html_object.css()
#ssf_html_object.css("ssf_str")
x = ssf_html_object.raw_parse()
print x
ssf_html_object.render()
