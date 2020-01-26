# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:20:34 2020

@author: mohan
"""
from scrapperImage.ScrapperImage import ScrapperImage  #bring datalayer librarries

class BusinessLayer:    #Create class variables like keyword,fileloc etc..
    
    keyword=""
    fileLoc=""
    image_name=""
    header="" 
    
    def downloadImages(Keyword, header):
        
        imageScrapper = ScrapperImage
        url = imgScrapper.createImageUrl(keyword) #Getting URL image from data layer - 1st function
        rawHtml = imgScrapper.scrap_html_data(url, header)
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterLIstOfImages = imgScrapper.downloadImagesfromURL(imageURLList,keyword, header)

        return masterLIstOfImages        
        
        

