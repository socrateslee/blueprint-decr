'''
Add an decorator to all the view functions of a flask blueprint.
'''
import copy
import six


def attach(blueprint, decorator=None):
    '''
    attach(blueprint, decorator=None)
    Add decorator for every view functions of blueprint.
    '''
    new_blueprint = copy.deepcopy(blueprint)
    new_blueprint.deferred_functions = []
    for func in blueprint.deferred_functions:
        freevar_dict = dict(zip(six.get_function_code(func).co_freevars,                                                                           
                       map(lambda f: f.cell_contents, six.get_function_closure(func))))
        rule = freevar_dict['rule']
        endpoint = freevar_dict['endpoint']
        view_func = freevar_dict['view_func']
        options = freevar_dict['options']
        decorated_view_func = decorator(view_func) if callable(view_func) and callable(decorator)\
                              else view_func
        new_blueprint.add_url_rule(rule, endpoint, decorated_view_func, **options)
    return new_blueprint
