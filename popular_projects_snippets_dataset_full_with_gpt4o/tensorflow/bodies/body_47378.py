# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
cells = []
for cell in self.cells:
    cells.append(generic_utils.serialize_keras_object(cell))
config = {'cells': cells}
base_config = super(StackedRNNCells, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
