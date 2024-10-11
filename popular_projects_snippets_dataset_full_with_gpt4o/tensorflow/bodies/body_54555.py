# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Enable or disable soft device placement.

  If enabled, ops can be placed on different devices than the device explicitly
  assigned by the user. This potentially has a large performance cost due to an
  increase in data communication between devices.

  Some cases where soft_device_placement would modify device assignment are:
    1. no GPU/TPU implementation for the OP
    2. no GPU devices are known or registered
    3. need to co-locate with reftype input(s) which are from CPU
    4. an OP can not be compiled by XLA.  Common for TPU which always requires
         the XLA compiler.

  For TPUs, if this option is true, a feature called automatic outside
  compilation is enabled. Automatic outside compilation will move uncompilable
  ops within a TPU program to instead run on the host. This can be used when
  encountering compilation failures due to unsupported ops.

  Note: by default soft device placement is enabled when running in eager mode
  (for convenience) and disabled in graph mode (for performance).

  Args:
    enabled: A boolean indicating whether to enable soft placement.
  """
context.context().soft_device_placement = enabled
