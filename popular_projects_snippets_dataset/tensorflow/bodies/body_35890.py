# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
self.assertAllClose([0., 1., 2., 3.], _IotaInitializer([4]))
self.assertAllClose([[0., 1.], [0., 10.], [0., 100.], [0., 1000.]],
                    _IotaInitializer([4, 2]))
with self.cached_session():
    vs = partitioned_variables.create_partitioned_variables([13, 5], [3, 1],
                                                            _IotaInitializer)
    self.evaluate(variables.global_variables_initializer())
    slice0 = _IotaInitializer([5, 5])
    slice1 = _IotaInitializer([4, 5])
    slice2 = _IotaInitializer([4, 5])
    val = array_ops.concat(vs, 0)
    self.assertAllClose(slice0 + slice1 + slice2, val)
    self._TestSaveSpec(vs, ["13 5 0,5:0,5", "13 5 5,4:0,5", "13 5 9,4:0,5"])
