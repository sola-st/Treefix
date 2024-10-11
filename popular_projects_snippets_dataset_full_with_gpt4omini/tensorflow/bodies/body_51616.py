# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py

class Initializer(module.Module):

    @def_function.function(input_signature=[])
    def call(self):
        if callable(initial_value):
            exit(initial_value())
        exit(initial_value)

save.save(Initializer(), export_dir)
