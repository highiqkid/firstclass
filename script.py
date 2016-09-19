from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

# Request from user - selecctedVal, class name, and password
password =
selectedVal = 
driver = webdriver.Chrome()
driver.get("https://my.sa.ucsb.edu/gold/login.aspx")
driver.execute_script("document.getElementById('pageContent_userNameText').value = 'victorcheng';")
driver.execute_script("document.getElementById('pageContent_passwordText').value = '';")
driver.execute_script("document.getElementById('pageContent_loginButton').click();")
driver.execute_script("document.getElementById('pageContent_ContinueButton').click();")
driver.execute_script("document.getElementById('ctl07').click();")
driver.execute_script("var selectedVal='ANTH'; var sel=document.getElementById('pageContent_subjectAreaDropDown'); for(var i=0;i<sel.length;i++){if(sel.options[i].value){var noSpaceSel=sel.options[i].value.replace(' ','');}if(noSpaceSel==selectedVal){sel.selectedIndex=i;break;}}");
driver.execute_script("document.getElementById('pageContent_searchButton').click();");
