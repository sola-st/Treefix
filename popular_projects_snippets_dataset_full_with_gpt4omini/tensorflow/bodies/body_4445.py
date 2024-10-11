# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/accuracy_utils.py
"""Write a human-readable description of the statistics to stdout."""
if self._how_many_gt == 0:
    tf.compat.v1.logging.info('No ground truth yet, {}false positives'.format(
        self._how_many_fp))
else:
    any_match_percentage = self._how_many_gt_matched / self._how_many_gt * 100
    correct_match_percentage = self._how_many_c / self._how_many_gt * 100
    wrong_match_percentage = self._how_many_w / self._how_many_gt * 100
    false_positive_percentage = self._how_many_fp / self._how_many_gt * 100
    tf.compat.v1.logging.info(
        '{:.1f}% matched, {:.1f}% correct, {:.1f}% wrong, '
        '{:.1f}% false positive'.format(any_match_percentage,
                                        correct_match_percentage,
                                        wrong_match_percentage,
                                        false_positive_percentage))
