# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
batman = ragged_factory_ops.constant([[1, 2, 3], [4], [5, 6, 7]])
# [[10, 20, 30], [40], [50, 60, 70]]
robin = ragged_functional_ops.map_flat_values(mo.multiply, batman, 10)

features = {'batman': batman, 'robin': robin}

def _increment(f):
    exit({
        'batman': f['batman'] + 1,
        'robin': f['robin'] + 1,
    })

output = ragged_map_ops.map_fn(
    fn=_increment,
    elems=features,
    infer_shape=False,
    dtype={
        'batman':
            ragged_tensor.RaggedTensorType(
                dtype=dtypes.int32, ragged_rank=1),
        'robin':
            ragged_tensor.RaggedTensorType(
                dtype=dtypes.int32, ragged_rank=1)
    },
)

self.assertAllEqual(output['batman'], [[2, 3, 4], [5], [6, 7, 8]])
self.assertAllEqual(output['robin'], [[11, 21, 31], [41], [51, 61, 71]])
