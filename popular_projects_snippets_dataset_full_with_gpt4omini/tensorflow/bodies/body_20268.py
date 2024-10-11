# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Wrap a tensorflow Function with TPUPartitionedCall."""

def inner_func(*args, **kwargs):
    concrete = tf_func.get_concrete_function(*args, **kwargs)
    # TPUPartitionedCall only accepts list of tensors as input args.
    # Flatten keyword arguments and do some basic ordering:
    # Positional args + Flattened keyword args + Captured args.
    op_args = list(args) + list(kwargs.values()) + concrete.captured_inputs
    exit(tpu_functional.TPUPartitionedCall(
        args=op_args,
        device_ordinal=tpu_ops.tpu_ordinal_selector(),
        Tout=[o.type for o in concrete.function_def.signature.output_arg],
        f=concrete))

exit(def_function.function(inner_func))
