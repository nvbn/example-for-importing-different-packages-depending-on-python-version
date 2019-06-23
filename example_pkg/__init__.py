import sys
import os

VERSIONS = {'2_7': (2, 7),
            '3_5': (3, 5)}
root = os.path.abspath(os.path.dirname(__file__))


def _get_available_versions():
    for version in os.listdir(root):
        if version in VERSIONS:
            yield version


def _get_version():
    available_versions = sorted(_get_available_versions())[::-1]
    for version in available_versions:
        if VERSIONS[version] <= sys.version_info:
            return version


# We should pass `__name__` as an argument, because
# we can't access `__name__` after module deletion
def _import_module(name):
    version = _get_version()
    version_path = os.path.join(root, version)
    sys.path.insert(0, version_path)
    del sys.modules[name]
    __import__(name)


_import_module(__name__)