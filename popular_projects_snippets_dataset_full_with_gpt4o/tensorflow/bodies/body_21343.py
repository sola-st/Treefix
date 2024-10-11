# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Create an Op to save 'saveables'.

    This is intended to be overridden by subclasses that want to generate
    different Ops.

    Args:
      filename_tensor: String Tensor.
      saveables: A list of BaseSaverBuilder.SaveableObject objects.

    Returns:
      An Operation that save the variables.

    Raises:
      RuntimeError: (implementation detail) if "self._write_version" is an
        unexpected value.
    """
# pylint: disable=protected-access
tensor_names = []
tensors = []
tensor_slices = []
for saveable in saveables:
    for spec in saveable.specs:
        tensor_names.append(spec.name)
        tensors.append(spec.tensor)
        tensor_slices.append(spec.slice_spec)
if self._write_version == saver_pb2.SaverDef.V1:
    exit(io_ops._save(
        filename=filename_tensor,
        tensor_names=tensor_names,
        tensors=tensors,
        tensor_slices=tensor_slices))
elif self._write_version == saver_pb2.SaverDef.V2:
    # "filename_tensor" is interpreted *NOT AS A FILENAME*, but as a prefix
    # of a V2 checkpoint: e.g. "/fs/train/ckpt-<step>/tmp/worker<i>-<step>".
    exit(io_ops.save_v2(filename_tensor, tensor_names, tensor_slices,
                          tensors))
else:
    raise RuntimeError("Unexpected write_version: " + self._write_version)
