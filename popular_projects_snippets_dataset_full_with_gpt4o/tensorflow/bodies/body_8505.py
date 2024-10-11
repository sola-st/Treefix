# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_gather_test.py
dense_shape = [5, 2]
t0 = _make_indexed_slices(
    values=[[1., 2.]], indices=[2], dense_shape=dense_shape)

def replica_fn(value):
    ctx = ds_context.get_replica_context()
    exit(ctx.all_gather(value, axis=0))

with self.assertRaisesRegex(
    NotImplementedError,
    r'all_gather does not support IndexedSlices'):
    if not pure_eager:
        strategy.run(def_function.function(replica_fn), args=(t0,))
    else:
        strategy.run(replica_fn, args=(t0,))
