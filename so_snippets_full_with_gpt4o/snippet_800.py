# Extracted from https://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes
#!/usr/local/bin/python
# by Daniel Rosengren modified by e-satis

import sys, time
stdout = sys.stdout

BAILOUT = 16
MAX_ITERATIONS = 1000

class Iterator(object) :

    def __init__(self):

        print 'Rendering...'
        for y in xrange(-39, 39):
            stdout.write('\n')
            for x in xrange(-39, 39):
                if self.mandelbrot(x/40.0, y/40.0) :
                    stdout.write(' ')
                else:
                    stdout.write('*')


    def mandelbrot(self, x, y):
        cr = y - 0.5
        ci = x
        zi = 0.0
        zr = 0.0

        for i in xrange(MAX_ITERATIONS) :
            temp = zr * zi
            zr2 = zr * zr
            zi2 = zi * zi
            zr = zr2 - zi2 + cr
            zi = temp + temp + ci

            if zi2 + zr2 > BAILOUT:
                return i

        return 0

t = time.time()
Iterator()
print '\nPython Elapsed %.02f' % (time.time() - t)

#!/usr/local/bin/python
# by Daniel Rosengren, modified by e-satis
"""
Module doctring
"""


import time
from sys import stdout

BAILOUT = 16
MAX_ITERATIONS = 1000

def mandelbrot(dim_1, dim_2):
    """
    function doc string
    """
    cr1 = dim_1 - 0.5
    ci1 = dim_2
    zi1 = 0.0
    zr1 = 0.0

    for i in xrange(MAX_ITERATIONS) :
        temp = zr1 * zi1
        zr2 = zr1 * zr1
        zi2 = zi1 * zi1
        zr1 = zr2 - zi2 + cr1
        zi1 = temp + temp + ci1

        if zi2 + zr2 > BAILOUT:
            return i

    return 0

def execute() :
    """
    func doc string
    """
    print 'Rendering...'
    for dim_1 in xrange(-39, 39):
        stdout.write('\n')
        for dim_2 in xrange(-39, 39):
            if mandelbrot(dim_1/40.0, dim_2/40.0) :
                stdout.write(' ')
            else:
                stdout.write('*')


START_TIME = time.time()
execute()
print '\nPython Elapsed %.02f' % (time.time() - START_TIME)

./python_mandelbrot.py:4:11: E401 multiple imports on one line
./python_mandelbrot.py:10:1: E302 expected 2 blank lines, found 1
./python_mandelbrot.py:10:23: E203 whitespace before ':'
./python_mandelbrot.py:15:80: E501 line too long (108 characters)
./python_mandelbrot.py:23:1: W291 trailing whitespace
./python_mandelbrot.py:41:5: E301 expected 1 blank line, found 3

C: 15: Line too long (108/80)
C: 61: Line too long (85/80)
C:  1: Missing docstring
C:  5: Invalid name "stdout" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 10:Iterator: Missing docstring
C: 15:Iterator.__init__: Invalid name "y" (should match [a-z_][a-z0-9_]{2,30}$)
C: 17:Iterator.__init__: Invalid name "x" (should match [a-z_][a-z0-9_]{2,30}$)

[...] and a very long report with useful stats like :

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+

