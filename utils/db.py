import sqlite3
import logging

logging.basicConfig(
    level=logging.INFO)

path_db = r'db/tasks.db'


async def get_num_task():
    try:
        connect = sqlite3.connect(path_db)
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
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS num_task(num INT);")
        connect.commit()
        cursor.execute("UPDATE num_task SET num = ?;", (num_task+1, ))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        return ex


async def reg_task(num_task: int, ss_count: int):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("INSERT INTO tasks VALUES(?, ?, ?, 0);", (num_task, ss_count, ''))
        connect.commit()
        connect.close()
        logging.info(f"пучком")
        return True
    except Exception as ex:
        logging.info(ex, 51)
        return ex


async def change_status_task(num_task: int, num: int):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("UPDATE tasks SET status=? WHERE num=?;", (num, num_task))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        logging.info(f"{ex} 65")
        return ex


async def change_ss_list(num_task: int, ss_list:list):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("UPDATE tasks SET list=? WHERE num=?;", (str(ss_list), num_task))
        connect.commit()
        connect.close()
        return True
    except Exception as ex:
        logging.info(f"{ex} 78")
        return ex


async def check_status(num_task: int):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("SELECT status FROM tasks WHERE num=?;", (num_task, ))
        status = cursor.fetchone()
        logging.info(f"СТатус{status}")
        connect.close()
        if status:
            return status[0]
        return 0
    except Exception as ex:
        logging.info(ex, 93, type(ex))
        return 0


async def get_ss_list(num_task: int):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("SELECT list FROM tasks WHERE num=?;", (num_task, ))
        ss_list = cursor.fetchone()
        connect.close()
        if ss_list:
            return ss_list[0]
        return ss_list
    except Exception as ex:
        logging.info(ex, 107)
        return 0


async def get_len_task(num_task: int):
    try:
        connect = sqlite3.connect(path_db)
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list TEXT, status INT);")
        connect.commit()
        cursor.execute("SELECT count FROM tasks WHERE num=?;", (num_task, ))
        len_task = cursor.fetchone()
        connect.close()
        if len_task :
            return len_task [0]
        return len_task
    except Exception as ex:
        logging.info(ex, 119)
        return 0
