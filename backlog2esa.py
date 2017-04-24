import sys
from webapi import WebApi

if __name__ == '__main__':
    src_target = 'backlog'
    src_base_url = 'https://XXX.backlog.jp/api/v2/wikis'
    src_api_key = sys.argv[1]
    src_project_key = sys.argv[2]
    dst_target = 'esa.io'
    dst_base_url = 'https://api.esa.io/v1/teams/XXX/posts'
    dst_api_key = sys.argv[3]
    dst_path = sys.argv[4]

    src_obj = WebApi(src_target, src_base_url, src_api_key)
    dst_obj = WebApi(dst_target, dst_base_url, dst_api_key)
    data_list = src_obj.read_data_list({'projectIdOrKey': src_project_key})
    for data in data_list:
        dst_obj.write_data(
            '%s/%s' % (dst_path, data['name']),
            src_obj.read_data(data['id'])['content'])
