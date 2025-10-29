# 🧠 Полуфинал: Автоматизация тестирования (Python)

## 🧩 Задание
Автоматизация проверки страниц с упражнениями:
- [Form Fields](https://practice-automation.com/form-fields/)
- [Click Events](https://practice-automation.com/click-events/)
- [Popups](https://practice-automation.com/popups/)

## ⚙️ Технологии
- Python 3.12+
- Selenium 4.x
- Pytest
- Allure Reports
- WebDriverManager

## 🚀 Как запустить
```bash
pip install -r requirements.txt
pytest --browser=chrome --alluredir=allure-results
allure serve allure-results
```
