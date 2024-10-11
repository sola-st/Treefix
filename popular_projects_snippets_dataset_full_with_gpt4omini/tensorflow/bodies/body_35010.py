# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/student_t_test.py
s_p = zip(sample_vals, pdf_vals)
prev = (sample_vals.min() - 1000, 0)
total = 0
for k in sorted(s_p, key=lambda x: x[0]):
    pair_pdf = (k[1] + prev[1]) / 2
    total += (k[0] - prev[0]) * pair_pdf
    prev = k
self.assertNear(1., total, err=err)
