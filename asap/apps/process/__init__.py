"""
Process : Every Process is connected with a resource and itself it is blind.
          For every action it asks his Resource for instructions.
"""

RESOURCE_UPSTREAM_URL = 'http://localhost:8000/api/v1/resource/{resource_token}/{operation}/'
