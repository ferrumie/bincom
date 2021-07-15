import re
from statistics import median
from math import factorial
import operator
from functools import reduce
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="bincom",
    user="postgres",
    password=None,
)
def list_to_dict(list):
    """
    To convert a list to a dictionary with the even elements mapped to the odd elements
    """

    dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return dict


def table_to_dict():
    """
    This function converts the html table from the bincom page
    to a readable dicts with all colours properly arranged
    """
    html_page = open("./python_class_question.html")
    content = html_page.read()
    regex = re.compile(r'<table>(.*)</table>', re.DOTALL)
    match = regex.search(content)
    found_table = match.group(1)

    # saving this in a dictionary
    # we will have {"monday":"..."}
    # store all colours in a list

    days = re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', found_table)
    #  store all the colours in a list
    colours = []
    for i in range(0, len(days), 2):
        colours.append(days[i+1])
    colours = ', '.join(colours).split(", ")
    colour_count = dict((x, colours.count(x)) for x in set(colours))
    return colour_count


def absolute_difference_function(
    list_value): return abs(list_value - mean_val)


# First task, mean colour
# first sum all the values of the colours
colour_count = table_to_dict()
values = colour_count.values()
total = sum(values)
length = len(values)
# average value
mean_val = total/length
# now find the number closest to the mean_val
closest_value = min(values, key=absolute_difference_function)
mean_colour = list(colour_count.keys())[list(
    colour_count.values()).index(closest_value)]
print(f"bincom mean colour is {mean_colour}")


# Second task, most worn colour
# This is literally the key with the highest value in our dictionary
# which is
max_colour = max(colour_count, key=colour_count.get)
print(f"colour worn the most by the staffs is the {max_colour} colour")


# Third task Median Colour
# rearrange the list
li = list(values)
li.sort()
# now find the median
mean_val = median(li)
closest_value = min(values, key=absolute_difference_function)
median_numb = list(colour_count.keys())[list(
    colour_count.values()).index(closest_value)]
print(f"median colour is the {median_numb} colour")


# Task 4 variance
# we need the mean
var_res = sum((xi - mean_val) ** 2 for xi in li) / len(li)
mean_val = var_res
closest_value = min(values, key=absolute_difference_function)
variance_col = list(colour_count.keys())[list(
    colour_count.values()).index(closest_value)]
print(f"median colour is the {variance_col} colour")

# task 5, probability of picking a red
# We can use combinatorics for this
# We need the number of red , and the total colour

# total number of red
red_num = colour_count.get("RED")

# probability of picking a red colour is 
prob = red_num/total
print(f"probability of picking red is {prob*100} percent")

