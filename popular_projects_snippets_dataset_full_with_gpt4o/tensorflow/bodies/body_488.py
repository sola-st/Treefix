# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
class FooWarningSpec(ast_edits.NoUpdateSpec):
    """Usages of function attribute foo() prints out a warning."""

    def __init__(self):
        ast_edits.NoUpdateSpec.__init__(self)
        self.function_warnings = {"*.foo": (ast_edits.WARNING, "not good")}

texts = ["object.foo()", "get_object().foo()",
         "get_object().foo()", "object.foo().bar()"]
for text in texts:
    (_, report, _), _ = self._upgrade(FooWarningSpec(), text)
    self.assertIn("not good", report)

# Note that foo() won't result in a warning, because in this case foo is
# not an attribute, but a name.
false_alarms = ["foo", "foo()", "foo.bar()", "obj.run_foo()", "obj.foo"]
for text in false_alarms:
    (_, report, _), _ = self._upgrade(FooWarningSpec(), text)
    self.assertNotIn("not good", report)
