# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
csv_string = convert_image_to_csv.array_to_int_csv(
    np.array([[1, 2], [3, 4]]))
self.assertEqual("1,2,3,4", csv_string)
