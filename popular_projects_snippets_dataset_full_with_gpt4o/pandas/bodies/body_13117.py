# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
class DummyClass(ExcelWriter):
    called_save = False
    called_write_cells = False
    called_sheets = False
    _supported_extensions = ("xlsx", "xls")
    _engine = "dummy"

    def book(self):
        pass

    def _save(self):
        type(self).called_save = True

    def _write_cells(self, *args, **kwargs):
        type(self).called_write_cells = True

    @property
    def sheets(self):
        type(self).called_sheets = True

    @classmethod
    def assert_called_and_reset(cls):
        assert cls.called_save
        assert cls.called_write_cells
        assert not cls.called_sheets
        cls.called_save = False
        cls.called_write_cells = False

register_writer(DummyClass)

with option_context("io.excel.xlsx.writer", "dummy"):
    path = "something.xlsx"
    with tm.ensure_clean(path) as filepath:
        with ExcelWriter(filepath) as writer:
            assert isinstance(writer, DummyClass)
        df = tm.makeCustomDataframe(1, 1)
        df.to_excel(filepath)
    DummyClass.assert_called_and_reset()

with tm.ensure_clean("something.xls") as filepath:
    df.to_excel(filepath, engine="dummy")
DummyClass.assert_called_and_reset()
