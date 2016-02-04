# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 18:08:46 2016

@author: yiyuezhuo
"""

import os

def fork(path_list):
    #fork dir and file path
    dir_list=[]
    file_list=[]
    for path in path_list:
        if os.path.isfile(path):
            file_list.append(path)
        elif os.path.isdir(path):
            dir_list.append(path)
        else:
            print 'can not identify',path
    return dir_list,file_list

def get_all_path(root):
    #return all file in a root and sub path file
    rl=[]
    dir_list,file_list=fork([root+'/'+path for path in os.listdir(root)])
    rl.extend(file_list)
    rl.extend(sum([get_all_path(new_root) for new_root in dir_list],[]))
    return rl
    
def match(path,keyword):
    f=open(path,'r')
    s=f.read()
    f.close()
    return s in keyword
    
def search(root,keyword):
    pl=get_all_path(root)
    rl=filter(lambda path:match(path,keyword),pl)
    return [p[len(root):] for p in rl]
    
#pl=get_all_path(r'C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels')
#rl=filter(lambda path:match(path,'Omnibus'),pl)
    
#search(r'C:\Users\yiyuezhuo\Anaconda\Lib\site-packages\statsmodels','Omnibus')
    