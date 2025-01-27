# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/logging/gen_html_test.py
toco_conversion_log_before = _toco_conversion_log_pb2.TocoConversionLog()
toco_conversion_log_after = _toco_conversion_log_pb2.TocoConversionLog()

toco_conversion_log_before.op_list.extend([
    "Conv1", "Conv2", "Identity", "Reshape", "Dense", "Dense", "CustomOp",
    "AvgPool3D", "Softmax"
])
toco_conversion_log_before.model_size = 9

toco_conversion_log_after.op_list.extend([
    "Conv1", "Conv2", "Dense", "Dense", "CustomOp", "AvgPool3D", "Softmax"
])
toco_conversion_log_after.built_in_ops["Conv1"] = 1
toco_conversion_log_after.built_in_ops["Conv2"] = 1
toco_conversion_log_after.built_in_ops["Dense"] = 2
toco_conversion_log_after.built_in_ops["Softmax"] = 1
toco_conversion_log_after.custom_ops["CustomOp"] = 1
toco_conversion_log_after.select_ops["AvgPool3D"] = 1
toco_conversion_log_after.model_size = 7

export_path = os.path.join(self.get_temp_dir(), "generated.html")
html_generator = gen_html.HTMLGenerator(
    html_template_path=resource_loader.get_path_to_datafile(
        "template.html"),
    export_report_path=export_path)

html_generator.generate(toco_conversion_log_before,
                        toco_conversion_log_after, True,
                        "digraph  {a -> b}", "digraph  {a -> b}", "",
                        "/path/to/flatbuffer")

with _file_io.FileIO(export_path, "r") as f_export, _file_io.FileIO(
    resource_loader.get_path_to_datafile("testdata/generated.html"),
    "r") as f_expect:
    expected = f_expect.read()
    exported = f_export.read()
    self.assertEqual(exported, expected)
