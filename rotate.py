#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2012 Chris Oelmueller <chris.oelmueller@gmail.com>
#
# Permission is hereby granted, free of charge,  to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction,  including without limitation the rights
# to use,  copy, modify,  merge, publish,  distribute, sublicense,  and/or sell
# copies of the Software,  and to permit persons  to whom  the Software is fur-
# nished to do so, subject to the following conditions:
#
# The above  copyright notice  and this permission notice  shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS  PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR
# IMPLIED,  INCLUDING  BUT NOT  LIMITED TO  THE WARRANTIES  OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR  PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR  COPYRIGHT HOLDERS  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIA-
# BILITY,  WHETHER IN AN ACTION OF CONTRACT,  TORT OR OTHERWISE,  ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Run as `rotate.py infile outfile degrees`

>>> numbers = ('123\\n'
...            '.5.\\n'
...            '678\\n'
...            '9.0'  )
>>> print(rotate(numbers))
3.80
257.
1.69
>>> print(transpose(numbers))
1.69
257.
3.80
>>> transpose(transpose(numbers)) == numbers
True
>>> rotate(rotate(rotate(rotate(numbers)))) == numbers
True
>>> transpose(rotate(numbers)) == rotate(transpose(numbers))
False
>>> transpose(rotate(transpose(numbers))) == rotate(rotate(rotate(numbers)))
True
"""

import itertools, sys

def transpose(instream, rotate=False):
	"""Transposes strings."""
	stripped = [l.rstrip() for l in instream.split('\n')]
	transposed = list(map(''.join, itertools.zip_longest(*stripped, fillvalue=' ')))
	if rotate:
		transposed.reverse()
	return '\n'.join(transposed)

def rotate(instream):
	"""Rotates strings by 90 degrees, counterclockwise."""
	return transpose(instream, rotate=True)

def main(infile, outfile, iterations):
	"""Rotates strings by *iterations* * 90 degrees, counterclockwise,
	and writes the result to *outfile*.
	While certain degrees like multiples of 45 might be fun to implement,
	this only works with multiples of 90 for the time being."""
	with open(infile, 'r') as f:
		f = ''.join([line for line in f])
	for _ in range(iterations):
		f = rotate(f)
	with open(outfile, 'w') as out:
		out.write(f)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	infile, outfile, rotation = sys.argv[1:]
	iterations = int(rotation) // 90 # how often to rotate 90 degrees, counterclockwise
	main(infile, outfile, iterations)
