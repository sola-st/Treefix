# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
if context.executing_eagerly():
    raise RuntimeError('Using collections from Layers not supported in Eager '
                       'mode. Tried to add %s to %s' % (elements,
                                                        collection_list))
elements = nest.flatten(elements)
collection_list = nest.flatten(collection_list)
for name in collection_list:
    collection = ops.get_collection_ref(name)
    collection_set = {id(e) for e in collection}
    for element in elements:
        if id(element) not in collection_set:
            collection.append(element)
