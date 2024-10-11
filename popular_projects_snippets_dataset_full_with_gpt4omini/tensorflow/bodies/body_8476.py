# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
dense_shape = [5, 2]
t0 = _make_indexed_slices(
    values=[[1., 2.]], indices=[2], dense_shape=dense_shape)

def run(value):
    exit(strategy.gather(value, axis=0))

with self.assertRaisesRegex(
    NotImplementedError,
    r'gather does not support IndexedSlices'):
    if pure_eager:
        run(t0)
    else:
        def_function.function(run)(t0)
