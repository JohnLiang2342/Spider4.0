


class UrlManager(object):
    
    def __init__(self):
        
        self.new_enter_urls = set()
        self.old_enter_urls = set()
        
        self.new_img_urls = set()
        self.old_img_urls = set()
        
    
    def has_new_enter_url(self):
        return len(self.new_enter_urls)!=0

    
    #添加单个url
    def add_new_enter_url(self,url):
        if url is None:
            return
        
        #既不在新urls也不在旧urls
        if url not in self.new_enter_urls and url not in self.old_enter_urls:
            self.new_enter_urls.add(url)
         
    #添加多个url
    def add_new_enter_urls(self,urls):
        if urls is None or len(urls)==0:
            return 
        for url in urls:
            self.add_new_enter_url(url)

        #return len(self.new_urls) 
    
    def get_new_enter_url(self):
        new_url = self.new_enter_urls.pop() #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        self.old_urls.add(new_url)
        return new_url

    
    def add_new_img_url(self, url):
        if url is None:
            return
        
        if url not in self.new_img_urls and url not in self.old_img_urls:
            self.new_img_urls.add(url)
        
    
    
    def add_new_img_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_img_url(url)         
        return len(self.new_img_urls)
    
    def has_new_img_url(self):
        return len(self.new_img_urls)!=0

    
    def get_new_img_url(self):
        img_url = self.new_img_urls.pop() #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        self.old_img_urls.add(img_url)
        return img_url
    
    
    
    
    
    
    
            
        
            
            
    
    
    



