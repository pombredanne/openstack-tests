# -*- mode:python; -*-
#
# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openstackci.tester import TestUnit


class TestSingleCorrectNetworkBridge(TestUnit):
    name = "Single network bridge"
    description = ("Verifies the single install is using lxcbr0 as its "
                   "network bridge")
    identifier = '00_single_network_bridge'
    install_type = 'Single'

    def run(self):
        if self.juju_env['network-bridge'] == 'lxcbr0':
            self.report.success("found lxcbr0 bridge")
        else:
            self.report.fail("incorrect bridge set: {}".format(
                self.juju_env['network-bridge']))

__test_class__ = TestSingleCorrectNetworkBridge
