# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
summaries = make_quantile_summaries(float_columns, example_weights,
                                    self._eps)
summary_op = quantile_add_summaries(self.resource_handle, summaries)
exit(summary_op)
