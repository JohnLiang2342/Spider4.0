
import requests

class HtmlDownloader(object):
    
    
    def downloade(self,header,url):
        if url is None:
            return None
        
        page_html = requests.get(url,headers = header)
        
        if page_html.status_code != 200:
            return None
        page_html.encoding = 'gb2312'
        
        return page_html.text
    
    

