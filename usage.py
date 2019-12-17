#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:04:38 2019

@author: ansh
"""

import nltk
import string
import pandas as pd
from draft import LSI
from nltk.stem.snowball import EnglishStemmer

data = pd.read_csv('wikipedia_utf8_filtered_20pageviews-1K.tsv',sep='\t', header=None)


    
lsi = LSI()

for i in range(100):
    doc = data.iloc[i,:][1]
    doc_id = data.iloc[i,:][0]
    lsi.add_doc(doc, doc_id)
lsi.rebuild_index()

lsi.query('kill animal')



#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#


D1 = {'d1' : 'swift is a hatchback.',
     'd2' : 'compact swift has good mileage.',
     'd3' : 'hatchback is a compact.',
     'd4' : 'compact houses are popular',
     'd5' : 'houses are expensive.',
     'd6' : 'swift sedan is expensive.',
     'd7' : 'expensive cars has less mileage.',
     'd8' : 'motorcycles have great mileage.',
     'd9' : 'motorcycles are unsafe',
     'd10' : 'stay in house if you want to be safe',
     }



Q1 = ['what is compact swift',
     'good mileage cars',
     'how to reduce expenses??']


from draft import LSI
lsi = LSI()

for item in D1:
    doc_id = item
    doc = D1[item]
    lsi.add_doc(doc, doc_id)
lsi.rebuild_index()


for q in Q1:
    print('query : {}\nresult : '.format(q))
    res = lsi.query(q, top=2)
    [print(x) for x in res]
    print()


#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#
    
D2 = {'d1' : 'He who has a why to live can bear almost any how.',
      'd2' : 'To live is to suffer, to survive is to find some meaning in the suffering.',
      'd3' : 'That which does not kill us makes us stronger.',
      'd4' : 'These are quotes by Friedrich Nietzsche.',
      'd5' : 'He was a German philosopher, cultural critic, composer, poet, philologist, and Latin and Greek scholar',
      'd6' : 'Spending his last 11 years in total mental darkness, Friedrich Nietzsche died in 1900.',
      'd7' : 'Here, enjoy a few more quotes.',
      'd8' : 'I am not upset that you lied to me, I am upset that from now on I ca n not believe you.',
      'd9' : 'Sometimes people do not want to hear the truth because they do not want their illusions destroyed.',
      'd10' : 'It is not a lack of love, but a lack of friendship that makes unhappy marriages.',
      'd11' : 'The higher we soar, the smaller we appear to those who cannot fly.',
      'd12' : 'Live and Love quotes by Shakespeare.', 
}


Q2 = ['how to love my life??',
     'good quotes on life']



lsi = LSI()

for item in D2:
    doc_id = item
    doc = D2[item]
    lsi.add_doc(doc, doc_id)
lsi.rebuild_index()


for q in Q2:
    print('query : {}\nresult : '.format(q))
    res = lsi.query(q, top=2)
    [print(x) for x in res]
    print()

#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#%%#