from flask_restful import Resource


class Status(Resource):

    def get(self):
        status = {
            'name': 'graph-image-generator',
            'version': 'v1',
            'build': '9-20-2016',
            'description': 'Network image generator service.  '
                           'This service generates network images on the fly from any CX JSON.',
            'documents': 'https://github.com/cytoscape-ci/image-generator'
        }
        return status
