from selenium import webdriver
search_q="avengers endgame"
driver=webdriver.Chrome(executable_path=r"C:\Users\Subham Roy\Documents\Drivers\chromedriver.exe")
driver.maximize_window()

def search_webpage():
#search webpage
  driver.get("https://www.google.com/")
  searchBar=driver.find_element_by_class_name("gLFyf").send_keys(search_q)
  driver.implicitly_wait(2)
  searchBut=driver.find_element_by_class_name("gNO89b")
  searchBut.click()
  driver.implicitly_wait(2)
  firstLink=driver.find_element_by_class_name("LC20lb")
  firstLink.click()
#search webpage

def search_youtube():
#search youtube
  driver.get("https://www.youtube.com/")
  driver.find_element_by_name("search_query").send_keys(search_q)
  driver.implicitly_wait(2)
  driver.find_element_by_id("search-icon-legacy").click()
  driver.implicitly_wait(2)
  links=driver.find_elements_by_id("video-title")
  links[0].click()
#search youtube

def search_wikipedia():
#search wikipedia
  driver.get("https://en.wikipedia.org/wiki/Main_Page")
  driver.find_element_by_name("search").send_keys(search_q)
  driver.implicitly_wait(2)
  driver.find_element_by_name("go").click()
  driver.implicitly_wait(2)
  links=driver.find_elements_by_tag_name("p")
  for link in links:
    if link.text!="":
      print(link.text)
      break
#search wikipedia

while True:
  choice=int(input("Enter 1-Website Search 2-Youtube Search 3-Wikipedia Search"))
  search_q=input("Enter Search Query")
  if choice==1:
    search_webpage()
  elif choice==2:
    search_youtube()
  elif choice==3:
    search_wikipedia()
  else:
    print("Wrong Option")

  again=int(input("Wanna go again? [1-Yes/2-No]"))
  if again==2:
    break

