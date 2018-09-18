from bs4 import BeautifulSoup




class HtmlParser(object):
    
    
    def get_enter_url(self,soup):
        enter_url = set()
        urls = soup.find(id='maincontent').find_all('a', target='_blank')
        for url in urls:
            enter_url.add(url['href'])
            
        return enter_url
            
    def get_img_page(self, soup):
        img_url = set()
        urls = soup.find(id='picture').find_all('img')
        for url in urls:
            img_url.add(url['src'])
            
        return img_url
    
    
    
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
    
    
    
    
