


from spider import url_manager, html_parser, html_downloader, img_outputer
import time
import random




class SpiderMain(object):
    UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    
    def __init__(self):
        #初始化各个对象
        self.url = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = img_outputer.ImgOutputer()
        


    
    def craw(self):
        
        #self.url.get_All_enter_url(header)
        

        page_number = 1
        while page_number<=1:
            header = {'User-Agent':random.choice(self.UserAgent_List)}
            root_url = "http://www.meizitu.com/a/more_%d.html" %(page_number)
            print(root_url)
            page_html = self.downloader.downloade(header,root_url)
            enter_url = self.parser.parse_enter_url(page_html)
            print(enter_url)
            self.url.add_new_enter_urls(enter_url)
            page_number = page_number + 1
        
        
        #time.sleep(5)    
        print(self.url.has_new_enter_url())                 
        
        try:       
            while self.url.has_new_enter_url():
                header = {'User-Agent':random.choice(self.UserAgent_List)}
                new_url = self.url.get_new_enter_url()
                page_html = self.downloader.downloade(header,new_url)        
                img_title,img_urls = self.parser.parser_img_urlAndtitle(page_html)
                print(img_title)
                print(img_urls)
                folder_name = self.outputer.creat_img_folder(img_title)
                self.outputer.download_img(img_urls,folder_name)
                #time.sleep(5)
          
        except:
            print('爬取图片url失败')  
            
        
#         img_num = 1
#         try:
#             while self.has_new_img_url():
#                 img_url = self.url.get_new_img_url()
#                 self.outputer.output(img_url,img_num)
#                 img_num = img_num + 1     
#                 
#             
#         except:
#             print("下载图片失败")
            
                
                
        



if __name__ == "__main__":
    #Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
    
    
# 爬取的预览页面数量

    obj_spider = SpiderMain() #构造函数创建爬虫对象
    obj_spider.craw() #启动爬虫