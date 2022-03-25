# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:55:08 2022

@author: odeya
"""

#TaskA
def read_line (n, file):
    try:
        data_file = open(file)
        number_line = n
        if type(number_line) != int:
            return ("invalid input detected")
        else:
            lst = list()
            for line in data_file:
                data = line.strip().split()
                lst.append(line)
                for i in range(len(lst)):
                    if number_line == i:
                        return (lst[i])
    except IOError:
        print("File not found")
    

read_line(3,"C:/Users/odeya/Desktop/pythonClass/ex3_text.txt")


    
#TaskB    
def longest_words(file):
    try:
        data_file = open(file)
        final_words = []
        for line in data_file:
            line = line.strip().split()
            for word in line:
                word = word.split(".")
                for w_without_p in word:
                    w_without_p =  w_without_p.split("-")
                    for final_w in  w_without_p:
                        final_words.append(final_w)
        
        sorted_words = sorted(final_words, key = len, reverse= True)
        return sorted_words[:5] 
    except IOError:
        print("File not found")               
                     
longest_words("C:/Users/odeya/Desktop/pythonClass/ex3_text.txt")    