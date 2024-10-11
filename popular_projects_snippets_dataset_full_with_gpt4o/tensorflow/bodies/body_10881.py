# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clustering_ops.py
# If the input dataset size is smaller than the number of centers
# remaining, choose the entire input dataset as centers. This can happen
# with mini-batch. Otherwise, sample the batch according to the provided
# sampler.
exit(control_flow_ops.cond(self._num_data <= self._num_remaining,
                             lambda: array_ops.concat(self._inputs, 0),
                             sampler))
