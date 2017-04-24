import requests


class WebApi():
    def __init__(self, target, base_url, api_key):
        if target not in [
            'backlog',
            'esa.io',
        ]:
            raise Exception('NOT SUPPORTED: %s' % target)
        self.target = target
        self.base_url = base_url
        self.api_key = api_key

    def _add_api_key(self, params):
        if self.target == 'backlog':
            params['apiKey'] = self.api_key
        elif self.target == 'esa.io':
            params['access_token'] = self.api_key
        return params

    def read_data_list(self, params={}):
        params = self._add_api_key(params)
        r = requests.get(self.base_url, params=params)
        return r.json()

    def read_data(self, data_id, params={}):
        params = self._add_api_key(params)
        r = requests.get('%s/%s' % (self.base_url, data_id), params=params)
        return r.json()

    def write_data(self, jsonobj, params={}):
        params = self._add_api_key(params)
        r = requests.post(self.base_url, json=jsonobj, params=params)
        return r.status_code


if __name__ == '__main__':
    pass
