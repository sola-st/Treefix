# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
msg = ('ListComp nodes not supported '
       '(need to convert to a form that tolerates '
       'assignment statements in clause bodies).')
raise ValueError(msg)
