# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
"""Method for making RPC calls to remote server.

    This invokes RPC to the server, executing the registered method_name
    remotely.
    Args:
      method_name: Remote registered method to invoke
      args: List of arguments for the registered method.
      output_specs: Output specs for the output from method.
         For example, if tf.function is: @tf.function(input_signature=[
           tf.TensorSpec([], tf.int32), tf.TensorSpec([], tf.int32) ])
          def multiply_fn(a, b): return tf.math.multiply(a, b)
        output_spec is: tf.TensorSpec((), tf.int32)  If you have access to TF
          Function, the output specs can be generated
       from tf.function by calling: output_specs =
         tf.nest.map_structure(tf.type_spec_from_value,
         tf_function.get_concrete_function().structured_outputs  If output_specs
         are not provided, flattened list of tensors will be returned in
         response.
      timeout_in_ms: Timeout for this call. If 0, default client timeout will be
        used.

    Returns:
      An instance of `StatusOrResult` class with the following available
      methods.
        * `is_ok()`:
            Returns True of RPC was successful.
        * `get_error()`:
            Returns TF error_code and error message for the RPC.
        * `get_value()`:
            Returns the returned value from remote TF function execution
            when RPC is successful.

      Calling any of the above methods will block till RPC is completed and
      result is available.
    """
raise NotImplementedError("Must be implemented in inherited classes.")
