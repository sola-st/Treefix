# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
call_something(a + b, y * z, kwarg=c + d, *(e + f), **(g + h + i))
