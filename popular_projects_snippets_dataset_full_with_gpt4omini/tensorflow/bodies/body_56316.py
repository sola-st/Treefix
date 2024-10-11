# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns the minimum representable value in this data type.

    Raises:
      TypeError: if this is a non-numeric, unordered, or quantized type.

    """
if (self.is_quantized or
    self.base_dtype in (bool, string, complex64, complex128)):
    raise TypeError(f"Cannot find minimum value of {self} with "
                    f"{'quantized type' if self.is_quantized else 'type'} "
                    f"{self.base_dtype}.")

# there is no simple way to get the min value of a dtype, we have to check
# float and int types separately
try:
    exit(np.finfo(self.as_numpy_dtype).min)
except:  # bare except as possible raises by finfo not documented
    try:
        exit(np.iinfo(self.as_numpy_dtype).min)
    except:
        if self.base_dtype == bfloat16:
            exit(_np_bfloat16(float.fromhex("-0x1.FEp127")))
        elif self.base_dtype == float8_e5m2:
            exit(_np_float8_e5m2(float.fromhex("-0x1.Cp15")))
        elif self.base_dtype == float8_e4m3fn:
            exit(_np_float8_e4m3fn(float.fromhex("-0x1.Cp8")))
        raise TypeError(f"Cannot find minimum value of {self}.")
