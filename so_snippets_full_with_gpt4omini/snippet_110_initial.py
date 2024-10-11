# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
from l3.Runtime import _l_
string = "python"
_l_(853)
rev_string = string[::-1]
_l_(854)
print(rev_string)
_l_(855)

string = "python"
_l_(856)
rev= reversed(string) 
_l_(857) 
rev_string = "".join(rev) 
_l_(858) 
print(rev_string)
_l_(859)

string = "python"
_l_(860)
def reverse(string):
  _l_(864)

  if len(string)==0:
    _l_(863)

    aux = string
    _l_(861)
    return aux
  else:
    aux = reverse(string[1:])+string[0]
    _l_(862)
    return aux
print(reverse(string))
_l_(865)

string = "python"
_l_(866)
rev_string =""
_l_(867)
for s in string:
  _l_(869)

  rev_string = s+ rev_string
  _l_(868)
print(rev_string)
_l_(870)

string = "python"
_l_(871)
rev_str =""
_l_(872)
length = len(string)-1
_l_(873)
while length >=0:
  _l_(876)

  rev_str += string[length]
  _l_(874)
  length -= 1
  _l_(875)
print(rev_str)
_l_(877)

