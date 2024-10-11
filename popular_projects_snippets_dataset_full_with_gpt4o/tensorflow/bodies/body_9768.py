# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
if not graph.is_fetchable(op):
    raise errors.InaccessibleTensorError(
        f'Operation {op.name} has been marked as not fetchable. Typically '
        'this happens when it is defined in another function or code block. '
        'Use return values, explicit Python locals or TensorFlow collections '
        'to access it.')
