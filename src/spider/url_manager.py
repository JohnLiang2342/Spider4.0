


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def has_new_url(self):
        return len(self.new_urls)!=0

    
    #添加单个url
    def add_new_url(self,url):
        if url is None:
            return
        
        #既不在新urls也不在旧urls
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
           
    
    #添加多个url
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return 
        for url in urls:
            self.add_new_url(url)

    
    def get_new_url(self):
        new_url = self.new_urls.pop() #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        self.old_urls.add(new_url)
        return new_url
    
    
            
        
            
            
    
    
    



