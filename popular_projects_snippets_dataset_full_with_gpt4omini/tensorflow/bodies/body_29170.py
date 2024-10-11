# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
devices = ["/cpu:0"]
if test_util.is_gpu_available():
    devices.append("/gpu:0")
for device in devices:
    with ops.device(device):
        # With value
        opt1 = optional_ops.Optional.from_value((1.0, 2.0))
        opt2 = optional_ops.Optional.from_value((3.0, 4.0))

        add_tensor = math_ops.add_n(
            [opt1._variant_tensor, opt2._variant_tensor])
        add_opt = optional_ops._OptionalImpl(add_tensor, opt1.element_spec)
        self.assertAllEqual(self.evaluate(add_opt.get_value()), (4.0, 6.0))

        # Without value
        opt_none1 = optional_ops.Optional.empty(opt1.element_spec)
        opt_none2 = optional_ops.Optional.empty(opt2.element_spec)
        add_tensor = math_ops.add_n(
            [opt_none1._variant_tensor, opt_none2._variant_tensor])
        add_opt = optional_ops._OptionalImpl(add_tensor, opt_none1.element_spec)
        self.assertFalse(self.evaluate(add_opt.has_value()))
