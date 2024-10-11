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
import tempfile # pragma: no cover
from lxml.etree import XSLTApplyError # pragma: no cover
import os # pragma: no cover

class TempManager:# pragma: no cover
    def ensure_clean(self, name):# pragma: no cover
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xml')# pragma: no cover
        tmp_file.close()# pragma: no cover
        return tmp_file # pragma: no cover
tm = TempManager() # pragma: no cover
geom_df = pd.DataFrame({'geometry': ['POINT (1 1)', 'POINT (2 2)']}) # pragma: no cover
def mock_to_xml(path, stylesheet):# pragma: no cover
        raise XSLTApplyError('Cannot resolve URI') # pragma: no cover
geom_df.to_xml = mock_to_xml # pragma: no cover

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
