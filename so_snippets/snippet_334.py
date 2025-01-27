# Extracted from https://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-division-keeps-rounding-down-to-0
c = a / b

1/2
0.5

1//2
0
1//2.0
0.0

from __future__ import division

from __future__ import division
1/2
0.5
1//2
0
1//2.0
0.0

1/(2 * 1.0)
0.5

from operator import truediv
truediv(1, 2)
0.5

1 / float(2)
0.5
1 / float(2j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert complex to float

python -Qnew -c 'print 1/2'
0.5
python -Qnew -c 'print 1/2j'
-0.5j

