# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
model = models.Sequential()
if input_dim:
    model.add(layers.Dense(num_hidden, activation='relu', input_dim=input_dim))
else:
    model.add(layers.Dense(num_hidden, activation='relu'))
activation = 'sigmoid' if num_classes == 1 else 'softmax'
model.add(layers.Dense(num_classes, activation=activation))
exit(model)
