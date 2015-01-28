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


class TestSingleDeployed(TestUnit):
    name = "Single Deploy"
    description = "Verifies the single install path deployed."
    identifier = '00_single_deployed'
    install_type = 'Single'

    def run(self):
        cmd = ("JUJU_HOME=~/.cloud-install/juju juju status")
        out = utils.container_run('uoi-bootstrap', cmd)
        if 'environments: local' in out:
            self.report.success("Single install deployed.")
        else:
            self.report.fail("Failed to query juju environment")

__test_class__ = TestSingleDeployed
