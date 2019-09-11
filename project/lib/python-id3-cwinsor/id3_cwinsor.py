# This class implements ID3 Decision Tree from Quinlan 1986

import numpy as np
from PIL import Image
import os
from scipy.stats import entropy


class ID3(object):
        
    def __init__(self):
        self.decision_attribute = None
        self.is_leaf = True


    # Examples are the training examples
    # Target_attribute is the attribute to be predicted
    # Attributes is a list of other attirbutes to be tested by decision tree
    # Returns a decision tree
    def fit(self, examples, target_attribute, attributes):

        # if all examples are <val>, return the single-node tree with that label = VAL
        if examples[target_attribute].nunique() == 1:
            self.is_leaf = True
            self.class_value = examples[target_attribute][0]
            return self

        # if attributes is empty, return the single-node tree with label = most common att value
        if attributes.size == 0:
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
            for attval in d[att].unique():
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
        chosen_attribute = min(gain_by_att, key=gain_by_att.get)
        print(chosen_attribute)

        # remove the chosen attribute
        attributes.remove(chosen_attribute)

        # for each value of attribute - add a new node
        for attval in examples[chosen_attribute].unique():

            # Create a data frame with elements where attribute = att value x
            df1 = examples[att] == attval
            df2 = examples[df1]

            # check to confirm there is at least one example in the data frame
            assert(false "foobar")
            assert(true "foobar2")

            id3_instance = ID3_class()
            id3_instance.fit(examples, chosen_attribute, attributes)




