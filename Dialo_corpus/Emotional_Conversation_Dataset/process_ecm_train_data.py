# -*- coding: utf-8 -*-

import os, sys
import json
from Dialo_corpus import utils

cur_dir = os.path.abspath(os.path.dirname(__file__))      # 返回当前文件所在的目录
if cur_dir not in sys.path:
    sys.path.append(cur_dir)

lines_all = []
data_path = os.path.join(cur_dir, 'data/train_data.json')
with open(data_path, 'r', encoding='utf8') as fr:
    lines_all = json.load(fr)
print("lines_all's length = ", len(lines_all))

lines_new = []
for cur_lines in lines_all:
    assert 2 == len(cur_lines)
    new_line = cur_lines[0][0].strip() + "<--->" + cur_lines[1][0].strip()
    lines_new.append(new_line)
print("lines_new's length = ", len(lines_new))

data_path_saves = os.path.join(cur_dir, 'data/train_data_processed.json')
with open(data_path_saves, 'w') as fw:
    json.dump(lines_new, fw, ensure_ascii=False)

