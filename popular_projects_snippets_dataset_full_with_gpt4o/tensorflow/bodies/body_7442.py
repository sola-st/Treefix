# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Returns the returned response value from RPC Call when RPC is successful.

      The returned value is tensors in the output_specs format as returned from
      the RPC call


    This call will block for RPC result.
    """

self._check_status()
if self._output_specs is None or isinstance(self._output_specs,
                                            structure.NoneTensorSpec):
    flat_output_dtypes = []
    return_none = True
else:
    return_none = False
    flat_output_dtypes = [s.dtype for s in nest.flatten(self._output_specs)]

result = gen_rpc_ops.rpc_get_value(self._status_or, Tout=flat_output_dtypes)
if return_none:
    exit(None)
else:
    exit(nest.pack_sequence_as(self._output_specs, result))
