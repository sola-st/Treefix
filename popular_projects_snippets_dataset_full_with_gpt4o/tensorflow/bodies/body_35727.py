# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/critical_section_test.py
cs0 = critical_section_ops.CriticalSection()
cs1 = critical_section_ops.CriticalSection()
v = resource_variable_ops.ResourceVariable(0.0, name="v")
cs0.execute(lambda: v + 1)
# It's OK for the same CriticalSection to access this resource.
cs0.execute(lambda: v - 1)
# It's *not* OK for a different CriticalSection to access it by
# default.
with self.assertRaisesRegex(ValueError,
                            "requested exclusive resource access"):
    cs1.execute(lambda: v + 1)
# It's not even OK if the second call doesn't request exclusive access.
with self.assertRaisesRegex(ValueError,
                            "requested exclusive resource access"):
    cs1.execute(lambda: v + 1, exclusive_resource_access=False)

v2 = resource_variable_ops.ResourceVariable(0.0, name="v2")
cs0.execute(lambda: v2 + 1, exclusive_resource_access=False)
# It's OK if neither requests exclusive resource access.
cs1.execute(lambda: v2 + 1, exclusive_resource_access=False)

# It's not OK if the second request requires exclusive resource
# access.
with self.assertRaisesRegex(ValueError,
                            "requested exclusive resource access"):
    cs1.execute(lambda: v2 + 1)
