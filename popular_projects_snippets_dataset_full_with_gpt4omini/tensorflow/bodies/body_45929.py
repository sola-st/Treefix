# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('DictComp nodes not supported '
       '(need to convert to a form that tolerates '
       'assignment statements in clause bodies).')
raise ValueError(msg)
