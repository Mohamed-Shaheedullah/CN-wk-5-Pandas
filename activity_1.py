
example_data = [6, 2, 9, 12, 24, 78, 5, 24, 44, 24, 67, 24, 34, 99, 85, 7, 43, 13, 26, 25, 77, 62, 53]

def my_range(datalist):
    the_range = max(datalist) - min(datalist)
    return the_range

print(my_range(example_data))

def my_mean(datalist):
    the_mean = sum(datalist) / len(datalist)
    return round(the_mean, 2)

print(f" Thew mean is {my_mean(example_data)}")

# https://www.nobledesktop.com/learn/python/mode-in-python

def my_mode(datalist):
    y={}
    
    for a in datalist:
        if not a in y:
            y[a] = 1
        else:
            y[a] += 1
    return [g for g, l in y.items() if l == max(y.values())]

print(f"The mode is {my_mode(example_data)}")


# https://www.codingem.com/python-calculate-median/

def my_median(datalist):
    sorted_list = sorted(datalist)
    list_len = len(sorted_list)

    middle = (list_len -1) // 2

    if middle % 2:
        return sorted_list[middle]
    else:
        return (sorted_list[middle] + sorted_list[middle + 1]) / 2.0

print(f"The median is {my_median(example_data)}") 
   
