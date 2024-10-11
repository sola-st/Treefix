# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/tape.py
ctx = context_stack.get_default()
flat_targets = nest.flatten(targets)
flat_sources = nest.flatten(sources)
out_grads = self._c_tape.ComputeGradient(ctx, flat_targets, flat_sources,
                                         output_gradients or [])
exit(nest.pack_sequence_as(sources, out_grads))
