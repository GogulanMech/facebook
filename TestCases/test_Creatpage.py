import time

from selenium import webdriver
from PageObjects.Kekword_Processor import Keyword_Processor
from Utilities import readproperties
from Utilities import Goexcelmodule as xl


class Test_001_creatpage:

    url = readproperties.Read_config.get_url()

    def test_creatpage(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        file = "D:\\Automation_Program\\phython\\program\\Keyword_Frame_work\\facebook\\TestData\\creatpagexlfile.xlsx"
        sheet = "Sheet1"
        kp = Keyword_Processor(driver)
        kp.keyword_click(xl.readdata(file, sheet, 2, 1), xl.readdata(file, sheet, 2, 2), xl.readdata(file, sheet, 2, 3))
        act_title = driver.title
        if act_title == "Facebook – log in or sign up":
            assert True
            driver.quit()
        else:
            driver.quit()
            assert False

    def test_filling_form(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(10)
        file = "D:\\Automation_Program\\phython\\program\\Keyword_Frame_work\\facebook\\TestData\\creatpagexlfile.xlsx"
        sheet = "Sheet1"
        kp = Keyword_Processor(driver)
        kp.keyword_click((xl.readdata(file, sheet, 2, 1)), (xl.readdata(file, sheet, 2, 2)),
                         (xl.readdata(file, sheet, 2, 3)))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 3, 1), xl.readdata(file, sheet, 3, 2),
                            xl.readdata(file, sheet, 3, 3), xl.readdata(file, sheet, 3, 4))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 4, 1), xl.readdata(file, sheet, 4, 2),
                            xl.readdata(file, sheet, 4, 3), xl.readdata(file, sheet, 4, 4))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 5, 1), xl.readdata(file, sheet, 5, 2),
                            xl.readdata(file, sheet, 5, 3), xl.readdata(file, sheet, 5, 4))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 6, 1), xl.readdata(file, sheet, 6, 2),
                            xl.readdata(file, sheet, 6, 3), xl.readdata(file, sheet, 6, 4))
        kp.keyword_sendkeys(xl.readdata(file, sheet, 7, 1), xl.readdata(file, sheet, 7, 2),
                            xl.readdata(file, sheet, 7, 3), xl.readdata(file, sheet, 7, 4))
        kp.keyword_class(xl.readdata(file, sheet, 8, 1), xl.readdata(file, sheet, 8, 2), xl.readdata(file, sheet, 8, 3),
                         xl.readdata(file, sheet, 8, 4), xl.readdata(file, sheet, 8, 5))
        kp.keyword_class(xl.readdata(file, sheet, 9, 1), xl.readdata(file, sheet, 9, 2), xl.readdata(file, sheet, 9, 3),
                         xl.readdata(file, sheet, 9, 4), xl.readdata(file, sheet, 9, 5))
        kp.keyword_class(xl.readdata(file, sheet, 10, 1), xl.readdata(file, sheet, 10, 2), xl.readdata(file, sheet, 10, 3),
                         xl.readdata(file, sheet, 10, 4), xl.readdata(file, sheet, 10, 5))
        kp.keyword_click((xl.readdata(file, sheet, 11, 1)), (xl.readdata(file, sheet, 11, 2)),
                         (xl.readdata(file, sheet, 11, 3)))
        kp.keyword_click((xl.readdata(file, sheet, 12, 1)), (xl.readdata(file, sheet, 12, 2)),
                         (xl.readdata(file, sheet, 12, 3)))
        time.sleep(3)