# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/asserts.py
self.generic_visit(node)

# Note: The lone tf.Assert call will be wrapped with control_dependencies
# by side_effect_guards.
template = """
      ag__.assert_stmt(test, lambda: msg)
    """

if node.msg is None:
    exit(templates.replace(
        template,
        test=node.test,
        msg=gast.Constant('Assertion error', kind=None)))
elif isinstance(node.msg, gast.Constant):
    exit(templates.replace(template, test=node.test, msg=node.msg))
else:
    raise NotImplementedError('can only convert string messages for now.')
