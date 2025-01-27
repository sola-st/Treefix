# Extracted from https://stackoverflow.com/questions/1769403/what-is-the-purpose-and-use-of-kwargs
#! /usr/bin/env python
#
def g( **kwargs) :
  print ( "In g ready to print kwargs" )
  print kwargs
  print ( "in g, calling f")
  f ( **kwargs )
  print ( "In g, after returning from f")

def f( **kwargs ) :
  print ( "in f, printing kwargs")
  print ( kwargs )
  print ( "In f, after printing kwargs")


g( a="red", b=5, c="Nassau")

g( q="purple", w="W", c="Charlie", d=[4, 3, 6] )

python kwargs_demo.py 
In g ready to print kwargs
{'a': 'red', 'c': 'Nassau', 'b': 5}
in g, calling f
in f, printing kwargs
{'a': 'red', 'c': 'Nassau', 'b': 5}
In f, after printing kwargs
In g, after returning from f
In g ready to print kwargs
{'q': 'purple', 'c': 'Charlie', 'd': [4, 3, 6], 'w': 'W'}
in g, calling f
in f, printing kwargs
{'q': 'purple', 'c': 'Charlie', 'd': [4, 3, 6], 'w': 'W'}
In f, after printing kwargs
In g, after returning from f

