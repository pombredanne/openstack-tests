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
from openstackci.validator import Validator


class TestMultiDeployed(TestUnit):
    name = "Multi install deploy"
    description = "Verifies the multi install deployed."
    identifier = '00_multi_deployed'
    install_type = 'Multi'

    def run(self):
        validate = Validator(self.config, self.juju_state)
        ret, services = validate.is_services_started()
        if ret:
            self.report.success('Test services started {}'.format(services))
        else:
            self.report.fail('Test services failed {}'.format(services))

__test_class__ = TestMultiDeployed
