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
driver.execute_script("var courseId='00026';var tableEntries=document.getElementById('pageContent_CourseList_PrimarySections_0_SecondarySections_0').children[0].children;for(var i=0;i<tableEntries.length;i++){var currentId=tableEntries[i].children[0].children[0].children[0].children[0].children[1].innerHTML; currentId=currentId.replace(/&nbsp|;/g,'');var currentSubmit=tableEntries[i].children[0].children[0].children[0].children[0].children;currentSubmit=currentSubmit[currentSubmit.length-1].children[0];if(currentId==courseId){currentSubmit.click();break;}}");
