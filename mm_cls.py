# CpG island classification
import numpy as np
#get cmd variable
import sys
# I wrote some basic utilities into a library
from utils import read_cfg, translate, read_test

# define the markov chain model class
class Markov_Chain:
    def __init__(self, inside_mat, outside_mat):
        # transform into log
        self.inside_mat  = np.log2(inside_mat)
        self.outside_mat = np.log2(outside_mat)
        
    # predict method
    def predict(self, str_chrome):
        inside_val = 0  # I neglected the prior probabilities because I don't know that.
        outside_val = 0
        str_chrome = translate(str_chrome)
        # compute summation of inside and outside log(conditional probabilities)
        for i in range(len(str_chrome)-1):
            inside_val += self.inside_mat[str_chrome[i], str_chrome[i+1]]
            outside_val += self.outside_mat[str_chrome[i], str_chrome[i+1]]
        result = inside_val - outside_val
        if result > 0:
            # positive
            return str(result)+'  inside\n'
        else:
            # negative
            return str(result)+'  outside\n'


if __name__ == "__main__":
    # read arguments
    inside_file_dir = sys.argv[1]
    outside_file_dir = sys.argv[2]
    test_file = sys.argv[3]
    inside_mat = read_cfg(inside_file_dir)
    outside_mat = read_cfg(outside_file_dir)
    # read test cases
    test_cases = read_test(test_file)
    # define a markov chain model
    model = Markov_Chain(inside_mat, outside_mat)
    test_result = []
    # run test cases
    for case in test_cases:
        test_result.append(model.predict(case))
    # write the result to the file
    outf = open('result_{}.txt'.format(test_file[0:-4]), 'x')
    outf.writelines(test_result)