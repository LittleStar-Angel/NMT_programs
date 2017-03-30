#encoding=utf-8

import os
import re

''' 
Correction and modification of code given at 
http://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/
'''

def make_trie(*args):
	"""
	Make a trie by given words.
	"""
	trie = {}

	for word in args:
		if type(word) != str:
			raise TypeError("Trie only works on str!")
		temp_trie = trie
		for letter in word:
			temp_trie = temp_trie.setdefault(letter, {})
		temp_trie = temp_trie.setdefault('_end_', '_end_')
        
	return trie

def insert_trie(trie, word):
	"""
	Insert a word to the trie
	"""	
	if type(word) != str:
		raise TypeError("Trie only works on str!")
	temp_trie = trie
	temp_trie.pop('_end_','_end_')
	for letter in word:
		temp_trie = temp_trie.setdefault(letter, {})
	temp_trie = temp_trie.setdefault('_end_', '_end_')
	
	return trie

def in_trie(trie, word):
	"""
	Detect if word in trie.
	"""
	if type(word) != str:
		raise TypeError("Trie only works on str!")
 
	temp_trie = trie
	for letter in word:
		if letter not in temp_trie:
			return False
		temp_trie = temp_trie[letter]
        
	if  "_end_" in temp_trie:
		return True
	else:
		return False
 
def remove_from_trie(trie, word, depth = 0):
	"""
	Remove certain word from trie.
	"""
	if word and word[depth] not in trie:
		return False
 
	if len(word) == depth + 1:
		if '_end_' in trie[word[depth]]:		
			del trie[word[depth]]['_end_']   # baz and barz both are safe
            
		if len(trie[word[depth]]) > 0 and len(trie) > 1:   # baz and barz both are present
			return False
		elif len(trie) > 1 :  # only baz is present
			del trie[word[depth]]
			return False
		elif len(trie[word[depth]]) > 0:   # only barz is present
			return False
		else:
			return True
	else:
		temp_trie = trie 
		# Recursively climb up to delete.
		if remove_from_trie(temp_trie[word[depth]], word, depth + 1):
			if temp_trie:
				del temp_trie[word[depth]]
			return not temp_trie
		else:
			return False

######################ADD###################################

def find_word(word):
	return in_trie(trie, word)

basename = os.path.abspath(__file__)

if re.findall('Trie_Tree.pyc',basename):
	basename = re.sub('Trie_Tree.pyc', 'words', basename)
else:
	basename = re.sub('Trie_Tree.py', 'words', basename)

trie = make_trie()

base = open(basename,'r')

for word in base:
	word = re.sub('\n','',word)
	trie = insert_trie(trie, word)

base.close()

############################################################

