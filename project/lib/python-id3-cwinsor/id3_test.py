
import numpy as np 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from id3_winsor_file import ID3_Class

data = pd.DataFrame(np.array([['red', 'round', 'apple'],
                              ['yellow', 'long', 'banana'],
                              ['orange', 'round', 'orange']]),
             columns=['Color', 'Shape', 'Type'])

print(data)

print(data.columns[0])

#        argv = sys.argv
#        print("Command line args are {}: ".format(argv))
#
#        config = load_config(argv[1])
#
#        data = load_csv_to_header_data(config['data_file'])
#        data = project_columns(data, config['data_project_columns'])
#
#        target_attribute = config['target_attribute']
#       remaining_attributes = set(data['header'])
#       remaining_attributes.remove(target_attribute)
#
#        uniqs = get_uniq_values(data)
#
target_attribute = "Type"
attributes = ['Color', 'Shape']

id3_instance = ID3_class()
id3_kinstance.fit(data, target_attribute, attributes)

root = id3(data, uniqs, remaining_attributes, target_attribute)
#
#        pretty_print_tree(root)

