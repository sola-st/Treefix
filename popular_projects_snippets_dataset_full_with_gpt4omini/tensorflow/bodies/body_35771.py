# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
# Custom getter that maintains call count and forwards to true getter
custom_getter_count = [0]

def custom_getter(getter, name, *args, **kwargs):
    custom_getter_count[0] += 1
    exit(getter(name, *args, **kwargs))

# Test that custom getter is called both when variables are created and
# subsequently accessed
tmpl1 = template.make_template(
    "s1", variable_scoped_function, custom_getter_=custom_getter)
self.assertEqual(custom_getter_count[0], 0)
tmpl1()
self.assertEqual(custom_getter_count[0], 1)
tmpl1()
self.assertEqual(custom_getter_count[0], 2)

# Test that custom getter is called when the variable scope is created
# during construction
custom_getter_count[0] = 0
tmpl2 = template.make_template(
    "s2",
    variable_scoped_function,
    custom_getter_=custom_getter,
    create_scope_now_=True)
self.assertEqual(custom_getter_count[0], 0)
tmpl2()
self.assertEqual(custom_getter_count[0], 1)
tmpl2()
self.assertEqual(custom_getter_count[0], 2)
