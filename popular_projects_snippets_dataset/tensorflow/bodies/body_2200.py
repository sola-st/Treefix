# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_test.py
steps = 5
for dtype in self.float_types:
    with self.session(), self.test_scope():
        val0, val1 = self.equivAdagradTest_FtrlPart(steps, dtype)
    with self.session(), self.test_scope():
        val2, val3 = self.equivAdagradTest_AdagradPart(steps, dtype)

self.assertAllCloseAccordingToType(val0, val2, rtol=1e-4, half_rtol=1e-2)
self.assertAllCloseAccordingToType(val1, val3, rtol=1e-4, half_rtol=1e-2)
