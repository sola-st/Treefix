# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/convert_image_to_csv_test.py
image_path = os.path.join(PREFIX_PATH, "jpeg", "testdata", "no_such.jpg")
with self.assertRaises(NotFoundError):
    _ = convert_image_to_csv.get_image(64, 96, False, image_path)
