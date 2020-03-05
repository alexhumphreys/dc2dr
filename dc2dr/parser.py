import yaml
import sys
from tsort import tsort

def flatten(l):
    return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

def sort(services):
    dependencies = {}
    for name, v in services.items():
        if 'links' in v or 'depends_on' in v:
            dependencies[name] = set()
        if 'links' in v:
            for link in v['links']:
                dependencies[name].update({link})
        if 'depends_on' in v:
            for d in v['depends_on']:
                dependencies[name].update({d})
    if dependencies == {}:
        # TODO tidy up for this case
        return [services]
    order = flatten(tsort(dependencies, smallest_first=True))
    sorted_services = []
    for name in order:
        sorted_services.append({name: services[name]})
    return sorted_services


def run_commands(path):
    f = open(path)
    y = yaml.safe_load(f)
    return parse_compose_file(y)

def parse_compose_file(yaml_file):
    services = yaml_file['services']
    sorted_services = sort(services)

    parsed_services = []
    for d in sorted_services:
        for k, v in d.items():
            parsed_services.append(parse_service(k, v))

    commands = []
    for s in parsed_services:
        commands.append(write_run_command(s))
    return commands

def parse_service(name, service):
    docker_args = {'name': name}
    docker_args['image'] = parse_image(service['image'])
    for arg in ['depends_on', 'links', 'ports', 'expose', 'environment', 'command']:
        if arg in service:
            docker_args[arg] = globals()['parse_' + arg](service[arg])
    return docker_args

def write_run_command(service):
    command = ""
    prefix = "docker run -d --name={0} ".format(service['name'])
    command += prefix
    for arg in ['depends_on', 'links', 'ports', 'expose', 'environment']:
        if arg in service:
            command += service[arg]
    command += service['image']
    if 'command' in service:
	    command += ' {0}'.format(service['command'])
    return command

def parse_image(image):
    return image

def parse_depends_on(deps):
    return to_docker_arg(deps, " --link={0} ")

def parse_links(links):
    return parse_depends_on(links)

def parse_ports(ports):
    return to_docker_arg(ports, " -p {0} ")

def parse_expose(exports):
    return to_docker_arg(exports, " --expose={0} ")

def parse_environment(envs):
    string = ""
    for k, v in envs.items():
        string += ' -e {0}="{1}" '.format(k, v)
    return string

def parse_command(command):
    if type(command) is list:
        return ' '.join(command)
    else:
        return command

def to_docker_arg(args, str_format):
    string = ""
    for a in args:
        string += str_format.format(a)
    return string
