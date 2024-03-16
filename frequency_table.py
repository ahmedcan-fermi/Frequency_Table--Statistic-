import numpy as np

import pandas as pd

import math as mt

import collections



raw_dt = np.random.randint(0,30,50)

#Step 1
#Determine The Number Of Observations

obs_num = len(raw_dt)

#Step 2
#Determine Range

'''
Formule of Range is = (Largest Value of Raw Dataset) - (Smallest Value of Raw Dataset)

The Abbreviation is:

R = L - S

'''

largest_of = raw_dt.max()

smallest_of = raw_dt.min()

range_of = (largest_of - smallest_of)

#Step 3
#Determine Number Of Classes in Frequency Table

'''
Firstly,You should take the square root of total observation number
The class number that we going to select  will be greater than and equal to this number
The exactly formule is:

(n**1/2) <= k

n  present observation number

k  present  class number

The k number that we going to choice would be in sequence of 5<= k <=20

'''
sqr_obs_num = mt.sqrt(obs_num)

if sqr_obs_num < 5 :
  sqr_obs_num = 5

elif sqr_obs_num > 20 :
  sqr_obs_num = 20

else:
  sqr_obs_num = mt.ceil(sqr_obs_num)

#Step 4
#Class Width
'''
Formula of Class Width is  (Range // Class Amount) <= H
'''
part_one = range_of / sqr_obs_num

clss_wd = mt.ceil(part_one)

#Step 5
#Store Values In A Dictionary

'''
I will create a dictionary in order to store values(datas) by dictionary comprehension method in this process

'''
subkeys = ['class_limits','class_borders','observations','class_median','additive_frequencies']

freq_tab = {str(i) : {j:[] for j in subkeys} for i in range(1,sqr_obs_num+1)}


#Step 6
#Determine Class Limits Of First Class


'''
!!!!!!! IMPORTANT !!!!!!!

 The count of sequance of lower and upper limit must be equal to class width
 I mean when you count number of this sequance one by one it must be equal to class width

 Don't Forget!

Lower and upper limits are inclusive

'''
lower_limit = smallest_of # The smallest value of dataset is also lower limit of first class

upper_limit = clss_wd - 1

freq_tab['1']['class_limits'] = [lower_limit,upper_limit]

#Step 7
#Fill Class Limits Of Other Classes By Efficency Of For Loop

for i in range(1,sqr_obs_num):

  lower_limit = (freq_tab[str(i)]['class_limits'][0]) + clss_wd

  upper_limit = (freq_tab[str(i)]['class_limits'][1])  + clss_wd

  freq_tab[str(i+1)]['class_limits'] = [lower_limit,upper_limit]


#Step 8
#Determine Class Borders Of First Class

'''
For determining class borders of first class we follow a solution algorithm:

1-Find that what is upper limit value of first class
2-Find that what is lower limit value of second class
3-Add those values
4- Divide by 2
5-The result that we got is upper border
6-For finding lower limit we substract upper border by class width
7-For finding class borders of other classes we add class width value to both lower border and upper border of previous class 

'''

up_lim = freq_tab['1']['class_limits'][1] # upper limit of first class

low_lim = freq_tab['2']['class_limits'][0] # lower limit of second class

up_border = (up_lim + low_lim) / 2 # upper border of first class

low_border = up_border - clss_wd #lower border of first class

freq_tab['1']['class_borders'] = [low_border,up_border]

#Create Class Borders Of Other Classes By Efficency Of For Loop

for j in range(1,sqr_obs_num):

  low_brd = freq_tab[str(j)]['class_borders'][0] + clss_wd
  
  upp_brd = freq_tab[str(j)]['class_borders'][1] + clss_wd

  freq_tab[str(j+1)]['class_borders'] = [low_brd,upp_brd]


#Step 9
#Create An User Defined Function For Determine Total Observation Numbers In Given Class Limit Sequence

def seq_obs(a,b):
  
  total_obs = 0
  
  counter = collections.Counter(raw_dt)

  for i in range(a,b+1):

    try:

      total_obs += counter[i]  
   
    except:
      
      continue
 
  return total_obs


#Step 10
#Use seq_obs user defined function for determine total observations in specific sequence

for k in range(1,sqr_obs_num+1):

  low_limit = freq_tab[str(k)]['class_limits'][0]
  
  upp_limit = freq_tab[str(k)]['class_limits'][1]
  
  freq_tab[str(k)]['observations'] = [seq_obs(low_limit,upp_limit)]


#Step 11
#Determine Class Limit Medians of Classes 

'''
We try to determine median of first class. It going to help us to find other class medians
'''
cls_lim = freq_tab['1']['class_limits']

list_of = [i for i in range(cls_lim[0],cls_lim[1]+1)] 

np_list = np.array(list_of)

first_med = np.median(np_list)

freq_tab['1']['class_median'] = [first_med]

#Step 12
#We Will Determine Class Medians Of Other Classes By Efficency Of For Loop  

for x in range(1,sqr_obs_num):

  class_med = freq_tab[str(x)]['class_median'][0] + clss_wd
  freq_tab[str(x+1)]['class_median'] = [class_med]

#Step 13
#Finally We Should Determine Additive Frequencies Of Classes

'''

So firstly we will find the first one's additive frequency

Just for the firs class,the observation amount and additive frequency are same value

'''

freq_tab['1']['additive_frequencies'] = freq_tab['1']['observations']



for q in range(1,sqr_obs_num):

  add_freq = freq_tab[str(q+1)]['observations'][0] + freq_tab[str(q)]['additive_frequencies'][0]

  freq_tab[str(q+1)]['additive_frequencies'] = [add_freq] 


print(freq_tab)

