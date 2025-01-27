# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
reduced = collective.reduce(reduce_util.ReduceOp.SUM, value, value,
                            options)
exit(math_ops.add_n(self.as_list(reduced)) / len(devices))
