#import AnnyE
import commaimg, Image, sys
import numpy as np

imgList = commaimg.getImgFilesFromTxtList("lista.txt")
#print len(imgList)
cList = commaimg.imgListToCsvList(imgList)
commaimg.saveCsvList(cList, "csv/")

iList = commaimg.resizeImgList(imgList,(50,50))
commaimg.saveImgList(iList, "img/resized","gif")
iList = commaimg.resizeImgList(imgList,(100,100))
commaimg.saveImgList(iList, "img/resized","tiff")
iList = commaimg.resizeImgList(imgList,(200,200))
commaimg.saveImgList(iList, "img/resized","png")
iList = commaimg.resizeImgList(imgList,(250,250))
commaimg.saveImgList(iList, "img/resized","jpg")

#csvList = commaimg.getCsvFilesFromTxtList("lista2.txt")
#print commaimg.resizeCsvList(csvList,(50,50))
