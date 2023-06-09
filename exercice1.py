
import time
import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec  # on a utilisé l'alias
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

wait=WebDriverWait(driver,10)  #l'explicite wait prend comme parametre le driver et le temps limite d'attente

def test_iframe():
    driver.get("https://videotron.com/")
    driver.maximize_window()
    #images du site
    print("**************************************************************************************************")
    liste_img=driver.find_elements(By.XPATH,"//*[name()='svg' or name()='img']")
    print("le nombre total des image =  ",len(liste_img))
    for img in liste_img:
        print(img.get_attribute('alt'))
    #lien du site
    print("**************************************************************************************************")
    liste_lien=driver.find_elements(By.TAG_NAME,"a")
    print("le nombre total des liens =  ", len(liste_lien))
    for lien in liste_lien:
        url= lien.get_attribute('href')
        print(url)
    #lien du footer
    print("**************************************************************************************************")
    lien_footer=driver.find_elements(By.XPATH,"//footer//span | //footer//a")
    print("le nombre total des liens dans le footer=  ", len(lien_footer))
    for lien in lien_footer:
        url=lien.get_attribute('href')
        print(url)
    driver.quit()