


from spider import url_manager, html_parser, html_downloader, img_outputer


class SpiderMain(object):
    
    def __init__(self):
        #初始化各个对象
        self.url = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = img_outputer.ImgOutputer()
        

    
    
    
    def craw(self,header):
        page_number = 1
        
        #循环的首页页数
        try:
            while page_number<=2:
                root_url = "http://www.meizitu.com/a/more_%d.html" %(page_number)
                page_html = self.downloader.downloade(header,root_url)
                enter_url = self.parser.parse_enter_url(page_html)
                #print(page_html)
                #print(root_url)
                #print(len(enter_page_url))
                self.url.add_new_enter_urls(enter_url)
                page_number = page_number + 1
        except:
            print("爬取入口页面失败")
                
        
        try:   
            while self.url.has_new_enter_url():
                new_url = self.url.get_new_enter_url()
                page_html = self.downloader.downloade(header,new_url)           
                img_url = self.parser.parser_img_url(page_html)
                num = self.url.add_new_img_urls(img_url)
                print(num)
                #print(img_url)
        except:
            print("爬取图片页面失败")   
            
            
        
        img_num = 1
        try:
            while self.has_new_img_url():
                img_url = self.url.get_new_img_url()
                self.outputer.output(img_url,img_num)
                img_num = img_num + 1     
            
        except:
            print("下载图片失败")
            
                
                
        



if __name__ == "__main__":
    
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 爬取的预览页面数量

    obj_spider = SpiderMain() #构造函数创建爬虫对象
    obj_spider.craw(header) #启动爬虫