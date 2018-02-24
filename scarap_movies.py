#!C:\Python36\python.exe 
from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import cgi
from pickle import dump,load
import json,random
import time
from get_ip import IP
import winsound

class Movie:
        def __init__(self):
                try:
                        self.f1=open('movies_data.txt','rb')
                        self.prev=load(self.f1)
                        self.f1.close()
                except:
                        self.prev=[]
                self.i=IP()
        
        def get_ip(self):
                return self.i.ip()
        def make_request(self,url,browser,ip):
                proxies_req = Request(url)
                proxies_req.add_header('User-Agent', browser)
                proxies_req.set_proxy(ip,'http')
                print(ip)
                return proxies_req
        def scrape_data(self,n):
                browser,ip=self.get_ip()
                browser=browser.random
                url = "http://extramovies.cc/page/"+str(n)
                pro_req=self.make_request(url,browser,ip)
                html = urlopen(pro_req).read().decode('utf8')

                soup=BeautifulSoup(html,"lxml")
                movies = soup.findAll("div", {"class": "thumbnail"})
                all_data=[]
                prev_title=[]
                for i in self.prev:
                        prev_title.append(i[0])
                try:
                        for every_movie in movies:
                                a_tag=every_movie.findAll("a")
                                img_tag=every_movie.findAll("img")
                                src=img_tag[0].attrs['src']
                                title=a_tag[0].attrs["title"]
                                link=a_tag[0].attrs["href"]
                                if title in prev_title:
                                        image,final=self.get_download_links(link,browser,ip)
                                        sample=[title,image,final,src]
                                        all_data.append(sample)
                                        print("Scrapped")
                except Exception as e:
                        print(e)
                finally:
                        new_title=[]
                        final_data=[]
                        for i in all_data:
                                new_title.append(i[0])
                        for i in range(len(new_title)):
                                if new_title[i] not in prev_title:
                                        final_data.append(all_data[i])
                        self.prev=final_data + self.prev
                        f1=open('movies_data.txt','wb+')
                        dump(self.prev,f1,protocol=2)
                        f1.close()
                        print("Done")
                        frequency = 2500
                        duration = 500
                        winsound.Beep(frequency, duration)
        def get_download_links(self,url,browser,ip):
                try:
                        movie_link=Request(url)
                        movie_link.add_header('User-Agent', browser)
                        movie_link.set_proxy(ip,'http')
                        html = urlopen(movie_link).read().decode('utf8')
                        soup=BeautifulSoup(html,"lxml") 
                        img=soup.findAll("img",{"class": "alignnone"})
                        d_link=soup.findAll("a",{"class": "buttn blue"})
                        f_link='http://extramovies.cc'+str(d_link[0].attrs["href"])
                                        
                        movie_link =Request(f_link)
                        movie_link.add_header('User-Agent', browser)
                        movie_link.set_proxy(ip,'http')
                                        
                        html = urlopen(movie_link).read().decode('utf8')
                        soup2=BeautifulSoup(html,"lxml")
                        last_link=soup2.findAll("a")
                        final=last_link[len(last_link)-3].attrs["href"]
                        images=[]
                        for j in range(1,len(img)):
                                k=img[j].attrs["src"]
                                images.append(k)
                        #result=[images,final]
                        #completed.append(result)
                        return images,final
                except Exception as e:
                        print(e)

#getting new movie links 
#mv=Movie()
pages=range(1,2)
for i in pages:
        mv=Movie()
        print("Page"+str(i))
        mv.scrape_data(i)
        #mv.get_download_links()

#mv.scrape_data('4')

#getting download links of movies
#mv.get_download_links()
