#!/usr/bin/env python

import pandas as pd
import csv

''' This is a python module for the online learning community.'''
df_blp = pd.read_csv("./csv/learning_path_bus.csv")
df_clp = pd.read_csv('./csv/learning_path_cre.csv')
df_tlp = pd.read_csv('./csv/learning_path_tech.csv')
def llp_bus_csv():
    '''This is a method that returns a CSV file of all the learning paths in the business category.'''
    return(df_blp)

def llp_bus_courses():
    '''This is a method that returns a list of all the learning paths in the business category.'''
    return(df_blp['name'].tolist())

def llp_bus_skills():
    '''This is a method that returns a list of all the skills in the business category.'''
    return(df_blp.groupby('skills').count().index.tolist())

def llp_bus_dict():
    '''This is a method that returns a dictionary of skills and their learning paths in the business category.'''
    return(df_blp.groupby('skills')['name'].apply(list).to_dict())

def llp_cre_csv():
    '''This is a method that returns a CSV file of all the learning paths in the creative category.'''
    return(df_clp)

def llp_cre_courses():
    '''This is a method that returns a list of all the learning paths in the creative category.'''
    return(df_clp['name'].tolist())

def llp_cre_skills():
    '''This is a method that returns a list of all the skills in the creative category.'''
    return(df_clp.groupby('skills').count().index.tolist())

def llp_cre_dict():
    '''This is a method that returns a dictionary of skills and their learning paths in the creative category.'''
    return(df_clp.groupby('skills')['name'].apply(list).to_dict())

def llp_tech_csv():
    '''This is a method that returns a CSV file of all the learning paths in the creative category.'''
    return(df_tlp)

def llp_tech_courses():
    '''This is a method that returns a list of all the learning paths in the creative category.'''
    return(df_tlp['name'].tolist())

def llp_tech_skills():
    '''This is a method that returns a list of all the skills in the creative category.'''
    return(df_tlp.groupby('skills').count().index.tolist())

def llp_tech_dict():
    '''This is a method that returns a dictionary of skills and their learning paths in the creative category.'''
    return(df_tlp.groupby('skills')['name'].apply(list).to_dict())
