import json

import urllib3

DATA_PATH = "../data"
HEAD_PAGE_URL = "https://www.zhipin.com/"
ZP_COMMON_URL = "https://www.zhipin.com/wapi/"

ZP_COMMON_JSON_DICT = {
    "position": "zpCommon/data/position.json",
    "city": "zpCommon/data/city.json",
    "industry": "zpCommon/data/industry.json",
    "citysites": "zpgeek/common/data/citysites.json"
}

http = urllib3.PoolManager()


def get_zp_common_dict(data_url):
    position_rs = http.request("GET", data_url)
    position_rs_dict = {}
    if position_rs.status == 200:
        print(data_url, "access success")
        position_rs_str = position_rs.data.decode("UTF-8")
        position_rs_dict = json.loads(position_rs_str)
    else:
        print(data_url, "access failed")
    return position_rs_dict


def save_zp_common_data(response_data_dict, target_file_name):
    full_path = DATA_PATH + "/" + target_file_name
    with open(full_path, "w") as position_file_handler:
        json.dump(response_data_dict, position_file_handler, indent=4, ensure_ascii=False)


def save_head_page_data():
    for file_name, file_url in ZP_COMMON_JSON_DICT.items():
        full_url = ZP_COMMON_URL + file_url
        response_data_dict = get_zp_common_dict(full_url)
        if response_data_dict:
            save_zp_common_data(response_data_dict, file_name + ".json")


if __name__ == "__main__":
    save_head_page_data()