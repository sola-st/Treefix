# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Creates a valid `name_scope` name."""
if self.name is None:
    self._name_scope = self.__class__.__name__
elif self.name == '<lambda>':
    self._name_scope = 'lambda'
else:
    # E.g. '_my_loss' => 'my_loss'
    self._name_scope = self.name.strip('_')
