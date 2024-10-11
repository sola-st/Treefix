# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_variable_on_tpu.py
with ops.device('/device:TPU:0'):
    w = self.w.read_value()
r = math_ops.matmul(x, w, name='result')
exit(r)
