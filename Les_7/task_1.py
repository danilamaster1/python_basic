"""1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp"""

import os

p_list = {'my_proj': [{'set': []}, {'mainapp': []}, {'adm': []}, {'authapp': []}]}

for key, val in p_list.items():
    if not os.path.exists(key):
        for item in val:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))

