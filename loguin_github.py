from time import sleep
from selenium import webdriver
# Primeiro de tudo verifica a sua verão do Chromeeeeee como ? abaixo....
# Na parte superior, clique no tipo de versão do Chrome cujos detalhes você quer ver:
# Versões do navegador ou Versões do ChromeOS. Clique no número da versão de lançamento principal para ver detalhes sobre as versões secundárias.
# baixar o executável chromedriver.exe COMPATIVEL com a versao do seu Chrome
# salve na mesma pasta do seu projeto, caso contrário tera que ficar identificando onde ele esta....
# driver = webdriver.Chrome("D:\Python Projects\loguin_site\chromedriver")


url = ("https://github.com/login")
usuario = 'usuario'
password = '12234'

driver = webdriver.Chrome()
driver.get(url)


driver.find_element("id", "login_field").send_keys(usuario)

driver.find_element("id", "password").send_keys(password)

driver.find_element("name", "commit").click()
sleep(2000)


sleep(2000)