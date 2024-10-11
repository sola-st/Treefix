# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py

def nested_template():
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

tmpl1 = template.make_template("s1", nested_template)
tmpl2 = template.make_template("s1", nested_template)

v1, v2 = tmpl1()
v3, v4 = tmpl1()
v5, v6 = tmpl2()

# The second invocation of tmpl1 should reuse the variables
# created in the first invocation.
self.assertIs(v1, v3)
self.assertIs(v2, v4)
for v, w in zip(tmpl1.variables, [v1, v2]):
    self.assertIs(v, w)
for v, w in zip(tmpl1.trainable_variables, [v1, v2]):
    self.assertIs(v, w)
self.assertEqual(len(tmpl1.non_trainable_variables), 0)

# tmpl1 and tmpl2 should not share variables.
self.assertIsNot(v1, v5)
self.assertIsNot(v2, v6)
for v, w in zip(tmpl2.variables, [v5, v6]):
    self.assertIs(v, w)
for v, w in zip(tmpl2.trainable_variables, [v5, v6]):
    self.assertIs(v, w)
self.assertEqual(len(tmpl2.non_trainable_variables), 0)
self.assertEqual("s1/nested/dummy:0", v1.name)
self.assertEqual("s1/nested_1/dummy:0", v2.name)
self.assertEqual("s1_1/nested/dummy:0", v5.name)
self.assertEqual("s1_1/nested_1/dummy:0", v6.name)

self.assertEqual(["nested", "nested_1"], list(tmpl1._trackable_children()))
