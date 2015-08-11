'''
Code from https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming/
'''

bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def assoc(_d, key, value):
    '''
    Sets _d[key] = value. Don't really understand why this is necessary.
    '''
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def call(fn, key):
    '''
    Returns a function that, when applied to a dictionary _d, will return a
    dictionary d where d[key] = fn(_d[key]).
    '''
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
    return apply_fn


def pluck(keys):
    '''
    Returns a function that, when applied to a dictionary _d, will return a
    dictionary d containing only keys.
    '''
    def pluck_fn(record):
        return reduce(lambda a, x: assoc(a, x, record[x]),
                      keys,
                      {})
    return pluck_fn


def pipeline_each(vals, fns):
    '''
    Generic pipeline that applies each fn in fns to each val in vals, returning
    a transformed list of vals.
    '''
    return reduce(lambda a, x: map(x, a),  # go through list of fns, applying
                                           # each in turn to output of last
                  fns,   # list of functions to apply
                  vals)  # starting list of values


set_canada_as_country = call(lambda x: 'Canada', 'country')
strip_punctuation_from_name = call(lambda x: x.replace('.', ''), 'name')
capitalize_names = call(str.title, 'name')
pluck_name_country = pluck(['name', 'country'])

print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names,
                            pluck_name_country])
