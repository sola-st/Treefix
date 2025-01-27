# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple", a="Bad string")
    self.assertIn(
        "Expected int32 passed to parameter 'a' of op 'Simple', "
        "got 'Bad string' of type 'str' instead.", str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple", a=self.Tensor(dtypes.string))
    self.assertIn(
        "Input 'a' of 'Simple' Op has type string "
        "that does not match expected type of int32.", str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple", a=6, extra="bogus")
    self.assertIn("Simple got unexpected keyword arguments: extra",
                  str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op(
            "Simple", a=6, extra1="bogus", extra2="also_bogus")
    self.assertIn(
        "Simple got unexpected keyword arguments: extra1, "
        "extra2", str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple")
    self.assertIn("No argument for input a", str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple", wrong=7)
    self.assertIn("No argument for input a", str(cm.exception))

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("Simple", a={"label": 1})
    self.assertIn(
        "Expected int32 passed to parameter 'a' of op 'Simple', "
        "got {'label': 1} of type 'dict' instead.", str(cm.exception))
