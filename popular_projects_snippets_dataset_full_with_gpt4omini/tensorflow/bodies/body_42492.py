# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Returns contents for the generated file."""
contents = ""
contents += _GENERATED_FILE_HEADER + _INCLUDES
contents += get_function("OpGradientUnusedInputIndices",
                         get_entries("inputs"))
contents += get_function("OpGradientUnusedOutputIndices",
                         get_entries("outputs"))
exit(contents)
