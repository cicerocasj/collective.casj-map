# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.casj-map.testing import COLLECTIVE_CASJ-MAP_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.casj-map is properly installed."""

    layer = COLLECTIVE_CASJ-MAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.casj-map is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.casj-map'))

    def test_browserlayer(self):
        """Test that ICollectiveCasj-MapLayer is registered."""
        from collective.casj-map.interfaces import (
            ICollectiveCasj-MapLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveCasj-MapLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_CASJ-MAP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.casj-map'])

    def test_product_uninstalled(self):
        """Test if collective.casj-map is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.casj-map'))
