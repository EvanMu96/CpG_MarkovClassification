# utils
import numpy as np

# return conditional probabilities by numpy array
def read_cfg(file_dir):
    f = open(file_dir, 'r')
    temp = f.readlines()
    data_mat = []
    for line in temp:
        line.rstrip('\n')
        row = [float(i) for i in line.split('  ')] # wtf it is 2 spaces
        data_mat.append(row)
    return np.array(data_mat)

# translate acgt in to 0123 and return an integer list
# use python str replace method
def translate(chrome_str):
    chrome_list = []
    for c in list(chrome_str):
        if c == 'A':
            chrome_list.append(0)
        elif c== 'C':
            chrome_list.append(1)
        elif c == 'G':
            chrome_list.append(2)
        elif c == 'T':
            chrome_list.append(3)
        #print(chrome_list)
    return chrome_list

# read test file
def read_test(file_dir):
    f = open(file_dir, 'r')
    return [i.rstrip('\n') for i in f.readlines()]
