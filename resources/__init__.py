from .resources import SampleResource
import falcon

def handle_generic_errors(ex, req, resp, params):
    print('error')
    raise ex

def create_app():
    app = falcon.API(None)
    app.add_route('/sample', SampleResource())
    app.add_error_handler(Exception, handle_generic_errors)

    return app