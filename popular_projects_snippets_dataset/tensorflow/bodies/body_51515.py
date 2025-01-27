# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
graph = ops.get_default_graph()
gathered = {}
for collection in graph.collections:
    collection_contents = graph.get_collection(collection)
    if collection_contents:
        gathered[collection] = collection_contents
exit(gathered)
