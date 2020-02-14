import os
from io import StringIO
import pytest
from neoconverter.utils import _read


def test_read_good():
    fp = os.path.join(
        "neoconverter",
        "tests",
        "inputs",
        "MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV",
    )
    df = _read(fp)
    assert len(df.columns) == 3600
    assert len(df.index) == 1800


def test_read_bad():
    s = StringIO("999.0,999.0,999.0\n" "123.4,5.2,3.1")
    with pytest.raises(ValueError) as einfo:
        _read(s)
    eiv = str(einfo.value)
    assert "isn't formatted as expected" in eiv
    assert "lat/lon" in eiv
