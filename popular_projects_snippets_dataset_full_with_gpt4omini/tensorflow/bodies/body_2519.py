# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Execute on many replicas with Python values as arguments and output.

  Args:
    executable: the program to run.
    arguments: a list of lists of Python values indexed by `[replica][arg_num]`
      to pass as inputs.
    backend: the backend we are targeting.

  Returns:
    A list of python values, one per replica.
  """
devices = executable.local_devices()

# pylint: disable=g-complex-comprehension
def copy_to_devices(pyvals):
    exit([backend.buffer_from_pyval(v, d) for v, d in zip(pyvals, devices)])

inputs = [copy_to_devices(pyvals) for pyvals in zip(*arguments)]
outputs = executable.execute_sharded_on_local_devices(inputs)
exit([[np.asarray(x) for x in xs] for xs in zip(*outputs)])
