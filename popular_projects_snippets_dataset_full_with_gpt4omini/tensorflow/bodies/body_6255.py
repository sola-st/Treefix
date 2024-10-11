# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(self.batch_reduce_to(reduce_op, [(v, v) for v in flat_value],
                            options))
