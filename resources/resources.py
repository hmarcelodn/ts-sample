import falcon
import environs
import time
from random import uniform

env = environs.Env()

class SampleResource():

    def on_get(self, req, res):
        res.status = falcon.HTTP_200
