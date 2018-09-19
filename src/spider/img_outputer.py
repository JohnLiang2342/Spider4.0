
import requests
import os
import time

class ImgOutputer(object):
    
    
    def format_name(self,img_title):
        for i in ['\\','/',':','*','?','"','<','>','!','|','，','！','、','：','？','.','-']:
            while i in img_title:
                img_title = img_title.strip().replace(i, '')
        return img_title
    
    def output(self,img_url,img_num):
        img_data = requests.get(img_url)
        with open('F:\\%d.jpg'%(img_num), 'wb') as f:
            f.write(img_data.content)
            f.close()

    
    def creat_img_folder(self,img_title):
        img_title = self.format_name(img_title)
        os.mkdir('F:\\妹子图\\%s'%img_title)
        print('文件夹'+img_title+'创建成功')
        return self.format_name(img_title)

    
    def download_img(self,img_urls,folder_name):
        num = 1
        for img in img_urls:
            img_data = requests.get(img)
            print(img)
            #img_html.encoding = 'gb2312'
            print(img_data.status_code)
            with open('F:\\妹子图\\%s\\%d.jpg'%(folder_name,num), 'wb') as f:
                f.write(img_data.content)
                f.close()
            num = num+1
            time.sleep(5)
            
    
    
    
    
    
    



