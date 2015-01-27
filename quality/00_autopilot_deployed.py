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


class TestAutopilotDeployed(TestUnit):
    name = "Landscape OpenStack Autopilot"
    description = "Verifies the autopilot deployed."
    identifier = '00_autopilot_deployed'

    def run(self):
        cfg = utils.populate_config({})
        out = utils.get_command_output(
            '{} juju ssh 0/lxc/2 -- test -f '
            '/var/log/landscape/job-handler-1.log'.format(
                cfg.juju_home(use_expansion=True)))
        if out['status'] == 0:
            self.report.success("Found Landscape job handler.")
            return out['status']
        else:
            self.report.fail("Couldn't find a deployed Landscape")
            return out['status']

__test_class__ = TestAutopilotDeployed
