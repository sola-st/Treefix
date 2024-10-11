# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
self._client_handle, methods = gen_rpc_ops.rpc_client(
    shared_name=name,
    server_address=address,
    list_registered_methods=list_registered_methods,
    timeout_in_ms=timeout_in_ms)
if context.executing_eagerly():
    self._handle_deleter = resource_variable_ops.EagerResourceDeleter(
        handle=self._client_handle, handle_device=self._client_handle.device)
else:
    raise NotImplementedError(
        "Client creation is supported only in eager mode.")
self._server_address = address
self._method_registry = {}
for method in methods.numpy():
    m = rpc_pb2.RegisteredMethod()
    m.ParseFromString(method)
    output_specs = nested_structure_coder.decode_proto(m.output_specs)
    input_specs = nested_structure_coder.decode_proto(m.input_specs)
    self._method_registry[m.method] = output_specs
    # TODO(ishark): Perhaps doc string can also be taken as input during
    # function registration.
    doc_string = "RPC Call for " + m.method + " method to server " + address
    self._add_method(m.method, output_specs, input_specs, self._client_handle,
                     doc_string)
