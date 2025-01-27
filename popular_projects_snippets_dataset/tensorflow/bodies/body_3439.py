# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type_test.py
original = function_type.FunctionType([
    function_type.Parameter("x",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, None),
    function_type.Parameter("y",
                            function_type.Parameter.POSITIONAL_OR_KEYWORD,
                            False, None),
    function_type.Parameter("z", function_type.Parameter.KEYWORD_ONLY,
                            False, None)
])
cloned = pickle.loads(pickle.dumps(original))
self.assertEqual(original, cloned)
