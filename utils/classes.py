import sqlite3

from config import PATH_DB


async def get_num_task() -> int:
    with sqlite3.connect(PATH_DB) as connect:
        cursor = connect.cursor()
        cursor.execute("SELECT num from num_task;")
        num_task = cursor.fetchone()
        if num_task:
            return num_task[0]
        cursor.execute("INSERT INTO num_task VALUES(0);")
        connect.commit()
    return 0


class DB:
    def __init__(self, num_task: int = 0):
        self.num_task = num_task
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS num_task(num INT);")
            connect.commit()
            cursor.execute("CREATE TABLE IF NOT EXISTS tasks(num INT, count INT, list STR, status INT);")
            connect.commit()

    def update_num_task(self) -> bool:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("UPDATE num_task SET num = ?;", (self.num_task + 1,))
            connect.commit()
        return True

    def reg_task(self, ss_count: int) -> bool:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO tasks VALUES(?, ?, ?, 0);", (self.num_task, ss_count, ''))
            connect.commit()
        return True

    def update_status_task(self, num_operation: int) -> bool:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("UPDATE tasks SET status=? WHERE num=?;", (num_operation, self.num_task))
            connect.commit()
        return True

    def update_ss_list(self, ss_list: list) -> bool:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("UPDATE tasks SET list=? WHERE num=?;", (str(ss_list), self.num_task))
            connect.commit()
        return True

    def check_status(self) -> int:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT status FROM tasks WHERE num=?;", (self.num_task,))
            status = cursor.fetchone()
        if status:
            return status[0]
        return 0

    def get_ss_list(self) -> str:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT list FROM tasks WHERE num=?;", (self.num_task,))
            ss_list = cursor.fetchone()
        if ss_list:
            return ss_list[0]
        return 'Не номер задания'

    def get_len_task(self) -> int:
        with sqlite3.connect(PATH_DB) as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT count FROM tasks WHERE num=?;", (self.num_task,))
            len_task = cursor.fetchone()
        if len_task:
            return len_task[0]
        return 0
