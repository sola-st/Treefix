# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html_test.py
# Copies all required data files into a temporary folder for testing.
export_path = self.get_temp_dir()
toco_log_before_path = resource_loader.get_path_to_datafile(
    "testdata/toco_log_before.pb")
toco_log_after_path = resource_loader.get_path_to_datafile(
    "testdata/toco_log_after.pb")
dot_before = resource_loader.get_path_to_datafile(
    "testdata/toco_tf_graph.dot")
dot_after = resource_loader.get_path_to_datafile(
    "testdata/toco_tflite_graph.dot")
shutil.copy(toco_log_before_path, export_path)
shutil.copy(toco_log_after_path, export_path)
shutil.copy(dot_before, export_path)
shutil.copy(dot_after, export_path)

# Generate HTML content based on files in the test folder.
gen_html.gen_conversion_log_html(export_path, True, "/path/to/flatbuffer")

result_html = os.path.join(export_path, "toco_conversion_summary.html")

with _file_io.FileIO(result_html, "r") as f_export, _file_io.FileIO(
    resource_loader.get_path_to_datafile("testdata/generated.html"),
    "r") as f_expect:
    expected = f_expect.read()
    exported = f_export.read()
    self.assertEqual(exported, expected)
