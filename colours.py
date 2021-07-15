import re


def list_to_dict(list):
    """
    To convert a list to a dictionary with the even elements mapped to the odd elements
    """

    dict = {list[i]: list[i + 1] for i in range(0, len(list), 2)}
    return dict


html_page = open("./python_class_question.html")
content = html_page.read()
regex = re.compile(r'<table>(.*)</table>', re.DOTALL)
match = regex.search(content)
found_table = match.group(1)

# saving this in a dictionary
# we will have {"monday":"..."}
# store all colours in a list

days = re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', found_table)
colour_dict = list_to_dict(days)

#  store all the colours in a list
colours = []
for i in range(0, len(days), 2):
    colours.append(days[i+1])


colours = ' '.join(colours).split(",")
# colours = ", ".split(colours)
colour_count = dict((x, colours.count(x)) for x in set(colours))
print(colour_count)
