# CpG island classification
import numpy as np
#get cmd variable
import sys
from utils import read_cfg, translate, read_test

class Markov_Chain:
    def __init__(self, inside_mat, outside_mat):
        self.inside_mat  = np.log2(inside_mat)
        self.outside_mat = np.log2(outside_mat)
        
    
    def predict(self, str_chrome):
        inside_val = 0
        outside_val = 0
        str_chrome = translate(str_chrome)
        for i in range(len(str_chrome)-1):
            inside_val += self.inside_mat[str_chrome[i], str_chrome[i+1]]
            outside_val += self.outside_mat[str_chrome[i], str_chrome[i+1]]
        return str(inside_val - outside_val)+'\n'


if __name__ == "__main__":
    inside_file_dir = sys.argv[1]
    outside_file_dir = sys.argv[2]
    test_file = sys.argv[3]
    inside_mat = read_cfg(inside_file_dir)
    outside_mat = read_cfg(outside_file_dir)

    test_cases = read_test(test_file)

    model = Markov_Chain(inside_mat, outside_mat)

    test_result = []

    for case in test_cases:
        test_result.append(model.predict(case))
    
    outf = open('result_{}.txt'.format(test_file[0:-4]), 'x')
    outf.writelines(test_result)