# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn

from reframe.core.runtime import runtime


@rfm.simple_test
class DefaultPrgEnvCheck(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Ensure PrgEnv-cray is loaded by default'
        self.valid_prog_environs = ['Default']
        self.valid_systems = ['archer2:login']
        self.executable = 'module'
        self.executable_opts = ['-t', 'list']
        self.maintainers = ['Andy Turner']
        self.tags = {'production', 'craype'}
        self.sanity_patterns = sn.assert_found(r'^PrgEnv-cray', self.stderr)


@rfm.simple_test
class EnvironmentCheck(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = 'Ensure programming environment is loaded correctly'
        self.valid_systems = ['archer2:login']
        self.valid_prog_environs = ['PrgEnv-cray', 'PrgEnv-gnu', 'PrgEnv-aocc']

        self.executable = 'module'
        self.executable_opts = ['-t', 'list']
        self.sanity_patterns = sn.assert_found(self.env_module_patt,
                                               self.stderr)
        self.maintainers = ['Andy Turner']
        self.tags = {'production', 'craype'}

    @property
    @deferrable
    def env_module_patt(self):
        return r'^%s' % self.current_environ.name
