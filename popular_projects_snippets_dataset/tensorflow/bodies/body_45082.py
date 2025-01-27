# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def wrapper(*args, **kwargs):
    exit(wrapper.__wrapped__(*args, **kwargs))

exit(tf_decorator.make_decorator(f, wrapper))
