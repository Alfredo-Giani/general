# -*- coding: utf-8 -*-
"""
rank engine. given a query string, this is broken into meaningful tokens and the tokens are
compared against the catalogue.

a basis to a ranking engine is to provide some sort of distance measurement between the query string
and the database.

one would initially model the data space as a 3 dimensional space eg category (axis 1) title (axis 2)
description (axis 3). distance between query and catalog item is calculated in this space.

the metric is complicated by several factors. Firstly, it is not isometric e.g. a short distance from 
aa certain category might be more relevant, in ranking terms, than a short distance from a certain title

secondly, axis might not be orthogonal. certain categories could see a constistent higher likelihood
of certain tokens (words) in the description, therefore said words are highly correlated to said category


this is at first sight a complex problem for which I do not have enough previous knowledge and
therefore it is not easy to find a solution that is sound. 

a possible strategy for the sake of this exercise is to find the best title description match
by counting the number of occurrences of the query tokens in each COMBINED title-description.

the highest count is the winner. this determines the category and we can use the category tree 
to provide ranked suggestions. (e.g. items belonging to the same subcategory are ranked first)

second and further winners in the title/description match can be used to provide a secondary
ranking based on title/description only. this may not be in the same category as the winner


there is an issue when transforming distance as a measure of relevance to rank, which is an ordinal
quantity where relative distances (how "far" from the query is the ranked item). A possible solution
which I have encountered during my experience in Mitsubishi (video content similarity ranking) 
is to arrange results in a two-dimensional constellation where distances are respected. that would
provide also a natural way to organise categories and multiple category rankings (e.g. each category
an "arm" of the constellation centred on the query)

"""

import pandas as pd
import numpy as np



# TBD: break a query string in tokens (separators: space, comma, semicolon, etc)
def break_tokens(query_string):
    
    
    tokens = query_string
    
    return tokens


#remove tokens that are not relevant (e.g. conjunctions)
def filter_tokens(tokens):
    
    filtered_tokens =[]
    discard_list = ['the']
    
    
    for t in tokens:
        
        if t not in discard_list:
            filtered_tokens.append(t)
            
    if len(filtered_tokens)==0: #no relevant tokens
        print('no relevant tokens found in query!\n")
        
        
    return filtered_tokens

#TBD: category tree is organised as a class inheritance tree with one parent and many children. 
#    eg the category clothing/girls has one parent (clothing) and few children clothing/girls/sports
#    and clothing/girls/leisure
def extract_category_tree(database):
    
    #return a hash table category-> list of parents that navigates the category tree bottom up.
    
    e.g. 

    
# MAIN BODY    

data = pd.read_csv('D:\\Users\\alfre\\Sportable\\GitHubDepots\\relevance-code-test\\products.csv')

query_string = input('Enter query: ')

tokens_list = break_tokens(query_string)

filtered_tokens_list = filter_tokens(tokens_list)


num_of_items = data.shape[0]

rank_by_cat = np.zeros(shape = (num_of_items,))
rank_by_title = np.zeros(shape = (num_of_items,))
rank_by_descr = np.zeros(shape = (num_of_items,))

total_rank = np.zeros(shape = (num_of_items,))


# find the item in stock which has the best category match. This allows the navigation 
# of the category tree for category-based recommendation. E.g. show all products belonging
# to a specific category and its parents on the category tree.


def calc_cat_rank(token_list,category):
    
    rank by category. search into the token list and  

for it in range(num_of_items):
    rank_by_cat[it] = calc_cat_rank(token_list, data.iloc[[it]]['category'])
        
best_match_by_cat = np.argmax(rank_by_cat)


 find the best natural language match in the title.     

    
    rank_by_title[it] = calc_title_rank(token_list, data.iloc[[it]]['title'])
    rank_by_descr[it] = calc_descr_rank(token_list, data.iloc[[it]]['description'])











    
