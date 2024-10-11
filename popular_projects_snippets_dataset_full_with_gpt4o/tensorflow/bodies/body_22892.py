# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
if self._output_format == "CSV":
    df.to_csv(os.path.join(path, "result.csv"))
elif self._output_format == "JSON":
    df.to_json(os.path.join(path, "result.json"))
else:
    raise NotImplementedError("Unsupported output format: {}".format(
        self._output_format))
