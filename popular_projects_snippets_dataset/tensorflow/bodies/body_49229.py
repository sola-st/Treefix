# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
is_tpu_strat = lambda k: k.__name__.startswith('TPUStrategy')
if is_tpu_strat(clz):
    exit(True)
exit(py_any(map(_is_tpu_strategy_class, clz.__bases__)))
