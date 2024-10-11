# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
"""Logs a TPUEmbeddingConfiguration proto across multiple statements.

  Args:
    config: TPUEmbeddingConfiguration proto to log.  Necessary because
      logging.info has a maximum length to each log statement, which
      particularly large configs can exceed.
  """
logging.info("Beginning log of TPUEmbeddingConfiguration.")
for line in str(config).splitlines():
    logging.info(line)
logging.info("Done with log of TPUEmbeddingConfiguration.")
