
import requests

class ImgOutputer(object):
    
    
    def output(self,img_url,img_num):
        img_data = requests.get(img_url)
        with open('F:\\%d.jpg'%(img_num), 'wb') as f:
            f.write(img_data.content)
            f.close()
    
    



