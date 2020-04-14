# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:43:18 2020

@author: Harika Vajha
"""
import nltk
from nltk.tokenize import word_tokenize 
nltk.download('punkt')
f=open("File.txt","r")
if f.mode=="r":
    text=f.read()
    
nltk_tokens = nltk.word_tokenize(text)
c1=c2=c3=c4=c5=c6=0
level1=["choose","define",'find','how','label','list','match','name','omit','recall','relate','select','show',
'spell','tell','what','why','when','who','where','which']
level2=['classify','compare','contrast','demonstrate','explain','extend','illustrate','infer',
'interpret','outline','relate','rephrase','show','summarize','translate']
level3=['apply','build','choose','construct','develop','experiment with','identify','interview'
'make use of','model','organize','plan','select','solve','utilize']
level4=['analyze','assume','categorize','classify','compare','conclusion','contrast','discover',
'dissect','distinguish','divide','examine','function','inference','inspect','list','motive','relationships',
'simplify','survey','take part in','test for','theme']
level5=['agree','appraise','assess','award','choose','compare','conclude','criteria',
'criticize','decide','deduct','defend','determine','disprove','dispute','estimate',
'evaluate','explain','importance','influence','interpret','judge','justify','mark',
'measure','opinion','perceive','prioritize','prove','rate','recommend','rule on',
'select','support','value']
level6=['adapt','build','change','choose','combine','compile','compose','construct','create',
'delete','design','develop','discuss','elaborate','estimate','formulate','happen','imagine',
'improve','invent','make up','maximize','minimize','modify','original','originate','plan',
'predict','propose','solution','solve','suppose','test','theory']
for i in nltk_tokens:
    if i in level1:
        c1+=1
    elif i in level2:
        c2+=1
    elif i in level3:
        c3+=1
    elif i in level4:
        c4+=1
    elif i in level5:
        c5+=1
    elif i in level6:
        c6+=1
l1=[c1,c2,c3,c4,c5,c6]


print("The paper has %d questions that come under the category of remember."%c1)
print("\n")


print("The paper has %d questions that come under the category of understand."%c2)
print("\n")

print("The paper has %d questions that come under the category of application."%c3)
print("\n")

print("The paper has %d questions that come under the category of analysis."%c4)
print("\n")

print("The paper has %d questions that come under the category of evaluate."%c5)
print("\n")

print("The paper has %d questions that come under the category of creation."%c6)
print("\n")

l2=sorted(l1)
if l2[-1]==c1:
    print("So, the paper is of level1- you can remember the subject and attempt")
if l2[-1]==c2:
    print("Hence, the paper is of level2- you have to understand the concept")
if l2[-1]==c3:
    print("So, paper is of level3- you have to know the application.")
if l2[-1]==c4:
    print("Hence, paper is of level4- you need to be able to analyze the subject")
if l2[-1]==c5:
    print("So,the paper is of level5- you need to be thorough with the concepts for evaluation.")
if l2[-1]==c6:
    print("Hence, paper is of level6- you can only attempt if you master the subject")
    
f.close()


    


    
