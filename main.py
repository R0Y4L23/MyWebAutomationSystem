from selenium import webdriver
search_q="avengers endgame"
driver=webdriver.Chrome(executable_path=r"C:\Users\Subham Roy\Documents\Drivers\chromedriver.exe")
driver.maximize_window()


#search webpage
#driver.get("https://www.google.com/")
# searchBar=driver.find_element_by_class_name("gLFyf").send_keys(search_q)
# driver.implicitly_wait(2)
# searchBut=driver.find_element_by_class_name("gNO89b")
# searchBut.click()
# driver.implicitly_wait(2)
# firstLink=driver.find_element_by_class_name("LC20lb")
# firstLink.click()
#search webpage

#search youtube
# driver.get("https://www.youtube.com/")
# driver.find_element_by_name("search_query").send_keys(search_q)
# driver.implicitly_wait(2)
# driver.find_element_by_id("search-icon-legacy").click()
# driver.implicitly_wait(2)
# links=driver.find_elements_by_id("video-title")
# links[0].click()
#search youtube

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
