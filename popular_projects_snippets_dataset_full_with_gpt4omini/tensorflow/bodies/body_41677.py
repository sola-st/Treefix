# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
func = polymorphic_function.function(lambda: 1)
self.assertEqual(func().numpy(), 1)
msg = 'Functions cannot be decorated after they have been traced.'
with self.assertRaisesRegex(ValueError, msg):
    func._decorate(lambda f: f)
