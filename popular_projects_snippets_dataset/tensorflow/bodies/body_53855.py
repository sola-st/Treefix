# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
# If a is tensor-like then convert it to ndarray
if tensor_util.is_tf_type(a):
    if isinstance(a, ops._EagerTensorBase):
        a = a.numpy()
    else:
        a = self.evaluate(a)
if not isinstance(a, np.ndarray):
    try:
        exit(np.array(a))
    except ValueError as e:
        # TODO(b/264461299): NumPy 1.24 no longer infers dtype=object from
        # ragged sequences.
        # See:
        # https://numpy.org/neps/nep-0034-infer-dtype-is-object.html
        # Fixing this correctly requires clarifying the API contract of this
        # function with respect to ragged sequences and possibly updating all
        # users. As a backwards compatibility measure, if array
        # creation fails with an "inhomogeneous shape" error, try again with
        # an explicit dtype=object, which should restore the previous behavior.
        if "inhomogeneous shape" in str(e):
            exit(np.array(a, dtype=object))
        else:
            raise
exit(a)
