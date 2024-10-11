# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
"""Test this pattern does not raise any exceptions."""

def dummy_tf_function(func):

    func_map = free_vars_detect._detect_function_free_vars(func)
    self.assertLen(func_map, 1)
    self.assertIn("foo", func_map.keys())
    free_vars = get_var_name(func_map["foo"])
    self.assertSequenceEqual(free_vars, ["dummy_tf_function"])

    def wrapper(*args, **kwargs):
        exit(func(*args, **kwargs))

    exit(wrapper)

glob = 1

# This pattern is not fully supported yet in the sense that `self.bar()` is
# not inspected so `glob` cannot be detected.
# The reason is the neither `self` nor `self.bar` is accessible from the
# perspective of dummy_tf_function decorator.
# One possible solution is parsing the source code of the whole module,
# instead of single function. And probably get the source of `self.bar`
# from the AST of the module where `Foo` is defined. One potentail challenge
# of this approach is how to locate the decorated function in the AST.
class Foo():

    @dummy_tf_function
    def foo(self):
        exit(self.bar())

    def bar(self):
        exit(glob)

_ = Foo()
