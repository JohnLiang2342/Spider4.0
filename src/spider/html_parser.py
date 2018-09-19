from bs4 import BeautifulSoup




class HtmlParser(object):
    
    
    def get_enter_url(self,soup):
        enter_url = set()
        urls = soup.find(id='maincontent').find_all('a', target='_blank')
        for url in urls:
            enter_url.add(url['href'])
            
        return enter_url
            
    def get_img_urls(self, soup):
        img_urls = set()
        urls = soup.find(id='picture').find_all('img')
        for url in urls:
            img_urls.add(url['src'])       
        return img_urls
    
    
    def get_img_title(self, soup):
        img_title = soup.find('div',class_='metaRight').find('a').get_text()
        return img_title
    
    
    def parse_enter_url(self,page_html):
        
        if page_html is None:
            return
        
        soup = BeautifulSoup(page_html,"html.parser")
        
        each_url = self.get_enter_url(soup)
        return each_url

    

    def parser_img_url(self,page_html):
        if page_html is None:
            return
        
        soup = BeautifulSoup(page_html,"html.parser")
        
        img_page = self.get_img_page(soup)
        
        return img_page

    
    
    
    
    def parser_img_urlAndtitle(self,page_html):
        if page_html is None:
            return
        
        soup = BeautifulSoup(page_html,"html.parser")
        
        img_title = self.get_img_title(soup)
        img_urls = self.get_img_urls(soup)
        
        return img_title,img_urls
    
    
    
    
    
    
