# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
exit('http://' + os.environ.get(_GCE_METADATA_URL_ENV_VARIABLE,
                                  'metadata.google.internal'))
