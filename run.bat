@echo off
call C:\Users\Roshan\PycharmProjects\nopcommerce\venv\Scripts\activate
pytest -v -s --html .\reports\test_report.html --browser chrome
pause