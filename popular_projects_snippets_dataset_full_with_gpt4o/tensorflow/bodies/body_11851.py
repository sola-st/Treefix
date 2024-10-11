# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
for j in range(unroll_cnt):
    q, count = sturm_step(start + j, q, count)
exit((start + unroll_cnt, q, count))
