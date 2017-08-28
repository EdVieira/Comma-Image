#import AnnyE
import commaimg, Image
import numpy as np

imgList = commaimg.getImgFilesFromTxtList("lista.txt")
csvList = commaimg.getCsvFilesFromTxtList("lista2.txt")
print commaimg.resizeImgList(imgList,(50,50))
print csvList[0]
print len(commaimg.resizeCsvList(csvList,(50,50)))
