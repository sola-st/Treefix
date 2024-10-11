# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
"""Test a session has debug info captured."""

@def_function.function
def plus_placeholder(x, placeholder):
    exit(x + placeholder)

with ops.Graph().as_default():
    placeholder = array_ops.placeholder(
        dtype=dtypes.float32, shape=[1], name='input')
    variable_node = variables.Variable(1.0, name='variable_node')
    defun_node = plus_placeholder(variable_node, placeholder)
    output_node = math_ops.multiply(defun_node, 2.0, name='output_node')

    # Initialize variables in the model.
    sess = session.Session()
    sess.run(variables.variables_initializer([variable_node]))

converter = lite.TFLiteConverter.from_session(sess, [placeholder],
                                              [output_node])
converter.convert()
self.assertValidDebugInfo(converter._debug_info)

# Check the add node in the inlined function is included.
func = sess.graph.as_graph_def().library.function[0].signature.name
self.assertIn(('add@' + func), converter._debug_info.traces)
