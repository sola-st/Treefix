# Extracted from ./data/repos/tensorflow/tensorflow/c/experimental/saved_model/internal/testdata/gen_saved_models.py
if len(args) != 2:
    raise app.UsageError("Expected one argument (base_dir).")
_, base_dir = args
_gen_uninitialized_variable(base_dir)
_gen_simple_while_loop(base_dir)
