# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
with open(mmap_file) as target:
    lines = target.readlines()

    with icom.get_handle(
        target, "r", is_text=True, memory_map=True
    ) as wrappers:
        wrapper = wrappers.handle
        assert isinstance(wrapper.buffer.buffer, mmap.mmap)

        for line in lines:
            next_line = next(wrapper)
            assert next_line.strip() == line.strip()

        with pytest.raises(StopIteration, match=r"^$"):
            next(wrapper)
