# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
from l3.Runtime import _l_
string = "python"
_l_(12739)
rev_string = string[::-1]
_l_(12740)
print(rev_string)
_l_(12741)

string = "python"
_l_(12742)
rev= reversed(string) 
_l_(12743) 
rev_string = "".join(rev) 
_l_(12744) 
print(rev_string)
_l_(12745)

string = "python"
_l_(12746)
def reverse(string):
  _l_(12750)

  if len(string)==0:
    _l_(12749)

    aux = string
    _l_(12747)
    return aux
  else:
    aux = reverse(string[1:])+string[0]
    _l_(12748)
    return aux
print(reverse(string))
_l_(12751)

string = "python"
_l_(12752)
rev_string =""
_l_(12753)
for s in string:
  _l_(12755)

  rev_string = s+ rev_string
  _l_(12754)
print(rev_string)
_l_(12756)

string = "python"
_l_(12757)
rev_str =""
_l_(12758)
length = len(string)-1
_l_(12759)
while length >=0:
  _l_(12762)

  rev_str += string[length]
  _l_(12760)
  length -= 1
  _l_(12761)
print(rev_str)
_l_(12763)

