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
import cloudinstall.utils as utils


class TestSingleCloudController(TestUnit):
    name = "Nova Cloud Controller tests"
    description = ("Verifies nova cloud controller is "
                   "configured properly on Single")
    identifier = '01_single_cloud_controller'
    install_type = 'Single'

    def run(self):
        # Make sure openstack credentials files exists
        for u in ['admin', 'ubuntu']:
            cmd = ("JUJU_HOME=~/.cloud-install/juju juju ssh "
                   "nova-cloud-controller/0 -- "
                   "test -f /tmp/openstack-{}-rc".format(u))
            out = utils.container_run('uoi-bootstrap', cmd)
            if out['status'] != 0:
                self.report.fail("Failed to query juju environment")
            else:
                self.report.success("Found openstack-{}-rc".format(u))

__test_class__ = TestSingleCloudController
