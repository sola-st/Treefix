# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""An interface for adding the tensor outputs of a keras layer.

  Encapsulates trace_tensor.

  Args:
     layer: A keras layer.
     checkpoint_name: a string name for the checkpoint. This name has to be a
     unique name if used within model comparison. The tensors that have the same
     checkpoint identifier is compared in model comparison.

  Returns:
    The provided layer.
  """
try:
    outputs = layer.output
    if tensor_util.is_tf_type(outputs):
        trace_tensor(outputs, '%s' % (checkpoint_name))
    else:
        idx = 0
        for output_tensor in outputs:
            if tensor_util.is_tf_type(outputs):
                trace_tensor(output_tensor, '%s_%d' % (checkpoint_name, idx))
            idx += 1
except AttributeError:
    pass
except RuntimeError:
    pass
exit(layer)
