
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import os
from termcolor import colored
import re    


""" 
http://e-mailid.blogspot.com/
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now') """

response=""
htmlContent=""
soup=""
all_content=""
counter=0

class Scrappy:

        
    def start(self):
        print("                                                                                 ")
        print(colored("**************************SwappyTheScrapy Welcomes You***************************",'blue'))
        print("                                                                                 ")
        print("                                                                                 ")
        print("*********Note :: please maximize your terminal for better experiance  ::*********")
        print("                                                                                 ")
        print("                                                                                 ")
        print("please enter url u want to scrap ...👿   please enter with http/https     ")
        print("                                                                                 ")
        print("                                                                                 ")
        
        global response,htmlContent,soup,all_content,url

        url=input()
        response=requests.get(url)     #request the url content
        htmlContent=response.content

        soup=BeautifulSoup(htmlContent,'html.parser')
        all_content=soup.prettify()
        
        #print("All the elements that were used in feeded url website")
        #getElementsName(self)
    
    def menu(self):
        #counter=1
        print(colored("\n \n make your choice to scrap from the url  ::\n \n","green"))
        print(url)
        print()
        print("1. Title            2.Header              3.Footer            4.body             5.forms")
        print("6. Anchors          7.Images              8.Meta information  9.Links            10.forms detail")
        print("11.Emails           12.Styles             13.Script           14.Paragraphs      15.Div")
        print("16.getElementsName  17.ElementsNamesWithDetails               18. Specific                        ")
        choice=input()
        return(choice)
            #scrap(self,choice)
    #menu(self)
    
###############################################################################################################
###############################################################################################################
    def scrap(self,choice):
        if choice=="1":
            self.getTitle()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="2":
            self.getHeader()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="3":
            self.getFooter()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="4":
            self.getBody()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="5":
            self.getform()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="6":
            self.getAnchors()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="7":
            self.getImages()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="8":
            self.getmeta()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="9":
            self.getLinks()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="10":
            self.getformsDetail()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="11":
            self.getEmails()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="12":
            self.getstyle()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="13":
            self.getScript()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="14":
            self.getParagraphs()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="15":
            self.getDiv()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="16":
            self.getElementsName()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="17":
            self.getElementsNamesWithDetails()
            ch=self.menu()
            self.scrap(ch)
        elif choice=="18":
            print("enter specific tag name data and value :")
            t=input()
            d=input()
            v=input()
            self.getSpecific(t,d,v)
            ch=self.menu()
            self.scrap(ch) 
        elif choice=="q"or choice=="Q":
            print("-----------------Exiting---------------")
            exit()
        else:
            print("invalid input")
        

    def display(self,x,filename):
        if(x=="" or x==None):
            print("########  no values available for requested data on website #########")
        else:
            print("\n\n\n\n################################  your scrapped data #####################################\n\n\n")
            try:
                x1=x.prettify()
                print(x1)
                #print("want to save in local dir..?")
                #yn=input()
                #if yn=='y' or 'Y':
                #    self.saveinFile(x1)
            except:
                print(x)
                #x1=x.prettify()
                print(colored("want to save in local dir..?","green"))
                yn=input()
                if yn=='y' or 'Y':
                    self.saveinFile(x,filename)

    def getElementsName(self):
        elementsSet=set()
        for tag in soup.find_all(True):
            #elementsSet.update(tag)
            print(tag.name)
            if tag in elementsSet:
                pass
                elementsSet=elementsSet.add(tag)
        print(elementsSet)


    def getElementsNamesWithDetails(self):
        for tag in soup(True):
            print(tag.name)
            print(colored(">>>>>>>>","yellow"))
            print(tag)
            print(colored("#############################################","red"))

        #header 
    def getHeader(self):
        header=soup.find('head')#.get_text()
        self.display(header,"head")
    
    def getmeta(self):
        meta=soup.find_all('meta')#.get_text()
        self.display(meta,"meta")


    def getFooter(self):
        footer=soup.find('footer')#.get_text()
        self.display(footer,"footer")

    def getstyle(self):
        styles=soup.find_all('style')
        self.display(styles,"style")

    def getBody(self):
        body=soup.find('body')#.get_text()
        self.display(body,"body")

    def boldContents(self):
        bolds=soup.find('b')#.get_text()
        self.display(bolds,"bolds")
    
   
    def getEmails(self):
        emails=set()
        #print(len(emails))
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com",soup.text, re.I)) # re.I: (ignore case)
        emails.update(new_emails)
        self.display(emails,"emails")


    def getScript(self):
        scriptsUSed= soup.find_all('script')#.get_text()
        self.display(scriptsUSed,"scripts")

    # get form detail
    def getform(self):
        forms= soup.find('form')#.get_Text()
        self.display(forms,"form")

    def getformsDetail(self):
        formsDetail= soup.find('form').get_text()
        self.display(formsDetail,"formsDetail")

    
    # # get paragraph
    def getParagraphs(self):
        paras= soup.find_all('p')#.get_text()
        para=set()
        for i in paras:
            paragraphs=para.add(i.get_text())
            #print(i.get_text())
        self.display(paragraphs,"para")

    # get division
    def getDiv(self):
        div= soup.find('div').get_text()
        self.display(div,"divisions")

    

    def saveAnchors(self,all_links):
        with open('links.txt', 'w') as file: 
            #link = all_links     
            file.writelines("% s\n" % data for data in all_links) 
            print(colored("--------------saved successfully-------------","red"))
        

        # # #get anchors
    def getAnchors(self):
        #burl=url.parser()
        anchorsCount=0
        anchorsAll= soup.find_all('a')
        #print(anchorsAll)
        allAnchorsSet=set()# #links with details
        for links in anchorsAll:
            if(links.get('href') != '#'):
                linkText = links.get('href')
                allAnchorsSet.add(linkText+"\n") 
                anchorsCount+=1
        print(allAnchorsSet)
        print("want to save all the anchors/links : type Y to save ")
        c=input()
        if(c=='y' or c=='Y'):
            self.saveAnchors(allAnchorsSet)
        print(colored('total no. of anchors in the page :'+str(anchorsCount),'green'))    # #print no. of links

    def getLinks(self):
        print(colored("\n first link in the url is .\n","blue"))
        link= soup.find('link') #         .get_text()
        self.display(link,"links")
       # print("\nlink content \n")
        #linkContent= soup.find('link').get_text()
       # print(linkContent)
        #print("all the links ......\n")
       # allLinks=soup.find_all('link')
        #for i in allLinks:
         #   print(allLinks.get_text())

    def getImages(self):
        imgset=set()
        imgs=soup.find_all('img')
        self.display(imgs,"image")
        print("img is as ")
        for img in imgs:
            Images=imgset.add(img)
            #imgUrl = img.a['href'].split("imgurl=")[1]
            #urllib.request.urlretrieve(imgUrl, os.path.basename(imgUrl))
        self.display(Images,"images")

    
    def getTelephone(self):
        try:
            Telephone = soup.findall(itemprop="telephone")#.get_text()
            self.display(Telephone,"contact no.")
        except AttributeError:
            print("Telephone Number: -")

    def getTitle(self):
        title=soup.find('title')#.get_Text()
        self.display(title,"title")


################### a special method  ##################
    def getSpecific(self,tag,data,value):
        results = soup.findAll(tag, {data : value})
        print("your result  is as follow.........:")
        self.display(results,"specific result")
########################################################
    def saveinFile(self,data,filename):
        with open(filename+'.txt', 'w') as file: 
            #link = all_links     
            file.writelines("% s\n" % data) #for data in all_links) 
            print(colored("------------saved successfully-------------","green"))
        


start=Scrappy()
start.start()
ch=start.menu()
#print(type(ch))
start.scrap(ch)
    



#https://www.thepythoncode.com/article/extracting-email-addresses-from-web-pages-using-python


""" print("enter specific tag name data and value :")
t=input()
d=input()
v=input()
start.getSpecific(t,d,v) """