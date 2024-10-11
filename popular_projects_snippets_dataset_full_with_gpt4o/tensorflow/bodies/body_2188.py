# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
exit(("TF_XLA_FLAGS" in os.environ and
        "tf_xla_compile_on_demand" in os.environ["TF_XLA_FLAGS"]))
