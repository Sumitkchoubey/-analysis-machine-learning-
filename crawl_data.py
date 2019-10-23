import requests 
from fake_useragent import UserAgent
import requests
from selenium import webdriver
import unicodecsv as csv
import time

def crawl_data():
  path = r'E:/internship project/chromedriver.exe'
  ua = UserAgent()
  header = {'User-Agent':str(ua.chrome)}
  driver = webdriver.Chrome(executable_path = path)
  driver.get('https://www.theguardian.com/environment/2019/oct/02/how-worried-should-we-be-about-microplastics#comments')
  quote=[]
  sidebar = driver.find_element_by_class_name('pagination__list')
  elementList1 = sidebar.find_elements_by_tag_name("span")
  if driver.find_element_by_xpath("//button[contains(.,'View more comments')]").is_displayed():
                    element = driver.find_element_by_xpath("//button[contains(.,'View more comments')]")
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    element.click()
  time.sleep(20)
  comment = driver.find_elements_by_xpath('//div[@class="d-comment__body"]')
            
  date=driver.find_elements_by_xpath('//time[@class="js-timestamp"]')
  username = driver.find_elements_by_xpath('//span[@class="d-comment__author"]')
  num_page_items = len(comment)
  for i in range(num_page_items):
        
                                      quotes={}
                                      quotes['username']=username[i].text
                                      quotes['date']=date[i].text
                                      quotes['comment']=(comment[i].text).rstrip("\n").split(",")
                                      quote.append(quotes)
                                      #print(quote)
  elementList = sidebar.find_elements_by_tag_name("a")
  for i in range(len(elementList)):
                             element = driver.find_element_by_class_name('pagination__list').find_elements_by_tag_name("a")[i]
                             driver.execute_script("arguments[0].click();", element)
                 
                             time.sleep(30)
                             comment = driver.find_elements_by_xpath('//div[@class="d-comment__body"]')
     
                             username = driver.find_elements_by_xpath('//span[@class="d-comment__author"]')
                             date=driver.find_elements_by_xpath('//time[@class="js-timestamp"]')
                             num_page_items = len(comment)
                             for i in range(num_page_items):
        
                                         quotes={}
                                         quotes['username']=username[i].text
                                         quotes['date']=date[i].text
                                         quotes['comment']=(comment[i].text).rstrip("\n").split(",")
        #s=pd.DataFrame(list(quotes.items()), columns=['username', 'comment'])
                                         quote.append(quotes)
  keys=quote[0].keys()
  with open('crawl_data.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(quote)
crawl=crawl_data()