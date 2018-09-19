


from spider import url_manager, html_parser, html_downloader, img_outputer
import time




class SpiderMain(object):
    
    def __init__(self):
        #初始化各个对象
        self.url = url_manager.UrlManager()
        self.parser = html_parser.HtmlParser()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = img_outputer.ImgOutputer()
        


    
    def craw(self,header):
        
        self.url.get_All_enter_url(header)
        time.sleep(5)    
        print(self.url.has_new_enter_url())                 
        
        while self.url.has_new_enter_url():
            new_url = self.url.get_new_enter_url()
            page_html = self.downloader.downloade(header,new_url)        
            img_title,img_urls = self.parser.parser_img_urlAndtitle(page_html)
            print(img_title)
            print(img_urls)
            folder_name = self.outputer.creat_img_folder(img_title)
            self.outputer.download_img(img_urls,folder_name)
            time.sleep(5)
          
            
            
        
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
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 爬取的预览页面数量

    obj_spider = SpiderMain() #构造函数创建爬虫对象
    obj_spider.craw(header) #启动爬虫