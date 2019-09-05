from data import entries



def lookup_by_name(name):
    results = []
    for entry in entries:
        if name == entry['first_name']:
            results.append(name)
        elif name == entry['last_name']:
            results.append(name)
    return results

     