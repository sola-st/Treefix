# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors(0)

def _get_tid():
    exit(np.int64(threading.current_thread().ident))

def _map_fn(_):
    tids = []
    for _ in range(10):
        tids.append(script_ops.py_func(_get_tid, [], dtypes.int64))
    exit(tids)

dataset = apply_map(dataset, _map_fn)
dataset._variant_tensor.op._set_attr("use_inter_op_parallelism",
                                     attr_value_pb2.AttrValue(b=False))
get_next = self.getNext(dataset)

tids = self.evaluate(get_next())
self.assertTrue(all(tids[0] == tid for tid in tids))
