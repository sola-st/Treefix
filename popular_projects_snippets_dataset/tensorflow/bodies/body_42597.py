# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions_test.py
expected_contents = gradient_input_output_exclusions.get_contents()
filename = os.path.join(
    resource_loader.get_root_dir_with_all_resources(),
    resource_loader.get_path_to_datafile("pywrap_gradient_exclusions.cc"))
actual_contents = file_io.read_file_to_string(filename)

# On windows, one or both of these strings may have CRLF line endings.
# To make sure, sanitize both:
sanitized_actual_contents = actual_contents.replace("\r", "")
sanitized_expected_contents = expected_contents.replace("\r", "")

self.assertEqual(
    sanitized_actual_contents, sanitized_expected_contents, """
pywrap_gradient_exclusions.cc needs to be updated.
Please regenerate using:
bazel run tensorflow/python/eager:gen_gradient_input_output_exclusions -- $PWD/tensorflow/python/eager/pywrap_gradient_exclusions.cc"""
)
