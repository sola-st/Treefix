# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
image_path = os.path.join(PREFIX_PATH, "jpeg", "testdata", "medium.jpg")
image_data = convert_image_to_csv.get_image(40, 20, True, image_path)
self.assertEqual((20, 40, 1), image_data.shape)
