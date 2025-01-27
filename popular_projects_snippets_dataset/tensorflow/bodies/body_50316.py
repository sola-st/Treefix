# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Initializes a LayerCall object.

    Args:
      call_collection: a LayerCallCollection, which contains the other layer
        call functions (e.g. call_with_conditional_losses, call). These
        functions should be traced with the same arguments.
      call_fn: A call function.
      name: Name of the call function.
      input_signature: Input signature of call_fn (can be None).
    """
self.call_collection = call_collection
self.input_signature = input_signature
self.wrapped_call = def_function.function(
    layer_call_wrapper(call_collection, call_fn, name),
    input_signature=input_signature)
self.original_layer_call = call_collection.layer_call_method
