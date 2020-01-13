'''

You need to build a web application to retrieve and show data from the YouTube API.

1. Use YouTube API v3.
2. Your UI should provide a text-box for the user to enter a search term. Returned results should be sortable based on 2 params - eg. name and published date. Sorting should be done client side and should not require another API call.
3. We are trying to understand how fast you learn new technologies and concepts, how deeply you understand them and how well you can apply them. So please keep a note of these as you proceed with this exercise.
4. Focus on getting the entire flow working - edge cases / bonus items are less important.
5. Submit an archive of your project which includes clear instructions on how to run or test your project detailed in a README file. 
6. You're free to make any assumptions about things not covered here.

'''


#importing libraries 
#project has been created on google cloud. image has been attached in the rar file

import os
from flask import Flask, render_template, request, flash
import numpy as np
from search import youtube_search
import sys

#basic flask parameters

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def index():
	return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
	if request.method=="POST":
		query = request.form.get("search_term")
		res=youtube_search(query)

	return render_template('index.html',tables=[res.to_html(classes="table_color")])

if __name__ == "__main__":
	app.run()