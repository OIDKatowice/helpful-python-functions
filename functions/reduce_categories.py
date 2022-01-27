# Version: Python 3.8.8 64-bit ('base': conda)

def reduce_categories(character_column, n = 10):
    ''' Reduces the number of unique categories/values present in a character/string variable to n, with the nth value as "other" '''
    top_n_values = character_column.value_counts()[0:n].index.values
    new_values = [x if x in top_n_values else "other" for x in character_column]
    return new_values
