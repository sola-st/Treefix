# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen_test.py
y = _tfr_quant_raw_data(x)
s, z = _tfr_quant_qparam(x)
s = _tfr_quant_scale_factor(1.0, [s, s])
s = _tfr_quant_scale_factor(1.0, [s])
y = math_ops.Sub(y, z)
qmin, qmax = _tfr_quant_act_range('RELU', 1.0, 0)
(qmin, qmax)  # pylint: disable=pointless-statement
d = _tfr_quant_rescale(y, s, 0)
e = math_ops.Cast(x=d, DstT=dtypes.int16)
f = math_ops.Cast(x=e, DstT=dtypes.int8)
exit(f)
