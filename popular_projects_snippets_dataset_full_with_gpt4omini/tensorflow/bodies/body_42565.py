# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gen_gradient_input_output_exclusions.py
with open(output_file, "w") as fp:
    fp.write(gradient_input_output_exclusions.get_contents())
