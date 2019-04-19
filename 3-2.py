#311499917 shaked astemker

from functools import reduce

def data_preprocessing(data,min_val,max_val):
    "func thet help fix the list and put the averge where is not have date, of the 2 from his sides do averge"
    filter_ = list(filter(lambda x: x=='' or min_val<= x <= max_val ,(map(lambda x: int(x) if x!='' else '',data.split(',')))))
    return list(map(lambda i: int(((filter_[i - 1] + filter_[i + 1])/2)) if filter_[i] == '' else filter_[i],range(len(filter_))))


def data_preprocessing_histogram(data,min_val,max_val):
    "give back the histogram of the date"
    map_filter_averge = data_preprocessing(data,min_val,max_val)
    histogram = set()#new
    #set(map(lambda x: histogram.add((x,map_filter_averge.count(x))),map_filter_averge))
    histogram = set(map(lambda x:(x, len(tuple(filter(lambda y: x==y,map_filter_averge)))),map_filter_averge))
    return histogram

def data_preprocessing_range(data,min_val,max_val):
    "give back the averge and min and max data"
    map_filter_averge = data_preprocessing(data,min_val,max_val)
    return (min(map_filter_averge),round(reduce(lambda x,y:x+y,map_filter_averge) / len(map_filter_averge),2),max(map_filter_averge))

'''
data = "1,1,,100,3,5,5,5,,1,2,3"
min_val,max_val = 0,10
histogram = data_preprocessing_histogram(data,min_val,max_val)
getrange = data_preprocessing_range(data,min_val,max_val)
print(histogram)
print(getrange)
'''






