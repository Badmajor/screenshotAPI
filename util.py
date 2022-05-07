import os
import sqlite3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


async def get_task(len_list) -> int:
    connect = sqlite3.connect(r'tasks.db')
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(task INT, len INT);")
    connect.commit()
    cursor.execute("SELECT * FROM tasks;")
    a = cursor.fetchall()
    count = len(a)
    cursor.execute("INSERT INTO tasks VALUES(?, ?);", (count, len_list))
    connect.commit()
    connect.close()
    return count


async def save_screenshot(list_url: list[str]) -> int:
    num_task = await get_task(len(list_url))
    num = 0
    for i in list_url:
        opt = Options()
        opt.add_argument('--no-sandbox')
        opt.add_argument('--headless')
        brow = webdriver.Firefox(
            options=opt, executable_path=f'{os.path.abspath(os.path.dirname("geckodriver"))}/geckodriver'
        )
        brow.get(i)
        brow.save_screenshot(f'ss/{num_task}-{num}.png')
        num += 1
    return num_task


async def get_list_screenshot(task_id: int):
    d = 'ss'
    list_ss = []
    for i in os.listdir(d):
        if int(i.split('-')[0]) == task_id:
            list_ss.append(i)
    return list_ss if len(list_ss) > 0 else 'не верный номер задачи'


async def check_status_task(task_id: int) -> str:
    connect = sqlite3.connect(r'tasks.db')
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT);")
    connect.commit()
    cursor.execute("SELECT * FROM tasks;")
    a = cursor.fetchall()
    count = len(a)
    if task_id+1 < count:
        return 'Задача готова'
    elif task_id+1 == count:
        d = 'ss'
        count_file = 0
        for i in os.listdir(d):
            if int(i.split('-')[0]) == task_id:
                count_file += 1
        if count == count_file:
            return 'Задача готова'
        else:
            return 'Задача в процессе'
    else:
        return 'не верный номер задачи'
