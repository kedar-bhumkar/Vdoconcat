# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:09:05 2020

@author: kedar
""" 
import os
from datetime import datetime
from moviepy.editor import VideoFileClip,concatenate_videoclips

#- directories
folderSuffix = 'Cel'
srcPath = './Storage/Stage/'+folderSuffix
targetPath = './Storage/Prod/'+folderSuffix
trashPath='./Storage/Trash/'+folderSuffix
targetFileSuffix = 'celeb'

# - time 
formatter = '%Y-%m-%d%H%M%S'
noOfSrcFiles = 25
noOfProgramRuns = 1


def vdo_concatenate():
    clips = []
    theClip= ''
    fileList =[]
    now = datetime.now()
    mp4Count = 0

    #- loop over all files and add them to the clips list
    for idx,filename in enumerate(os.listdir(srcPath)):    
        if filename.endswith(".mp4"):
            if mp4Count < noOfSrcFiles:
                mp4Count+=1
                print('idx',idx)
                filePath = os.path.join(srcPath,filename)
                fileList.append(filename)
                theClip = VideoFileClip(filePath)  
                
                for i in range(3):
                    clips.append(theClip)
            else:
                print('idx', idx)
                break;       
        else:
            print(idx, 'No mp4')
    
    if len(clips)==0:
        print('No files found')
    else:           
        #- concatenate and write final file
        video = concatenate_videoclips(clips, method='compose')
        video.write_videofile(targetPath + '/' + targetFileSuffix + '_' + now.strftime(formatter) +'.mp4',threads = 8, fps=24)
        
        for clip in clips:
            print('clip - ',clip)    
            clip.close()
        
        #-delete src files 
        for filename in fileList:
            print('fName - ',filename)        
            os.rename(os.path.join(srcPath,filename), os.path.join(trashPath,filename))

#Start of the program
for i in range(noOfProgramRuns):
    vdo_concatenate()