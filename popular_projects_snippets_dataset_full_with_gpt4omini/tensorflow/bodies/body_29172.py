# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
devices = ["/cpu:0"]
if test_util.is_gpu_available():
    devices.append("/gpu:0")
for device in devices:
    with ops.device(device):
        # With value
        opt = optional_ops.Optional.from_value((1.0, 2.0))
        zeros_tensor = array_ops.zeros_like(opt._variant_tensor)
        zeros_opt = optional_ops._OptionalImpl(zeros_tensor, opt.element_spec)
        self.assertAllEqual(self.evaluate(zeros_opt.get_value()), (0.0, 0.0))

        # Without value
        opt_none = optional_ops.Optional.empty(opt.element_spec)
        zeros_tensor = array_ops.zeros_like(opt_none._variant_tensor)
        zeros_opt = optional_ops._OptionalImpl(zeros_tensor,
                                               opt_none.element_spec)
        self.assertFalse(self.evaluate(zeros_opt.has_value()))
