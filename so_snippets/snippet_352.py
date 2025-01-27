# Extracted from https://stackoverflow.com/questions/1009860/how-to-read-process-command-line-arguments
try:
   _, arg1, arg2, arg3, *_ = sys.argv + [None] * 2
except ValueError:
   print("Not enough arguments", file=sys.stderr) # unhandled exception traceback is meaningful enough also
   exit(-1)

Traceback (most recent call last):
  File "test.py", line 3, in <module>
    _, arg1, arg2, arg3, *_ = sys.argv + [None] * 2
ValueError: not enough values to unpack (expected at least 4, got 3)

