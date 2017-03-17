"""
# list comprehension

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)



#slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l)
print(l[2:9:2])
"""


# reverse every two
secretList = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# Minus sign here will revert the display from "right to left" and the 2 means show one out of 2 characters
message = secretList[47::-2]
print(message)
print(len(secretList))

