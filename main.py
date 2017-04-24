import sys
from webapi import WebApi

if __name__ == '__main__':
    src_target, src_base_url, src_api_key = sys.argv[1:4]
    src_project_key = sys.argv[4]
    dst_target, dst_base_url, dst_api_key = sys.argv[5:8]
    dst_path = sys.argv[8]

    src_obj = WebApi(src_target, src_base_url, src_api_key)
    dst_obj = WebApi(dst_target, dst_base_url, dst_api_key)
    data_list = src_obj.read_data_list({'projectIdOrKey': src_project_key})
    for data in data_list:
        dst_obj.write_data(
            '%s/%s' % (dst_path, data['name']),
            src_obj.read_data(data['id'])['content'])
