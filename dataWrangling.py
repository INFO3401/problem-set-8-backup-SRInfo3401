#By: Steven Rothaus 
#Problem Set 8 Due 28th
import pandas as pd
import re
import csv

#Should contain a function called generateCleanFile that takes as input 
#(1) the name of the file to be cleaned
#(2) the name of the file to be generated that will hold the cleaned data.
def generateCleanFile(input_file, output_file):
    df = pd.read_csv(input_file, encoding="latin1", low_memory=False)

#Remove as many special and standard HTML style characters(https://lzone.de/examples/Python%20re.sub)
#re. function(https://docs.python.org/3/library/re.html)

#Aaron advised we solved by starting with #2
#Number 2
    df['comment_msg'] = df['comment_msg'].apply(lambda x: str(x).strip())
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'\r*',"", str(x)))
    df['comment_msg'] = df['comment_msg'].apply(lambda x: re.sub(r'<.*?>',"",str(x)))
    
#Remove web address content(http.www.com)/App, FREE, %20, Check out my page.(Not case sensitive, remove all variations)
#Number 1
    df['comment_msg'] = df['comment_msg'].apply(lambda x: x.lower())
    spam_comments_remove = ['app', 'free', '%20', 'check out my page', 'http://', 'www.', '.com']
    df = df[df.comment_msg.str.contains('|'.join(spam_comments_remove)) == False]

#Remove null values given to unprocessable content.(null/nan)
#Number 3
    df = df[df['comment_msg'] != "nan"]
    df = df[df['comment_msg'] != "null"]
    df = df[df['comment_msg'] != ""]
    
#Export/Generate 
    df.to_csv(output_file)

generateCleanFile("dd-comment-profile.csv", "dd-comment-profile-revised-clean.csv")