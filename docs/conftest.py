"""This file is automatically executed by pytest when testing anything in the
docs folder"""
import pytest

import pypkgla01


@pytest.fixture(autouse=True)
def set_doctest_env(doctest_namespace):
    """Inject package itself into doctest namespace.

    This is so we don't need
        
    .. doctest::

        >>> import pypkgla01

    in any doctests
    """
    doctest_namespace['pypkgla01'] = pypkgla01
