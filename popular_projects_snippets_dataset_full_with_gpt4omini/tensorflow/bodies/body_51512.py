# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
signature = [tensor_spec.TensorSpec(None, dtypes.string)]
exit(def_function.function(input_signature=signature)(
    lambda x: table.lookup(x)))  # pylint: disable=unnecessary-lambda
