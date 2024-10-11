# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
inp = constant_op.constant(2.0, shape=[100, 32], name="in")
w = constant_op.constant(4.0, shape=[10, 100], name="w")
wx = math_ops.matmul(w, inp, name="wx")
wx_print = logging_ops.Print(wx, [w, w, w])
wx_grad = gradients_impl.gradients(wx, w)[0]
wx_print_grad = gradients_impl.gradients(wx_print, w)[0]
wxg = self.evaluate(wx_grad)
wxpg = self.evaluate(wx_print_grad)
self.assertAllEqual(wxg, wxpg)
