# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
exit(("  inputs: (\n" + "    " + ",\n    ".join(str(i) for i in inputs) +
        ")\n" + "  input_signature: (\n" + "    " +
        ",\n    ".join(str(i) for i in input_signature) + ")"))
