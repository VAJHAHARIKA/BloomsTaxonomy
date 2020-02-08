# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:43:18 2020

@author: User
"""
import nltk
from nltk.tokenize import word_tokenize 
nltk.download('punkt')

text = input()
nltk_tokens = nltk.word_tokenize(text)
print (nltk_tokens)
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
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
l2=sorted(l1)
print(l2)
if l2[-1]==c1:
    print("level1")
if l2[-1]==c2:
    print("level2")
if l2[-1]==c3:
    print("level3")
if l2[-1]==c4:
    print("level4")
if l2[-1]==c5:
    print("level5")
if l2[-1]==c6:
    print("level6")


    
