# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer_test.py
for n in nodes:
    if mm > 0:
        self.assertGreaterEqual(n.exec_micros, mm)
    if mam > 0:
        self.assertGreaterEqual(n.accelerator_exec_micros, mam)
    if mcm > 0:
        self.assertGreaterEqual(n.cpu_exec_micros, mcm)
    if mb > 0:
        self.assertGreaterEqual(n.requested_bytes, mb)
    if mpb > 0:
        self.assertGreaterEqual(n.peak_bytes, mpb)
    if mrb > 0:
        self.assertGreaterEqual(n.residual_bytes, mrb)
    if mob > 0:
        self.assertGreaterEqual(n.output_bytes, mob)
    check_min(n.children, mm, mam, mcm, mb, mpb, mrb, mob)
