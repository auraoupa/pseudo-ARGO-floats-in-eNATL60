#!/usr/bin/env python

"""Tests for `pseudo_argo_floats_in_enatl60` package."""

import pytest


from pseudo_argo_floats_in_enatl60 import pseudo_argo_floats_in_enatl60


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
