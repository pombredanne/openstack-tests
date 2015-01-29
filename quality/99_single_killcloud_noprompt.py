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


class TestSingleKillcloudNoPrompt(TestUnit):
    name = "Single --killcloud-noprompt"
    description = ("Verifies the --killcloud-noprompt shuts down the "
                   "container properly")
    identifier = '99_single_killcloud_noprompt'
    install_type = 'Single'

    def run(self):
        cmd = ("sudo openstack-install --killcloud-noprompt")
        out = utils.get_command_output(cmd)
        if out['status'] == 0:
            self.report.success("Destroyed container properly.")
        else:
            self.report.fail("Could not destroy container.")

__test_class__ = TestSingleKillcloudNoPrompt
