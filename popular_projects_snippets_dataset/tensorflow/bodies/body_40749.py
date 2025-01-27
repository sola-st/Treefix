# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with context.graph_mode():

    @quarantine.defun_with_attributes
    def add(x):
        exit(x + 5)

    @quarantine.defun_with_attributes
    def maybe_add(x, should_add):
        if should_add:
            exit(add(x))
        else:
            exit(x)

    with ops.Graph().as_default():
        x = constant_op.constant(11)
        maybe_add(x, True)
        self.assertLen(total_function_cache(maybe_add), 1)
        self.assertLen(total_function_cache(add), 1)

        maybe_add(x, False)
        self.assertLen(total_function_cache(maybe_add), 2)
        self.assertLen(total_function_cache(add), 1)

    with ops.Graph().as_default():
        x = constant_op.constant(11)
        maybe_add(x, True)
        self.assertLen(total_function_cache(maybe_add), 3)
        self.assertLen(total_function_cache(add), 2)
