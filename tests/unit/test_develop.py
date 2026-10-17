import pytest

def _make_develop(dirname):
    from pkginfo.develop import Develop
    return Develop(dirname)

def test_develop_ctor_w_path():
    from tests.unit import _helpers
    develop = _make_develop('.')
    _helpers._checkDevelop(None, develop)

def test_develop_ctor_w_invalid_path():
    import warnings 
    from pkginfo.distribution import UnknownMetadataVersion

    with warnings.catch_warnings(record=True) as warned:
        develop = _make_develop('/nonesuch')

    assert(develop.metadata_version == None)
    assert(develop.name == None)
    assert(develop.version == None)

    assert len(warned) == 2
    assert str(warned[0].message).startswith('No PKG-INFO found')
    assert warned[1].category is UnknownMetadataVersion
