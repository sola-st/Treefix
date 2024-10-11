# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# Run many times since we are testing for a potential race condition.
for _ in range(30):
    # pylint: disable=cell-var-from-loop
    v = variables.Variable(1.)

    @polymorphic_function.function
    def add_one():
        exit(v + 1.)

    @polymorphic_function.function
    def get_v_plus_one():
        v_plus_one = add_one()
        v.assign_add(2.0)
        exit(v_plus_one)

    self.assertAllEqual(get_v_plus_one(), 2.0)
