'''Write a function to compute 5/0 and use try/except to catch the exceptions'''
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")

