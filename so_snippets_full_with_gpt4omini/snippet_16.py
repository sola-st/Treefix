# Extracted from https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
from numba import vectorize, float64

@vectorize([float64(float64)])
def f(x):
    #x is your line, do something with it, and return a float

