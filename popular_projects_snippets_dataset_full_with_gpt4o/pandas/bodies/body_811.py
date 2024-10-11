# Extracted from ./data/repos/pandas/pandas/tests/internals/test_api.py
# SUBJECT TO CHANGE

modules = [
    "blocks",
    "concat",
    "managers",
    "construction",
    "array_manager",
    "base",
    "api",
    "ops",
]
expected = [
    "Block",
    "NumericBlock",
    "DatetimeTZBlock",
    "ExtensionBlock",
    "ObjectBlock",
    "make_block",
    "DataManager",
    "ArrayManager",
    "BlockManager",
    "SingleDataManager",
    "SingleBlockManager",
    "SingleArrayManager",
    "concatenate_managers",
    "create_block_manager_from_blocks",
]

result = [x for x in dir(internals) if not x.startswith("__")]
assert set(result) == set(expected + modules)
