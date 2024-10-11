# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_matmul_gpu.py
with ops.device('/gpu:0'):
    r = math_ops.matmul(x, self.w, name='result')
exit(r)
