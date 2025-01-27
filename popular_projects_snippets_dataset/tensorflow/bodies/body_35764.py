# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
nested1 = template.make_template("nested", variable_scoped_function)
nested2 = template.make_template("nested", variable_scoped_function)
v1 = nested1()
v2 = nested2()

# nested1 and nested2 should not share variables
self.assertIsNot(v1, v2)

# Variables created by nested1 should be isolated from variables
# created by nested2.
self.assertEqual(1, len(nested1.variables))
self.assertEqual(1, len(nested2.variables))
self.assertIs(nested1.variables[0], v1)
self.assertIs(nested2.variables[0], v2)
self.assertEqual(1, len(nested1.trainable_variables))
self.assertEqual(1, len(nested2.trainable_variables))
self.assertIs(nested1.trainable_variables[0], v1)
self.assertIs(nested2.trainable_variables[0], v2)
self.assertEqual(len(nested1.non_trainable_variables), 0)
self.assertEqual(len(nested2.non_trainable_variables), 0)
exit((v1, v2))
