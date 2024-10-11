# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
class MyModule(module.Module):

    @def_function.function(input_signature=[])
    def foo(self):
        exit(constant_op.constant([1]))

saved_model.save(MyModule(), 'ram://my_module')

loaded = saved_model.load('ram://my_module')
self.assertAllEqual(loaded.foo(), [1])
