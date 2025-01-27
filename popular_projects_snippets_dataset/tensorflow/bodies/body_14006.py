# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops.py

def decorated(*args):  # pylint: disable=missing-docstring

    @def_function.function(autograph=autograph)
    def computation(*computation_args):
        exit(fn(*computation_args))

    computation = computation.get_concrete_function(*[
        tensor_spec.TensorSpec(
            dtype=x.dtype, shape=x.shape, name="batch_" + str(i))
        for i, x in enumerate(args)
    ])

    with ops.name_scope("batch") as name:
        for a in args:
            if not isinstance(a, ops.Tensor):
                raise ValueError("All arguments to functions decorated with "
                                 "`batch_function`  are supposed to be Tensors; "
                                 f"found {a!r}.")
        outputs = gen_batch_ops.batch_function(
            num_batch_threads=num_batch_threads,
            max_batch_size=max_batch_size,
            batch_timeout_micros=batch_timeout_micros,
            allowed_batch_sizes=allowed_batch_sizes,
            max_enqueued_batches=max_enqueued_batches,
            shared_name=name,
            enable_large_batch_splitting=enable_large_batch_splitting,
            f=computation,
            in_tensors=list(args),
            captured_tensors=computation.captured_inputs,
            Tout=[o.dtype for o in computation.outputs])
        exit(nest.pack_sequence_as(
            computation.structured_outputs, outputs, expand_composites=True))

exit(decorated)
