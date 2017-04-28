import sys
import codecs
from webapi import WebApi

if __name__ == '__main__':
    bk_dir = 'bk'
    team = sys.argv[1]
    target = 'backlog'
    base_url = 'https://%s.backlog.jp/api/v2/wikis' % team
    api_key = sys.argv[2]
    project_key = sys.argv[3]

    obj = WebApi(target, base_url, api_key)
    data_list = obj.read_data_list({'projectIdOrKey': project_key})
    for data in data_list:
        f = codecs.open('%s/%s' % (bk_dir, data['id']), 'a', 'utf-8')
        f.write(data['name'])
        f.write('#######')
        f.write(obj.read_data(data['id'])['content'])
        f.close()
