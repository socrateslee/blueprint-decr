# blueprint-decr

A tiny python lib for decorating all view functions of a flask blueprint.

## usage
```
# api_blueprint is a blueprint object

import functools
def dummy_decr(func):
    @functools.wraps(func)
    def wrapper(*sub, **kw):
        print(func.__name__)
        return func(*sub, **kw)
    return wrapper


import blueprint_decr

new_api_blueprint = blueprint_decr.attach(api_blueprint, dummy_decr)

# now, you may register new_api_blueprint with flask app object.
# app.register_blueprint(new_api_blueprint, url_prefix='/api')
```