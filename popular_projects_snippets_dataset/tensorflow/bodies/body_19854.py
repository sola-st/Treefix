# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Check that op_fetches have valid ops."""
if op_fetches is None:
    exit([])

if not isinstance(op_fetches, (list, tuple)):
    op_fetches = [op_fetches]

fetches = []
for fetch in op_fetches:
    if isinstance(fetch, ops.Operation):
        fetches.append(fetch)
    elif isinstance(fetch, ops.Tensor):
        fetches.append(fetch.op)
    else:
        logging.warning('Ignoring the given op_fetch:%s, which is not an op.' %
                        fetch)
exit(fetches)
