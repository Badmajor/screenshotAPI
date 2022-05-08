import sqlite3
import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)


async def get_num_task():
    try:
        connect = sqlite3.connect(r'db/num_task.db')
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS num_task(num INT);")
        connect.commit()
        cursor.execute("SELECT num from num_task;")
        num_task = cursor.fetchone()
        if num_task:
            connect.close()
            return num_task[0]
        cursor.execute("INSERT INTO num_task VALUES(0);")
        connect.commit()
        connect.close()
        return 0
    except Exception as ex:
        return ex


async def change_num_task(num_task: int):
    try:
        connect = sqlite3.connect(r'db/num_task.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE num_task SET num = ?;", (num_task+1, ))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        return ex


async def reg_task(num_task: int, ss_count: int):
    try:
        connect = sqlite3.connect(r'db/status_tasks.db')
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list LIST, status BOOL);")
        connect.commit()
        cursor.execute("INSERT INTO tasks VALUES(?, ?, [], False);", (num_task, ss_count))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        return ex


async def change_status_task(num_task: int, ss_list):
    try:
        connect = sqlite3.connect(r'db/status_tasks.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE tasks SET list=?, status=True WHERE num=?;", (ss_list, num_task))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        return ex


async def check_status(num_task: int):
    try:
        connect = sqlite3.connect(r'db/status_tasks.db')
        cursor = connect.cursor()
        cursor.execute("SELECT status from num_task WHERE num=?;", (num_task, ))
        status = cursor.fetchone()
        logging.debug(f"{status}")
        connect.close()
        return status
    except Exception as ex:
        return ex


async def get_ss_list(num_task: int):
    try:
        connect = sqlite3.connect(r'db/status_tasks.db')
        cursor = connect.cursor()
        cursor.execute("SELECT list from num_task WHERE num=?;", (num_task, ))
        ss_list = cursor.fetchone()
        logging.debug(f"{ss_list}")
        connect.close()
        return ss_list
    except Exception as ex:
        return ex
