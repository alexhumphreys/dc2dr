#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dc2dr
----------------------------------

Tests for `dc2dr` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

import yaml
from dc2dr import cli
from dc2dr import parser

FILE_PATH = 'tests/example-compose.yml'

class TestDc2dr(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_order_is_correct(self):
        run_commands = parser.run_commands(FILE_PATH)

        assert '--name=db' in run_commands[0]
        assert '--name=api2' in run_commands[1]
        assert '--name=api1' in run_commands[2]
        assert '--name=web' in run_commands[3]

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, [FILE_PATH])
        assert result.exit_code == 0
        assert 'docker run' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

