# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
tape, eager_inputs, eager_outputs = tape_cache.pop(compat.as_bytes(token))
exit(tape.gradient(eager_outputs, eager_inputs, output_gradients=dy))
