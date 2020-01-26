# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:02:41 2020

@author: mohan
"""
#Importing necessary libraries
from flask_cors import CORS, cross_origin #Cross Origin resource sharing (CORS) 
#CORS is sec machanisam that allows a web page from one domain or origin to access a resource with a diffrent domain (cross domain request)
from flask import Flask, render_template, request, jsonify  #Render_Template for displaying html files
import os
abc = os.listdir()
print(abc)
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer


#importing request
app = Flask(__name__) #Initializing the flask app with the name 'app'

@app.route('/')  #route for redirecting to home page
@cross_origin() 
def home():
    return render_template('index.html')

@app.route('/showImages')  #calling 2nd route and this is URL
@cross_origin()
def displayImages():  # function for displaying all images in the statick folder
    list_images=os.listdir('static')  #use OS library to read dir's
    print(list_images)
    try:   #handling the exceptions when there is no images in the folder
        if(len(list_images) > 0 ):  #basically checking length of the images when its >0
            return render_template('showImage.html', user_images=list_images)
        else: 
            return "Images are not present"
        
    except Exception as e:
        print("no images found", e)
        return "Please try with a different search keywaor"

@app.route('/searchImages', methods=['Get','POST']) # /searchimages = index.html we have formaction of search images .. calling the function from index.html
def searchImage(): #after submit button 
    if request.method=='POST':
        search_term=request.form['keyword'] #assigning the value of the input keyword to the variable keyword
        
    else:
        print("Please enter something else")
        
    imagescrapperutil=BusinessLayer ## Initiating a object for scrapperimage class
    imagescrapper=scrapperimage()
    list_images=os.listdir('static')
    imagescrapper.delete_downloaded_images(list_images) #deleting old images before search begins
    
    image_name=search_term.split()
    image_name="+".join(image_name)
    
    #add the header metadata = what is my browser user agent
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
    lst_images=imagescrapperutil.downloadImages(search_term,header)
    return displayImages()



if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000)
    #app.run(debug=True) #to run on cloud
    