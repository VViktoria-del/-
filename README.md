Развёртывание проекта

Скачай архив из репозитория

Распакуй, например в C:\users\user\projects\practice_automation_tests

В проводнике: Shift + ПКМ → Open PowerShell window here
или открой cmd и перейди в папку:

cd C:\projects\practice_automation_tests

Установка зависимостей
pip install -r requirements.txt


Если предупреждение о pip — обнови:

python -m pip install --upgrade pip

Запуск тестов
pytest --browser=chrome --alluredir=allure-results

Длякорректной работы используйте это:
- Python 3.12+
- Selenium 4.x
- Pytest
- Allure Reports
- WebDriverManager

git init
git add .
git commit -m "Practice Automation semifinals tests"
git branch -M main
git remote add origin https://github.com/ВАШ_АККАУНТ/practice_automation_tests.git
git push -u origin main
