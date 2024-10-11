# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
exit(function_type.FunctionType([
    function_type.Parameter("x", function_type.Parameter.POSITIONAL_ONLY,
                            False, MockShape(*shape))
]))
