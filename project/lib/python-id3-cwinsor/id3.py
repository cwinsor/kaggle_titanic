# This class implements ID3 Decision Tree from Quinlan 1986

import numpy as np
#from PIL import Image
import os
from scipy.stats import entropy
import pandas as pd

class ID3(object):
        
    def __init__(self):
        self.chosen_attribute = None
        self.is_leaf = False
        self.subtree = {}


    # Examples are the training examples
    # Target_attribute is the attribute to be predicted
    # Attributes is a list of other attirbutes to be tested by decision tree
    # Returns a decision tree
    def fit(self, examples, target_attribute, attributes):

        assert isinstance(examples, pd.core.frame.DataFrame), 'Argument of wrong type!'
        assert isinstance(target_attribute, str), 'Argument of wrong type!'
        assert isinstance(attributes, list), 'Argument of wrong type!'

        print("=================")
        print("creating tree - attribute list = {}".format(attributes))

        # if all examples are <val>, return the single-node tree with that label = VAL
        if examples[target_attribute].nunique() == 1:
            self.is_leaf = True
            self.class_value = examples[target_attribute][0]
            return self

        # if attributes is empty, return the single-node tree with label = most common att value
        if len(attributes) == 0:
            self.is_leaf = True
            self.class_value = examples[target_attribute].value_counts().index[0]
            return self

        # find the attribute that best classifies examples
        gain_by_att = {}

        for att in attributes:
            print("----------------------------")
            print(att)
            count = examples[att].count()

            gain = 0.0
            for attval in examples[att].unique():
                print("  " + attval)
                
                # Create a subset data frame where attribute = att value x
                df1 = examples[att] == attval
                df2 = examples[df1]
                print(df2)
                subcount = df2[att].count()
                print("     " + str(subcount) + " of " + str(count))

                # Calculate entropy on the target attribute
                value,counts = np.unique(df2[target_attribute], return_counts=True)
                entr = entropy(counts, base=2)
                print("     entropy = " + str(entr))

                # Accumulate gain (weighted) - the second term of equation
                gain += (subcount/count)*entr

            gain_by_att[att] = gain

        # find the attribute with greatest gain
        print(gain_by_att)
        self.chosen_attribute = min(gain_by_att, key=gain_by_att.get)
        print(self.chosen_attribute)

        # remove the chosen attribute
        attributes.remove(self.chosen_attribute)

        # for each value of attribute - add a new subtree
        for attval in examples[self.chosen_attribute].unique():

            # Create a data frame with elements where attribute = att value x
            df1 = examples[self.chosen_attribute] == attval
            df2 = examples[df1]

            # check to confirm there is at least one example in the data frame
            count = df2[self.chosen_attribute].count()
            assert count>0, print("blast - there are no examples in the data frame for attval {}".format(attval))

            self.subtree[attval] = ID3()
            self.subtree[attval].fit(examples, self.chosen_attribute, attributes)




    def traverse(self, indent):
        print("{}{} {}".format(indent, self.is_leaf, self.chosen_attribute))
        for subroot in self.subtree:
            self.subtree[subroot].traverse(indent+"  ")

