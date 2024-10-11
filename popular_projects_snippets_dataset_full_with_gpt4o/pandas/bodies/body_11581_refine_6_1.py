import pytest # pragma: no cover
import pandas as pd # pragma: no cover
import tempfile as tm # pragma: no cover
from unittest.mock import Mock # pragma: no cover

pytest = Mock(raises=pytest.raises) # pragma: no cover
tm = Mock(ensure_clean=tm.NamedTemporaryFile) # pragma: no cover
geom_df = pd.DataFrame({'geometry': ['POINT (1 1)', 'POINT (2 2)']}) # pragma: no cover
geom_df.to_xml = Mock() # pragma: no cover

import pytest # pragma: no cover
import pandas as pd # pragma: no cover
import tempfile as tm # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover

class TemporaryDirectoryWrapper:# pragma: no cover
    def __enter__(self):# pragma: no cover
        self.temporary_file = tm.NamedTemporaryFile(delete=False, suffix='.xml')# pragma: no cover
        return self.temporary_file.name# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        try:# pragma: no cover
            self.temporary_file.close()# pragma: no cover
        except Exception:# pragma: no cover
            pass# pragma: no cover
    def write(self, content):# pragma: no cover
        with open(self.temporary_file.name, 'w') as f:# pragma: no cover
            f.write(content)# pragma: no cover
        return self.temporary_file.name # pragma: no cover
tm.ensure_clean = TemporaryDirectoryWrapper # pragma: no cover
geom_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_to_xml.py
from l3.Runtime import _l_
try:
    from lxml.etree import XSLTApplyError
    _l_(21714)

except ImportError:
    pass

xsl = """\
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" encoding="utf-8" indent="yes" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:copy-of select="document('non_existent.xml')/*"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>"""
_l_(21715)

with pytest.raises(XSLTApplyError, match=("Cannot resolve URI")):
    _l_(21718)

    with tm.ensure_clean("test.xml") as path:
        _l_(21717)

        geom_df.to_xml(path, stylesheet=xsl)
        _l_(21716)
