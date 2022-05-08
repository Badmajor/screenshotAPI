import os
import shutil
import zipfile


async def clear_temp():
    shutil.rmtree('temp', ignore_errors=True)
    os.mkdir('temp')


async def create_zip(num_task: int, ss_list: list):
    try:
        with zipfile.ZipFile(f'ss/task_{num_task}.zip', 'a') as zf:
            for file in ss_list:
                zf.write(filename=f'temp/{file}', arcname=file)
        return True
    except Exception as ex:
        return ex
