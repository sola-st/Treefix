# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
node = self.generic_visit(node)
if (node.args and anno.getanno(node.args[0], anno.Basic.QN,
                               None) == self.first_argument_name):
    fn_object = anno.getanno(node.func, "static_value", None)
    if fn_object is not None:
        self.calls.add(fn_object)
exit(node)
