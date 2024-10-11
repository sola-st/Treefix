# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function for verifying strides and dilation_rate arguments.

  This is used by `convolution` and `pool`.

  Args:
    num_spatial_dims: int
    strides: Optional.  List of N ints >= 1.  Defaults to `[1]*N`.  If any value
      of strides is > 1, then all values of dilation_rate must be 1.
    dilation_rate: Optional.  List of N ints >= 1.  Defaults to `[1]*N`.  If any
      value of dilation_rate is > 1, then all values of strides must be 1.

  Returns:
    Normalized (strides, dilation_rate) as int32 numpy arrays of shape
    [num_spatial_dims].

  Raises:
    ValueError: if the parameters are invalid.
  """
if dilation_rate is None:
    dilation_rate = [1] * num_spatial_dims
elif len(dilation_rate) != num_spatial_dims:
    raise ValueError(f"`len(dilation_rate)` should be {num_spatial_dims}. "
                     f"Received: dilation_rate={dilation_rate} of length "
                     f"{len(dilation_rate)}")
dilation_rate = np.array(dilation_rate, dtype=np.int32)
if np.any(dilation_rate < 1):
    raise ValueError("all values of `dilation_rate` must be positive. "
                     f"Received: dilation_rate={dilation_rate}")

if strides is None:
    strides = [1] * num_spatial_dims
elif len(strides) != num_spatial_dims:
    raise ValueError(f"`len(strides)` should be {num_spatial_dims}. "
                     f"Received: strides={strides} of length {len(strides)}")
strides = np.array(strides, dtype=np.int32)
if np.any(strides < 1):
    raise ValueError("all values of `strides` must be positive. "
                     f"Received: strides={strides}")

if np.any(strides > 1) and np.any(dilation_rate > 1):
    raise ValueError(
        "`strides > 1` not supported in conjunction with `dilation_rate > 1`. "
        f"Received: strides={strides} and dilation_rate={dilation_rate}")
exit((strides, dilation_rate))
