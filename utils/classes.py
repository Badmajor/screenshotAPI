import sqlite3

from config import PATH_DB


class DB:
    def __int__(self, num_task: int = 0):
        self.num_task = num_task
        self.connect = sqlite3.connect(PATH_DB)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS num_task(num INT);")
        self.connect.commit()

    def get_num_task(self) -> int:
        self.cursor.execute("SELECT num from num_task;")
        num_task = self.cursor.fetchone()
        if num_task:
            self.connect.close()
            return num_task[0]
        self.cursor.execute("INSERT INTO num_task VALUES(0);")
        self.connect.commit()
        return 0

    def update_num_task(self) -> bool:
        self.cursor.execute("UPDATE num_task SET num = ?;", (self.num_task + 1,))
        self.connect.commit()
        return True

    def reg_task(self, ss_count: int) -> bool:
        self.cursor.execute("INSERT INTO tasks VALUES(?, ?, ?, 0);", (self.num_task, ss_count, ''))
        self.connect.commit()
        return True

    def update_status_task(self, num_operation: int) -> bool:
        self.cursor.execute("UPDATE tasks SET status=? WHERE num=?;", (num_operation, self.num_task))
        self.connect.commit()
        return True

    def update_ss_list(self, ss_list: list) -> bool:
        self.cursor.execute("UPDATE tasks SET list=? WHERE num=?;", (str(ss_list), self.num_task))
        self.connect.commit()
        return True

    def check_status(self) -> int:
        self.cursor.execute("SELECT status FROM tasks WHERE num=?;", (self.num_task,))
        status = self.cursor.fetchone()
        if status:
            return status[0]
        return 0

    def get_ss_list(self) -> str:
        self.cursor.execute("SELECT list FROM tasks WHERE num=?;", (self.num_task,))
        ss_list = self.cursor.fetchone()
        if ss_list:
            return ss_list[0]
        return 'Не номер задания'

    def get_len_task(self) -> int:
        self.cursor.execute("SELECT count FROM tasks WHERE num=?;", (self.num_task,))
        len_task = self.cursor.fetchone()
        if len_task:
            return len_task[0]
        return 0

    def close(self):
        self.connect.close()
