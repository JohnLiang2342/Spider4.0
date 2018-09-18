from bs4 import BeautifulSoup




class HtmlParser(object):
    
    
    def get_enter_page(self,soup):
        enter_page = set()
        urls = soup.find(id='maincontent').find_all('a', target='_blank')
        for url in urls:
            enter_page.add(url['href'])
            
        return enter_page
            
    
    
    def parse_enter_page(self,page_html):
        
        if page_html is None:
            return
        
        soup = BeautifulSoup(page_html,"html.parser")
        
        each_page = self.get_enter_page(soup)
        return each_page

    
    def parser_img_url(self,page_html):
        if 
    
    
