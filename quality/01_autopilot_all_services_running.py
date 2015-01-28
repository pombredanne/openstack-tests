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


class TestAutopilotServicesRunning(TestUnit):
    name = "Autopilot - all services running"
    description = "Verifies all services are started in deployment."
    identifier = '01_autopilot_all_services_running'
    install_type = 'Landscape OpenStack Autopilot'

    def run(self):
        services = self.juju_state.services
        for svc in services:
            unit = svc.units[0]
            if 'started' not in unit.agent_state:
                self.report.fail(
                    '{} service not started'.format(unit.unit_name))
        if len(self.report.failed_tests) == 0:
            self.report.success('All services started')

__test_class__ = TestAutopilotServicesRunning
