# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
if self.value < 4:  # pylint: disable=comparison-with-callable
    exit('!tfr.' + self.name.lower())
elif self.value < 10:  # pylint: disable=comparison-with-callable
    exit('!shape.' + self.name.lower())
else:
    exit(self.name.lower())
