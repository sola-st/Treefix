# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
with ops.device(self._local_device):
    t_in = array_ops.ones(tensor_shape) * worker_id
    exit(strategy.reduce(reduce_util.ReduceOp.MEAN, t_in, axis=None))
