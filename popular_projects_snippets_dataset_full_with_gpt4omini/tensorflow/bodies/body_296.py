# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.image.extract_glimpse(x, size, off, False, "
        "False, False, name=\"foo\")\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.image.extract_glimpse(x, size, off, False, "
    "False, 'uniform' if (False) else 'gaussian', name=\"foo\")\n",
)

text = ("tf.image.extract_glimpse(x, size, off, centered=False, "
        "normalized=False, uniform_noise=True if uniform_noise else "
        "False, name=\"foo\")\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.image.extract_glimpse(x, size, off, centered=False, "
    "normalized=False, noise='uniform' if (True if uniform_noise else "
    "False) else 'gaussian', name=\"foo\")\n",
)

text = ("tf.image.extract_glimpse(x,\n"
        "                         size,\n"
        "                         off,\n"
        "                         centered=True,\n"
        "                         normalized=True, # Stuff before\n"
        "                         uniform_noise=False,\n"
        "                         name=\"foo\")# Stuff after\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text, "tf.image.extract_glimpse(x,\n"
    "                         size,\n"
    "                         off,\n"
    "                         centered=True,\n"
    "                         normalized=True, # Stuff before\n"
    "                         noise='uniform' if (False) else 'gaussian',\n"
    "                         name=\"foo\")# Stuff after\n")

text = "tf.image.extract_glimpse(x)\n"
_, unused_report, errors, new_text = self._upgrade(text)
self.assertEqual(new_text, text)
self.assertEqual(errors, [])
