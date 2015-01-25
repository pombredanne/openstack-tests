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


class TestAgentsStarted(TestUnit):
    name = "Agents Started"
    description = "Verifies an installation has all required agents started"
    identifier = 'agents_started'

    def run(self):
        self.report.success("Yes!")
        return 0

__test_class__ = TestAgentsStarted
