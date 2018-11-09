# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:51:33 2018

@author: danie
"""

from avl_node import Node
from avl_tree import AVLTree
from rbt_node import RBTNode
from rb_tree import RedBlackTree

#helper function to create a list out of the file for easier tree insertions
def build_list(file):
    alist = []
    
    #opens and reads file line by line
    with open(file) as f:
        alist = f.read().splitlines()
    return alist

#function creates an avl tree out of list given
def build_avl(alist):
    avl_tree = AVLTree()
    
    #line by line splits in order to check if the word starts with an alpha char or not
    for i in range(len(alist)):
        temp_a = alist[i].split(" ")
        temp_w = temp_a[0]
        
        #if it is an alpha char it will create a new list for the embedding and create a node
        if temp_w.isalpha():
            embedding = []
            
            for j in range(len(temp_a -1)):
                embedding.append(temp_a[j+1])
                
            temp_n = Node(temp_w, embedding)
            avl_tree.insert(temp_n)
                

#function that builds a red black tree out of the list given
def build_rb_tree(alist):
    rb_tree = RedBlackTree()
    
    for i in range(len(alist)):
        temp_a = alist[i].split(" ")
        temp_w = temp_a[0]
        
        if temp_w.isalpha():
            embedding = []
            
            for j in range(len(temp_a -1)):
                embedding.append(temp_a[j+1])
                
            temp_n = RBTNode(temp_w, embedding)
            rb_tree.insert(temp_n)

#helper function that calculates the similarity between two given words in a list
def calc_appendix(alist):
    sim_top = alist[0].embedding * alist[1].embedding()
    sim_bot = alist[0].embedding().abs() * alist[1].embedding().abs()
    sim = sim_top // sim_bot
    return sim

#function that reads the appendix file and calculates and returns the similarities
# in a list        
def read_appendix(file):
    alist = []
    
    with open(file) as f:
        alist = f.read().splitlines()
    
    i = 0
    for i in range(len(alist)):
        blist = alist[i].split(' ')
        #calls method that does the actual similarity calculation
        sim = calc_appendix(blist)
        alist[i].append(sim)
    return alist
        
def nodes_in_tree(tree):
    if tree is None:
        return None
    if tree.leftchild():
        left_subt = nodes_in_tree(tree.leftchild() + 1)
    if tree.rightchild():
        right_subt = nodes_in_tree(tree.rightchild() + 1)
    total = left_subt + right_subt
    return total

def height_of_tree(tree):
    if tree is None:
        return None
    if tree.leftchild():
        left = height_of_tree(tree.leftchild() + 1)
    if tree.rightchild():
        right = height_of_tree(tree.rightchild() + 1)
    return max(left, right)
        
def main():
    alist = build_list('glove.6B.50d.txt')
    blist = read_appendix('appendix.txt')
    print("Hi. What kind of tree would you like to use?")
    tree_type = input("1. AVL \n  2. Red-Black")
    
    if tree_type == "1":
        print("planting...")
        print("sprouting...")
        print("growing...")
        print(build_avl(alist))
        
    elif tree_type == "2":
        print("planting...")
        print("sprouting...")
        print("growing...")
        print(build_rb_tree(alist))
        
    else:
        print("You had literally one job.")
        print("I was going to do all the work for you.")
        print("Goodbye.")
        
    for i in range(len(blist)):
        print(blist[i])

main()