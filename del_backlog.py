import sys
from webapi import WebApi

if __name__ == '__main__':
    team = sys.argv[1]
    target = 'backlog'
    base_url = 'https://%s.backlog.jp/api/v2/wikis' % team
    api_key = sys.argv[2]
    project_key = sys.argv[3]

    obj = WebApi(target, base_url, api_key)
    data_list = obj.read_data_list({'projectIdOrKey': project_key})
    for data in data_list:
        obj.delete_data(data['id'])
