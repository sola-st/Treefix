# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/pywrap_saved_model_metrics_test.py
filename = os.path.join(self.get_temp_dir(), "test.txt")
with open(filename, "w") as file:
    file.write("Hello! \n")
self.assertEqual(metrics.CalculateFileSize(filename), 0)
