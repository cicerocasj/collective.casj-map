# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.casj-map


class CollectiveCasj-MapLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.casj-map)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.casj-map:default')


COLLECTIVE_CASJ-MAP_FIXTURE = CollectiveCasj-MapLayer()


COLLECTIVE_CASJ-MAP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CASJ-MAP_FIXTURE,),
    name='CollectiveCasj-MapLayer:IntegrationTesting'
)


COLLECTIVE_CASJ-MAP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CASJ-MAP_FIXTURE,),
    name='CollectiveCasj-MapLayer:FunctionalTesting'
)


COLLECTIVE_CASJ-MAP_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CASJ-MAP_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveCasj-MapLayer:AcceptanceTesting'
)
