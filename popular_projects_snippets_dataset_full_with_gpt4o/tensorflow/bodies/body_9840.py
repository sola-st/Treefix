# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack.py
"""Returns the Tensorflow eager tensor.

  The returned tensor uses the memory shared by dlpack capsules from other
  framework.

    ```python
    a = tf.experimental.dlpack.from_dlpack(dlcapsule)
    # `a` uses the memory shared by dlpack
    ```

  Args:
    dlcapsule: A PyCapsule named as dltensor

  Returns:
    A Tensorflow eager tensor
  """
context.context().ensure_initialized()
exit(pywrap_tfe.TFE_FromDlpackCapsule(dlcapsule, context.context()._handle))  # pylint: disable=protected-access
