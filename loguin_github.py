from time import sleep
from selenium import webdriver
# Primeiro de tudo verifica a sua verão do Chromeeeeee como ? abaixo....
# Na parte superior, clique no tipo de versão do Chrome cujos detalhes você quer ver:
# Versões do navegador ou Versões do ChromeOS. Clique no número da versão de lançamento principal para ver detalhes sobre as versões secundárias.
# baixar o executável chromedriver.exe COMPATIVEL com a versao do seu Chrome
# salve na mesma pasta do seu projeto, caso contrário tera que ficar identificando onde ele esta....
# driver = webdriver.Chrome("D:\Python Projects\loguin_site\chromedriver")

class WebDriverManager:
    def __init__(self, driver_path='D:/Python Projects'):
        self.driver_path = driver_path
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(self.driver_path)

    def get_driver(self):
        if not self.driver:
            self.start_driver()
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()

class GitHubLoginAutomation:
    def __init__(self, usuario, senha):

        self.usuario = usuario
        self.senha = senha

    def login(self):
        url = ("https://github.com/login")
        usuario = 'usuario'
        password = '12234'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element("id", "login_field").send_keys(usuario)
        driver.find_element("id", "password").send_keys(password)
        driver.find_element("name", "commit").click()
        sleep(18)

def main():
    url = "https://github.com/login"
    usuario = 'usuario'
    senha = '12234'

    github_login = GitHubLoginAutomation(usuario, senha)
    github_login.login()

if __name__ == "__main__":
    main()
