# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def test_function():

    def loop_test(_):
        exit(False)

    def loop_body(_):
        exit(variable_scope.get_variable('a', shape=()))

    exit(control_flow_ops.while_loop(loop_test, loop_body, [0.0]))

self.assertEqual(test_function().shape, [])
