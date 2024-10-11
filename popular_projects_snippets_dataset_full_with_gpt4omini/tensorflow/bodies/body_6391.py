# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
if ((self._communication_options.implementation ==
     collective_util.CommunicationImplementation.NCCL) and
    self._local_device_type != "GPU"):
    logging.warning("Enabled NCCL communication but no GPUs detected/"
                    "specified.")
