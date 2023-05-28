import requests
import json

def get_qq_nickname(qqid):
    url = f"http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins={qqid}"
    response = requests.get(url)
    
    # 解析返回的JSON数据
    json_str = response.text[response.text.index("(") + 1:response.text.rindex(")")]
    user_info = json.loads(json_str)[qqid]
    
    # 取出数组中的第七个元素，即索引为6的元素，它的值就是用户的名称
    user_name = user_info[6]
    
    # 将结果以字典格式返回
    return {'qqid': qqid, 'user_name': user_name}