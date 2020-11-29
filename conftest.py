import pytest
from selenium import webdriver
from py.xml import html

@pytest.fixture(scope="session") # данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию.
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver 
    driver.quit() 
	# код ниже добавляет поля в html-отчет
def pytest_html_report_title(report):
    report.title = "Report"

def pytest_html_results_table_header(cells):
	cells.insert(1, html.th('Description'))	

def pytest_html_results_table_row(report, cells):
	cells.insert(1, html.td( report.description ))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
	pytest_html = item.config.pluginmanager.getplugin('html')
	outcome = yield
	report = outcome.get_result()
	report.description = str( item.function.__doc__ )