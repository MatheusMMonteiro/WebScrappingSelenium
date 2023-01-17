from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
options = Options() 
options.add_experimental_option("detach", True) #mantém o webdriver aberto após execução
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.headless = True # esconder o webdriver
# options.add_argument("--window-size=1920,1200")


DRIVER_PATH = 'C:\Program Files\edge\msedgedriver'

service = Service("C:\Program Files\edge\msedgedriver")

driver = webdriver.Edge(options=options, service=Service(DRIVER_PATH))

driver.get('https://www.loteriasonline.caixa.gov.br/')


btn_year = driver.find_element('id', 'botaosim').click()

btn_loto = driver.find_element('class name', 'titulo-mega-sena').click()

numbers = ["05","03", "04", "15", "20", "08"]

div_element = driver.find_element('class name', 'coluna-aposte')
#driver.execute_script("arguments[0].scrollIntoView();", div_element)
#time.sleep(1)
for x in numbers:
    driver.find_element('xpath', "//*[@id='n%s']" %x ).click()


driver.find_element('id', 'colocarnocarrinho').click()