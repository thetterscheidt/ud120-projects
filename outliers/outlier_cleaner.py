#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import operator    
    
    errors = [a-b for a,b in zip(predictions, net_worths)]    
    data = sorted(zip(ages, net_worths, errors))
#    data.sort(key=operator.itemgetter(2)) NOTE: .sort not valid in Python 3.7
    cleaned_data = data[:int(len(predictions)*0.9)]
    
    return cleaned_data

