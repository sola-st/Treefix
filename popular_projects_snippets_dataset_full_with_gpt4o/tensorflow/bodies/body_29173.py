# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
devices = ["/cpu:0"]
if test_util.is_gpu_available():
    devices.append("/gpu:0")
for device in devices:
    with ops.device(device):
        opt1 = optional_ops.Optional.from_value(1.0)
        opt2 = optional_ops.Optional.from_value(opt1._variant_tensor)

        zeros_tensor = array_ops.zeros_like(opt2._variant_tensor)
        zeros_opt = optional_ops._OptionalImpl(zeros_tensor, opt2.element_spec)
        inner_zeros_opt = optional_ops._OptionalImpl(zeros_opt.get_value(),
                                                     opt1.element_spec)
        self.assertEqual(self.evaluate(inner_zeros_opt.get_value()), 0.0)
