from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from test.testrail import APIClient


class TestClass1:
    def test_method1(self):
        print("TestClass1 : - I am Method 1 Emailid =  oex02445@eoopy.com  Password = Selenium@123")

        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        driver = webdriver.Remote(
            command_executor='https://testuser1319:kqwyxq2TqmGvA5zYNyXp@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=desired_cap)
        driver.get("https://www.google.com")
        if not "Google" in driver.title:
            raise Exception("Unable to load google page!")
        elem = driver.find_element_by_name("q")
        elem.send_keys("cybage")
        elem.submit()
        print(driver.title)
        driver.quit()
        client = APIClient('https://dar20409.testrail.io')
        client.user = 'dar20409@bcaoo.com'
        client.password = 'Selenium@123'
        run_id =2
        case_id =1
        status_id =5
        msg = "This is working fine marked Passed By Selenium Thanks NKY"
        result = client.send_post(
            'add_result_for_case/%s/%s'%(run_id,case_id),
                {'status_id': status_id, 'comment': msg })
        print(result)



