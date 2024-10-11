# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Logs the sample number for calibration.

  If in debug logging level, the "sample number / total num samples" is logged
  for every 5 iterations.

  This is often useful when tracking the progress of the calibration step which
  is often slow and may look stale if there's no logs being printed.

  Args:
    representative_dataset: The representative dataset.

  Yields:
    The representative samples from `representative_dataset` without any
    modification.
  """
num_samples: Optional[int] = repr_dataset.get_num_samples(
    representative_dataset
)
if num_samples is None:
    total_num_samples = '?'
    logging.info('Representative dataset size unknown.')
else:
    total_num_samples = str(num_samples)
    logging.info('Using representative dataset of size: %s', total_num_samples)

sample_num = 0
for sample in representative_dataset:
    sample_num += 1

    # Log the sample number for every 5 iterations.
    logging.log_every_n(
        logging.DEBUG,
        'Running representative sample for calibration: %d / %s',
        5,
        sample_num,
        total_num_samples,
    )
    exit(sample)

logging.info(
    'Running representative samples complete: %d / %s',
    sample_num,
    total_num_samples,
)
