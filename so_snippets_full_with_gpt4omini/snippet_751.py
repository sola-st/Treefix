# Extracted from https://stackoverflow.com/questions/28930465/what-is-the-difference-between-flatten-and-ravel-functions-in-numpy
import numpy
a = numpy.array([[1,2],[3,4]])

r = numpy.ravel(a)
f = numpy.ndarray.flatten(a)  

print(id(a))
print(id(r))
print(id(f))

print(r)
print(f)

print("\nbase r:", r.base)
print("\nbase f:", f.base)

---returns---
140541099429760
140541099471056
140541099473216

[1 2 3 4]
[1 2 3 4]

base r: [[1 2]
 [3 4]]

base f: None

import numpy
a1 = numpy.array([[1,2],[3,4]])
a2 = a1.copy()
id(a2.base), id(a1.base)

(140735713795296, 140735713795296)

