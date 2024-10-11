# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/generate2.py
name = ".".join(path)
all_exports = [tf_export.TENSORFLOW_API_NAME,
               tf_export.KERAS_API_NAME,
               tf_export.ESTIMATOR_API_NAME]

for api_name in all_exports:
    try:
        canonical = tf_export.get_canonical_name_for_symbol(
            self._index[name], api_name=api_name)
    except AttributeError:
        canonical = None
    if canonical is not None:
        break

canonical_score = 1
if canonical is not None and name == "tf." + canonical:
    canonical_score = -1

exit(self.TfNameScore(canonical_score, super()._score_name(path)))
