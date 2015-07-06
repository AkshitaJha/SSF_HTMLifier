#!/usr/bin/env python
import os
import sys
import codecs
import re
import locale

import SSF

class ssf_htmlifier:
    
    def __init__(self, S):
        # read the file containing the sentence
        fileName = S
        self.S = SSF.Document(fileName) 
	self._get_words()

    def _get_words(self):
	self.words = []
	self.sent = ''
	for tree in self.S.nodeList : 
             for chunkNode in tree.nodeList :
                 for node in chunkNode.nodeList :
                     self.words.append(node.printValue()) #node.index
                     refAddress = node.getAttribute('ref')
                     if refAddress != None :
                         refNode = getAddressNode(refAddress, node)
                         #print tree.printSSFValue()
                         #print tree.header + tree.text + tree.footer
	# print self.words
	for each_word in self.words:
		self.sent = self.sent + each_word + ' '

    def css(self, s=None):
        # returns the associated css
	css = "<b> "
	if s == None:
		css = css + self.sent
	else:
		css = css + s 
	css = css + "</b>"
	print css

    def html_markup(self, s=None):
        # returns the associated html_markup
	html = "<p> "
	if s == None:
		html = html + self.sent
	else:
		html = html + s
	html = html + "</p>"
	print html

    def scripts(self, s=None):
        # returns the associated scripts string
	foo = 1
	
    def raw_parse(self):
        # returns the raw XML parse of the sentence
        for k in self.S.nodeList:
            if k.__class__.__name__=="ChunkNode":
            	foo=1
            if k.__class__.__name__=="Sentence":
            	print k.getXML()
            if k.__class__.__name__=="Node":
            	foo = 1


    def render():
        # Returns the full stand alone CSS + HTML + JS as a string, 
        # which can be embedded in any HTML page
	foo = 1


ssf_html_object = ssf_htmlifier(sys.argv[1])
ssf_html_object.html_markup()
ssf_html_object.html_markup("testing")
ssf_html_object.css()
ssf_html_object.css("testing")
ssf_html_object.raw_parse()
#ssf_html_object.render()

