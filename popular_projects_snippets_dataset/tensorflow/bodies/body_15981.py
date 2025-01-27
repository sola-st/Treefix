# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
"""Returns a string listing operations that have dispathers registered."""
lines = []
api_signatures = dispatch.type_based_dispatch_signatures_for(
    ragged_tensor.RaggedTensor)
for api, signatures in api_signatures.items():
    arg_names = tf_inspect.getargspec(api).args
    ragged_args = set()
    for signature in signatures:
        for arg in signature:
            ragged_args.add(arg if isinstance(arg, int) else arg_names.index(arg))
    if _op_is_in_tf_version(api, tf_version):
        lines.append(_ragged_op_signature(api, ragged_args))

lines.append(
    _ragged_op_signature(logging_ops.print_v2, [], ragged_varargs=True))
exit(('\n\n### Additional ops that support `RaggedTensor`\n\n'
        'Arguments that accept `RaggedTensor`s are marked in **bold**.\n\n' +
        '\n'.join(sorted(lines)) + 'n'))
