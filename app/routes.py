from flask import json, request

from app import app
from util import check_staus_task, get_list_screenshot, save_screenshot


@app.route('/ch')
def check():
    return 'проверка'


@app.route('/screenshot/', methods=['POST'])
async def post_screenshot():
    return str(await save_screenshot(json.loads(request.data)))


@app.route('/status/<task_id>/', methods=['GET'])
async def get_status(task_id):
    return await check_staus_task(int(task_id))


@app.route('/screenshot/<task_id>/', methods=['GET'])
async def get_screenshot_list(task_id):
    return str(await get_list_screenshot(int(task_id)))
