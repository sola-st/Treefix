# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
if self._test_conversion_params["_tftrt_convert_function"]:
    for func_def in function_protos:
        if not func_def.signature.name.startswith("TRTEngine"):
            for key, value in self._test_conversion_params.items():
                self.assertIn(key, func_def.attr,
                              "key %s not found in func_def.attr" % key)
                if isinstance(value, str):
                    self.assertEqual(func_def.attr[key].s, compat.as_bytes(value))
                elif isinstance(value, bool):
                    self.assertEqual(func_def.attr[key].b, value)
                elif isinstance(value, int):
                    self.assertEqual(func_def.attr[key].i, value)
