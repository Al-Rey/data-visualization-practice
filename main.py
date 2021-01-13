import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == "__main__":
    col_names = ['Style']
    data = pd.read_csv('archive\\ramen-ratings.csv', usecols=col_names).fillna('NA')

    styles_list = data.Style.tolist()

    values_dict = {}
    style_types = values_dict.keys()

    # make the dictionaries of the different styles of ramen
    for style in styles_list:
        if style in style_types:
            values_dict[style] += 1
        else:
            values_dict[style] = 1

    # print the contents of the dictionary and the list of the differents styles of 
    print("Dicitonary of Styles:")
    print(values_dict)
    print(style_types)
    
    # list of all the counts for each of the different styles
    style_count = values_dict.values()

    # make a list of the names
    types = []
    for name in style_types:
        types.append(name)

    # make a list of the count of the style types
    count = []
    for cnt in style_count:
        count.append(cnt)

    # create the actual graph
    fig = plt.figure()
    y_pos = np.arange(len(types))

    plt.bar(y_pos, count, align='center', alpha=0.5)

    plt.xticks(y_pos, types)
    plt.ylabel('Count')
    plt.title('Ramen Styles')
    
    plt.show()