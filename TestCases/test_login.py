import time

from Utilities.readproperties import Read_config
from PageObjects.Kekword_Processor import Keyword_Processor
from Utilities import Goexcelmodule as xl

class Test_002_Login:

    baseurl = Read_config.get_url()

    def test_login(self,setup):
        driver = setup
        driver.get(self.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        kp = Keyword_Processor(driver)
        file = "D:\\Automation_Program\\phython\\program\\Keyword_Frame_work\\facebook\\TestData\\creatpagexlfile.xlsx"
        sheet = "Sheet1"
        kp.keyword_sendkeys(xl.readdata(file, sheet, 14, 1), xl.readdata(file, sheet, 14, 2),
                            xl.readdata(file, sheet, 14, 3), xl.readdata(file, sheet, 14, 4))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 15, 1), xl.readdata(file, sheet, 15, 2),
                            xl.readdata(file, sheet, 15, 3), xl.readdata(file, sheet, 15, 4))
        kp.keyword_click(xl.readdata(file, sheet, 16, 1), xl.readdata(file, sheet, 16, 2),
                            xl.readdata(file, sheet, 16, 3))
        time.sleep(3)
        act_title = driver.title
        print(act_title)
        if act_title == "Facebook":
            assert True
            driver.quit()
        else:
            driver.save_screenshot("Screenshoots\\logintest.png")
            driver.quit()
            assert False




