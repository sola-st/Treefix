# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
logging.warning("The training loop will run indefinitely since you have "
                "set `steps_per_epoch=-1`. Please use batch-level "
                "callbacks to save checkpoints or log training progress, "
                "etc")
