# -*- coding: utf-8 -*-

import click
import yaml
import sys
import dc2dr

def parse_yml(path):
    f = open(path)
    y = yaml.safe_load(f)

    run_commands = dc2dr.parse_compose_file(y)
    for c in run_commands:
	print(c)

@click.command()
@click.argument('f', type=click.Path(exists=True))
def main(f):
    parse_yml(f)

if __name__ == "__main__":
    main()
