# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
self.assertEqual("arg_42", function_type.sanitize_arg_name("42"))
self.assertEqual("a42", function_type.sanitize_arg_name("a42"))
self.assertEqual("arg__42", function_type.sanitize_arg_name("_42"))
self.assertEqual("a___", function_type.sanitize_arg_name("a%$#"))
self.assertEqual("arg____", function_type.sanitize_arg_name("%$#"))
self.assertEqual("foo", function_type.sanitize_arg_name("foo"))
self.assertEqual("arg_96ab_cd___53",
                 function_type.sanitize_arg_name("96ab.cd//?53"))
