import json

import urllib3

from boss_config import BossConfig

config = BossConfig()
DATA_PATH = config.get_property("data_folder_path")

HEAD_PAGE_URL = "https://www.zhipin.com/"
ZP_COMMON_URL = "https://www.zhipin.com/wapi/"

ZP_COMMON_JSON_DICT = {
    "position": "zpCommon/data/position.json",
    "city": "zpCommon/data/city.json",
    "industry": "zpCommon/data/industry.json",
    "citysites": "zpgeek/common/data/citysites.json"
}

http = urllib3.PoolManager()
self_ip_url = "http://httpbin.org/ip"

def get_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36",
        # "Accept": "text/html,appliction/xhtml+xml,appliction/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    return headers


def get_zp_common_dict(data_url):
    headers = get_headers()
    position_rs = http.request("GET", data_url, headers=headers)
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
