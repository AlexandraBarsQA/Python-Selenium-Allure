import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.mark.xfail(reason="Wait for fix bug")

def test_my_site():
    """
    Test case MS-1
    
    """
    """
    exp_skills = [
      {'Веб-технологии:': 'HTML / CSS / JavaScript'},
      {'Базы данных:': 'MySQL'},
      {'API:': 'Postman'},
      {'Proxy:': 'Charles'}
    ]

    """

    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://alexandrabarsqa.github.io/"
    driver.get(url=url)

    url = driver.current_url

    skills = driver.find_element(by=By.CSS_SELECTOR, value="#skills h2")
    assert skills.text == "Технические навыки:", "Неверный текст в загаловке"
    assert "навыки" in skills.text, "Текст не содержит слово навыки"

    li_list = driver.find_elements(by=By.CSS_SELECTOR, value="#skills ul li")
    for li in li_list:
      
      assert li_list, ""

