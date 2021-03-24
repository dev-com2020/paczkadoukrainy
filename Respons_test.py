from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def respons_check(w, file):
    height = 768
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(w, height)
    driver.get(url='https://paczkadoukrainy.pl')
    driver.save_screenshot(file)
    print("Screenshot OK!")
