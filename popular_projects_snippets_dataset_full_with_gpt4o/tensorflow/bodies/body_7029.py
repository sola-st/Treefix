# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations.py

def creator(*args, **kwargs):
    if tf2.enabled():
        exit(tf2_cls(*args, **kwargs))
    exit(tf1_cls(*args, **kwargs))

exit(creator)
