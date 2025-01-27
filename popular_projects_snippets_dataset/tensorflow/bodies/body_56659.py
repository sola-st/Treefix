# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
image_path = os.path.join(PREFIX_PATH, "png", "testdata", "lena_rgba.png")
image_data = convert_image_to_csv.get_image(10, 10, False, image_path)
self.assertEqual((10, 10, 3), image_data.shape)
