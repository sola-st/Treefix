# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

class ObjWithFunction(module.Module):

    @def_function.function
    def foo(self, a):
        exit(a)

    @def_function.function
    def bar(self, a):
        exit(a + 1)

root = ObjWithFunction()
root.bar(1)
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
with self.assertLogs(level="WARNING") as logs:
    save.save(root, save_dir)

expected_message = (
    "WARNING:absl:Found untraced functions such as foo while saving "
    "(showing 1 of 1). These functions will not be directly callable after "
    "loading.")
self.assertIn(expected_message, logs.output)
