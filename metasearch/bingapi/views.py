# Create your views here.
import requests

class Item(object):
    def __init__(self, item_dict):
        self.title = item_dict["Title"]
        self.url = item_dict["Url"]
        self.displayurl = item_dict["DisplayUrl"]
        self.snippet = item_dict.get("Description", "<i>No snippet available for this item.</i>")
        self.source = ['BING']
        self.base_score = [0, 0, 0]
        self.weighted_score = 0.0
        
def get_json_obj(query, page_num, result_per_page):
    base_url = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Web?Query=%s%s%s&$format=json&$top=%s&$skip=%s'
    key = 'D9qFt/S64oJyYDWeGIBxordSl1N28cubAeXQld7rSfE='
    top = result_per_page
    skip = (page_num - 1)*top
    url = base_url % ('%27', query, '%27', top, skip)
    
    return requests.get(url, auth=('', key)).json()
    
def get_item_list(query, page_num, result_per_page):
    item_list = []
    json_obj = get_json_obj(query, page_num, result_per_page)
    
    if not json_obj:
        return []
    
    for i in json_obj["d"]["results"]:
        item_list.append(Item(i))
        
    return item_list
