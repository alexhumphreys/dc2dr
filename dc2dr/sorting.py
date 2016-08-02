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
    order = flatten(tsort(dependencies, smallest_first=True))
    sorted_services = []
    for name in order:
        sorted_services.append({name: services[name]})
    return sorted_services
