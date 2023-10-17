import time
from conf import cf
from log.logger import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time


def login(driver):
    driver.get(cf.get('url', 'login_url'))
    time.sleep(1)
    driver.find_element(By.ID, 'user_name').send_keys(cf.get('auth', 'user_name'))
    driver.find_element(By.ID, 'input_password').send_keys(cf.get('auth', 'password'))
    driver.find_element(By.ID, 'submitId').click()
    time.sleep(1)
    driver.get(cf.get('url', 'task_url'))
    time.sleep(1)


def get_status(driver):
    row = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div[3]/table').text
    row_lis = row.split()
    time.sleep(2)
    return row_lis


def main():
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Firefox(service=Service('geckodriver'), options=option)
    #driver = webdriver.Firefox(service=Service('D:\\devlop\\dazahui\\code\\python\\py_qzzdh\\util\\geckodriver.exe'), options=option)
    #driver = webdriver.Firefox(options=option)
    #driver = webdriver.Chrome(service=Service('D:\\devlop\\dev\\dazahui\\code\\python\\py_qzzdh\\util\\chromedriver.exe'),options=option)

    # 先登录平台
    login(driver)
    # 获取当前任务状态
    status = get_status(driver)[1]
    logger.info(status)
    if status == 'STOPPED' or status == 'SUCCEEDED':
        logger.info('项目已停止，准备重启')
        # 点击重新调试
        driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div[3]/table/tbody/tr/td[6]/div/div/a[1]').click()
        time.sleep(3)
        while True:
            status = get_status(driver)[1]
            logger.info(status)
            if status == 'WAITING':
                logger.info('项目正在重启中')
                time.sleep(30)
            elif status == 'RUNNING':
                logger.info('项目重启成功，准备开始调试')
                # 点击调试
                driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div/div[3]/table/tbody/tr/td[6]/div/div/a[1]').click()
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(3)
                lis = driver.find_elements(By.CLASS_NAME, 'jp-LauncherCard')
                # 点击进入命令行
                lis[2].click()
                time.sleep(10)
                # 键入相关命令
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys('bash').perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys(Keys.ENTER).perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys('cd /code').perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys(Keys.ENTER).perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys('./start_app.sh').perform()
                time.sleep(1)
                ActionChains(driver).move_to_element(driver.switch_to.active_element).send_keys(Keys.ENTER).perform()
                time.sleep(300)
                driver.quit()
                logger.info('项目调试完成')
                break


if __name__ == '__main__':
    while True:
        main()
        #  2个小时执行一次
        #time.sleep(3600*2)
        #  方便测试 5分钟执行一次
        time.sleep(300)

# while True:
#     now = datetime.datetime.now().time()  # 获取当前时间
#     start_time = datetime.time(8, 0, 0)  # 设置开始时间为8点
#     end_time = datetime.time(20, 0, 0)  # 设置结束时间为20点
#     if start_time <= now <= end_time:  # 判断当前时间是否在8点到20点之间
#         logger.info('工作时间项目执行')
#         main()  # 如果是，则执行 main() 函数
#     else:
#         logger.info('休息时间项目不执行')
#     time.sleep(300)  # 每5分钟执行一次

