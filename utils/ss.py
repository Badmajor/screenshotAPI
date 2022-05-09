import logging
import os

from utils.classes import DB
from utils.other import clear_temp, create_zip

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


async def save_ss(url_list: list) -> int or str:
    await clear_temp()
    ss_count = len(url_list)
    task = DB()
    num_task = task.get_num_task()
    task.num_task = num_task
    task.reg_task(ss_count)
    num = 0
    for i in url_list:
        opt = Options()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--headless')
        brow = webdriver.Firefox(
            options=opt, executable_path=f'{os.path.abspath(os.path.dirname("geckodriver"))}/geckodriver'
        )
        brow.get(i)
        brow.save_screenshot(f'temp/{num_task}-{num}.png')
        num += 1
        task.update_status_task(num)
    ss_list = os.listdir('temp')
    await create_zip(num_task, ss_list)
    task.update_ss_list(ss_list)
    task.update_num_task()
    task.close()
    return num_task


async def check_status_task(task_id: int):
    task = DB()
    num_task = task.get_num_task()
    task.num_task = task_id
    if num_task > task_id:
        task.close()
        return 'Задача готова'
    status = task.check_status()
    len_task = task.get_len_task()
    if status:
        task.close()
        return f'Задача в процессе, готово {status} из {len_task} '
    task.close()
    return 'Не верный номер задачи'


async def get_list_screenshot(task_id):
    task = DB()
    task.num_task = task_id
    ss_list = task.get_ss_list()
    logging.info(ss_list)
    if ss_list:
        task.close()
        return ss_list
    task.close()
    return 'Ошибка'
