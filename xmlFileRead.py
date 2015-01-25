'''
Created on Jan 24, 2015

@author: trinter
'''
#from xml.dom import minidom
import os

filepath=raw_input('Enter the file path: ')

#filepath="C:/Users/tttri_000/Documents/Chatham/Clients/SMBC/XML Results"
os.chdir(filepath)
# filename = "A9B2858.xml.result"
# 
# xmldoc = minidom.parse(filename)
# CRNnode = xmldoc.getElementsByTagName('CRN')
# if CRNnode.length>0:
#     CRN=CRNnode[0].firstChild.data 
# 
# transIDnode = xmldoc.getElementsByTagName('TransactionID')
# if transIDnode.length>0:
#     transID=transIDnode[0].firstChild.data     
# #TransactionId= xmldoc.getElementsByTagName('TransactionID').firstChild.nodeValue
# 
# print CRN
# print transID

import xml.etree.ElementTree as etree
import datetime

files_in_dir = os.listdir(filepath)
if len(files_in_dir)>0:
    now=datetime.datetime.now()
    fileName="results" + str(now.year) +"-"+str(now.month)+"-"+str(now.day)+".csv"

    #Open a file where the results will be written as csv
    resultFile=open(fileName, "w+")
    resultFile.write("FileName,CRN,TransactionID,Success,Message" +chr(13))
    for file_in_dir in files_in_dir:
        if file_in_dir.find('.result')>0:
            mydoc = etree.ElementTree(file=file_in_dir)
            CRN=""
            transID=""
            message=""

            CRNnode=mydoc.findall('.//CRN')
            if len(CRNnode)>0:
                CRN=CRNnode[0].text
    #             print CRN
            
            transIDnode=mydoc.findall('.//TransactionID')
            if len(transIDnode)>0:
                transID=transIDnode[0].text
    #             print transID
        
            messageList=mydoc.findall('.//MessageText')
            if len(messageList)>0:
                success=False
            #Look for success message
                for msg in messageList:
                    if msg.text.find("Successful records: 1")>-1:
                        success=True

            message=messageList[len(messageList)-1].text
            #remove commas, and line breaks     
            message=message.replace(',',';')
            message=message.replace('\n',':')
            resultFile.write(file_in_dir +","+ CRN +"," + str(transID) +',' + str(success) + ',' + message + chr(13))

    #Close the results file
    resultFile.close()  
    print "Finished"
      
