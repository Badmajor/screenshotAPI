import os

from utils.db import get_num_task, change_num_task, reg_task, change_status_task, check_status, get_ss_list
from utils.other import clear_temp, create_zip

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


async def save_ss(url_list: list) -> int or str:
    await clear_temp()
    ss_count = len(url_list)
    num_task = await get_num_task()
    await reg_task(num_task, ss_count)
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
    ss_list = os.listdir('temp')
    await create_zip(num_task, ss_list)
    await change_status_task(num_task, ss_list)
    await change_num_task(num_task)
    return num_task


async def check_status_task(task_id: int):
    num_task = await get_num_task()
    if num_task < task_id:
        return 'Не верный номер задачи'
    if num_task > task_id:
        return 'Задача готова'
    if not await check_status(task_id):
        return 'Задача в процессе'
    return 'Не верный номер задачи'


async def get_list_screenshot(task_id):
    ss_list = await get_ss_list(task_id)