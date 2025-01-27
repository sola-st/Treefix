# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
with ops.colocate_with(self._coloc_op):
    ret = get_fn()

indices = list(range(len(self._dtypes)))  # Hard coded
exit(self._get_return_value(ret, indices))
