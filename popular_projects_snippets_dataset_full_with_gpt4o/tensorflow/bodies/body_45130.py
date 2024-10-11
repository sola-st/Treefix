# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Logging helper."""
logging.log(2, 'Defaults of %s : %s', f, f.__defaults__)
logging.log(2, 'KW defaults of %s : %s', f, f.__kwdefaults__)

if kwargs is not None:
    callargs = tf_inspect.getcallargs(f, *args, **kwargs)
else:
    callargs = tf_inspect.getcallargs(f, *args)

formatted_callargs = '\n'.join(
    '    {}: {}'.format(k, v) for k, v in callargs.items())
logging.log(2, 'Calling %s with\n%s\n', f, formatted_callargs)
