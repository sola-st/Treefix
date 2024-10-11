# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
devices = ["/cpu:0"]
if test_util.is_gpu_available():
    devices.append("/gpu:0")
for device in devices:
    with ops.device(device):
        opt1 = optional_ops.Optional.from_value([1, 2.0])
        opt2 = optional_ops.Optional.from_value([3, 4.0])
        opt3 = optional_ops.Optional.from_value((5.0, opt1._variant_tensor))
        opt4 = optional_ops.Optional.from_value((6.0, opt2._variant_tensor))

        add_tensor = math_ops.add_n(
            [opt3._variant_tensor, opt4._variant_tensor])
        add_opt = optional_ops._OptionalImpl(add_tensor, opt3.element_spec)
        self.assertEqual(self.evaluate(add_opt.get_value()[0]), 11.0)

        inner_add_opt = optional_ops._OptionalImpl(add_opt.get_value()[1],
                                                   opt1.element_spec)
        self.assertAllEqual(inner_add_opt.get_value(), [4, 6.0])
