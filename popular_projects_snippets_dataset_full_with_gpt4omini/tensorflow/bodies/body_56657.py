# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
image_path = os.path.join(PREFIX_PATH, "jpeg", "testdata", "small.jpg")
image_data = convert_image_to_csv.get_image(64, 96, False, image_path)
self.assertEqual((96, 64, 3), image_data.shape)
