"""
The MIT License (MIT)

Copyright (c) 2017 Eduardo Henrique Vieira dos Santos

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys, commaimg, Image

filePath = "".join(sys.argv[1])
if filePath == "--help" or filePath == "-h":
	print "Usage: python term_commaimg.py <input-file> [option] <output-file> [args...]"
	print "  python term_commaimg.py file.x [option] file.y"
	print "  python term_commaimg.py file.x -csv\n"
	print "    -csv \t Convert input-file to .csv format"
	print "    -img \t Convert input-file to img (.jpeg) format"
	print "    -resize_csvtojpeg <file> [width] [height] \t Resize input-file.csv to .jpeg format"
	print ""
	print "  python term_commaimg.py file.jpeg -csv file.csv"
	print "  python term_commaimg.py file.csv -img file.jpeg"
else:
	option = sys.argv[2]
	f_output = sys.argv[3]

	if str(option) == "-csv":
		commaimg.convertFileToCsvSave(filePath,f_output)

	if str(option) == "-img":
		commaimg.convertFileToImgSave(filePath,f_output)

	if str(option) == "-resize_csvtojpeg":
		commaimg.resizeFileCsvToImg(filePath, [sys.argv[4],sys.argv[5]],f_output)