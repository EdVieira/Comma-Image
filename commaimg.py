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
from PIL import Image, ImageDraw
import numpy
from StringIO import StringIO
from numpy import genfromtxt
from io import BytesIO

def RGBAtoRGB(img,ext="jpg"):
    fill_color = 'WHITE'  # your background
    if img.mode in ('RGBA', 'LA') and ext not in ('png','tiff'):
        background = Image.new(img.mode[:-1], img.size, fill_color)
        background.paste(img, img.split()[-1])
        img = background.convert('RGB')
    return img

def imgToCsv(img, file = False):
    print "Converting image to CSV"
    print "hold on a sec..."
    if file:
        img=Image.open(img)
    img = RGBAtoRGB(img)
    imgarray=numpy.array(img)
    fullstring = ""
    for row in imgarray:
        outputstring=""
        for column in row:
            count = 0
            valuestring=""
            for value in column:
                if value < 10:
                    valuestring+="00"+str(value%256)+";"
                elif value < 100:
                    valuestring+="0"+str(value%256)+";"
                else:
                    valuestring+=str(value%256)+";"
            outputstring+=valuestring
        fullstring += outputstring+"\n"
        fullstring.replace("a","")
    return fullstring

def csvToImg(csv, file = False):
    print "Converting CSV to image"
    print "hold on a sec..."
    temp = 0
    if file:
        temp = readCsv(csv,True)
    else:
        temp = readCsv(csv)
    temp = numpy.array(temp)
    im = Image.fromarray(temp, 'RGB')
    pix = im.load()
    cols,rows = im.size
    for x in xrange(rows):
        l = temp.tolist()[x]
        for y in xrange(cols):
            if (x+y) % 1000 == 0:
                print "x:",x," of:",rows,"\t y:",y," of:",cols
            i = l[y]
            pix[y,x] = (int(i[0])%256, int(i[1])%256, int(i[2])%256)
    return im

def readCsv(name, openF = False):
    temp = 0
    if openF:
        name = open(name, 'rwb')
        temp = genfromtxt(name, delimiter = ';')
        temp = temp.tolist()
        name.close()
    else:
        temp = genfromtxt(StringIO(name), delimiter = ';')
        temp = temp.tolist()
    for i in temp:
        for j in i:
            if str(j) == 'nan':
                i.pop(i.index(j))
    final = []
    for x in xrange(len(temp)):
        final.append(splitList(temp[x], 3))
    return final

def splitList(lista, sizes):
    final = []
    last = 0
    aux = 0
    for i in xrange(len(lista)):
        if i % sizes == 0:
            final.append(lista[last:i])
            last = i
        aux = i
    final.append(lista[last:])
    final = final[1:]
    return final

def saveCsv(csv, string):
    f = open(csv, 'wb')
    f.write(string)
    f.close()
    print csv+' saved'
    return csv

def saveImg(imgName, img):
    img.save(imgName)
    img.close()
    print imgName+' saved'
    return img

def convertFileToCsv(filePath, f_output, save = False):
    csv = imgToCsv(filePath,True)
    if save:
        csv = saveCsv(f_output,csv)
    return csv

def convertFileToImg(filePath, f_output, save = False):
    img = csvToImg(filePath,True)
    if save:
        img = saveCsv(f_output,img)
    return img

def resizeFileCsvToImg(filePath, xy, f_output, save = False):
    shape = (int(xy[0]),int(xy[1]))
    img = csvToImg(filePath,True)
    img = img.resize(xy, Image.ANTIALIAS)
    if save:
        img = saveImg(f_output,img)
    return img

def resizeFileImgToCsv(filePath, xy, f_output, save = False):
    shape = (int(xy[0]),int(xy[1]))
    img = csvToImg(filePath, True)
    img = img.resize(xy, Image.ANTIALIAS)
    csv = imgToCsv(img)
    if save:
        csv = saveCsv(f_output,img)
    return csv

def resizeFileImg(filePath, xy,f_output, save = False):
    shape = (int(xy[0]),int(xy[1]))
    csv = imgToCsv(filePath,True)
    img = csvToImg(csv)
    img = img.resize(xy, Image.ANTIALIAS)
    if save:
        img = saveImg(f_output,img)
    return img

def resizeFileCsv(filePath, xy,f_output, save = False):
    shape = (int(xy[0]),int(xy[1]))
    img = csvToImg(filePath,True)
    img = resizeImg(img, xy)
    csv = imgToCsv(img)
    if save:
        csv = saveCsv(f_output,img)
    return img

def resizeCsvToImg(csv, xy):
    shape = (int(xy[0]),int(xy[1]))
    img = csvToImg(csv)
    img = img.resize(xy, Image.ANTIALIAS)
    return img

def resizeImgToCsv(img, xy):
    shape = (int(xy[0]),int(xy[1]))
    img = img.resize(xy, Image.ANTIALIAS)
    csv = imgToCsv(img)
    return csv

def resizeImg(img, xy):
    shape = (int(xy[0]),int(xy[1]))
    img = img.resize(xy, Image.ANTIALIAS)
    return img

def resizeCsv(csv, xy):
    shape = (int(xy[0]), int(xy[1]))
    img = csvToImg(csv)
    img = img.resize(xy, Image.ANTIALIAS)
    csv = imgToCsv(img)
    return csv

def getCsvFilesFromTxtList(filePath):
	f = open(filePath, "rb")
	l = list(f)
	filePathList = []
	for i in xrange(len(l)):
		filePathList.append(l[i].replace("\n", ""))
	f.close()
	l = []
	for i in filePathList:
		l.append(imgToCsv(csvToImg(i,True)))
	return l

def getImgFilesFromTxtList(filePath):
	f = open(filePath, "rb")
	l = list(f)
	filePathList = []
	for i in xrange(len(l)):
		filePathList.append(l[i].replace("\n", ""))
	f.close()
	l = []
	for i in filePathList:
		img=Image.open(i)
		l.append(img)
	return l

def imgListToCsvList(imgList):
    l = []
    for i in xrange(len(imgList)):
        l.append(imgToCsv(imgList[i]))
    return l

def csvListToImgList(csvList):
    l = []
    for i in csvList:
        l.append(csvToImg(i))
    return l

def resizeImgList(imgList, xy):
	l = []
	for i in imgList:
		l.append(resizeImg(i,xy))
	return l

def resizeCsvList(csvList, xy):
	l = []
	for i in csvList:
		l.append(resizeCsv(i,xy))
	return l

def saveImgList(imgList, filePath, ext):
    for i in xrange(len(imgList)):
        saveImg(filePath+"/"+str(i)+"."+ext, RGBAtoRGB(imgList[i],ext))
    return imgList

def saveCsvList(csvList, filePath):
    for i in xrange(len(csvList)):
        saveCsv(filePath+"/"+str(i)+".csv", csvList[i])
    return csvList
"""

filePath = "".join(sys.argv[1])
option = sys.argv[2]
f_output = sys.argv[3]

if str(option) == "-csv":
    csv = comajpeg.imgToCsv(filePath)
    comajpeg.saveCsv(f_output,csv)

if str(option) == "-jpeg":
    img = comajpeg.csvToImg(filePath)
    comajpeg.saveImg(f_output,img)
"""