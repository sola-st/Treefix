# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py
"""Generate examples for test sets.

  Args:
    options: Options containing information to generate examples.
    test_sets: List of the name of test sets to generate examples.
  """
_prepare_dir(options)

multi_gen_state = MultiGenState()
options.multi_gen_state = multi_gen_state

zip_path = os.path.join(options.output_path, options.zip_to_output)
with zipfile.PyZipFile(zip_path, "w") as archive:
    multi_gen_state.archive = archive

    for test_name in test_sets:
        # Some generation function can change the value of the options object.
        # To keep the original options for each run, we use shallow copy.
        new_options = copy.copy(options)

        # Remove suffix and set test_name to run proper test generation function.
        multi_gen_state.test_name = re.sub(
            r"(_(|with-flex|forward-compat|mlir-quant))?$",
            "",
            test_name,
            count=1)
        # Set label base path to write test data files with proper path.
        multi_gen_state.label_base_path = os.path.join(
            os.path.dirname(zip_path), test_name + ".zip")

        generate_examples(new_options)

    zipinfo = zipfile.ZipInfo("manifest.txt")
    archive.writestr(zipinfo, "".join(multi_gen_state.zip_manifest),
                     zipfile.ZIP_DEFLATED)
