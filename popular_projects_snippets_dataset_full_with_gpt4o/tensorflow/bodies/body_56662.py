# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
image_path = os.path.join(PREFIX_PATH, "jpeg", "testdata", "small.jpg")
image_data = convert_image_to_csv.get_image(27, 33, True, image_path)
self.assertLessEqual(0, np.min(image_data))
self.assertGreaterEqual(255, np.max(image_data))
