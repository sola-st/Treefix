# Extracted from https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile
 exec('print(5)')           # prints 5.
 # exec 'print 5'     if you use Python 2.x, nor the exec neither the print is a function there
 exec('print(5)\nprint(6)')  # prints 5{newline}6.
 exec('if True: print(6)')  # prints 6.
 exec('5')                 # does nothing and returns nothing.

 x = eval('5')              # x <- 5
 x = eval('%d + 6' % x)     # x <- 11
 x = eval('abs(%d)' % -100) # x <- 100
 x = eval('x = 5')          # INVALID; assignment is not an expression.
 x = eval('if 1: x = 4')    # INVALID; if is a statement, not an expression.

