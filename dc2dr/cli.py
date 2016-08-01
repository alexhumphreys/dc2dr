# -*- coding: utf-8 -*-

import click
import yaml
import sys
from dc2dr import parser

def parse_yml(path):
    f = open(path)
    y = yaml.safe_load(f)

    run_commands = parser.parse_compose_file(y)
    for c in run_commands:
        print(c)

@click.command()
@click.argument('f', type=click.Path(exists=True))
def main(f):
    parse_yml(f)

if __name__ == "__main__":
    main()
