# -*- coding: utf-8 -*-

import os, sys

cur_dir = os.path.abspath(os.path.dirname(__file__))      # 返回当前文件所在的目录
if cur_dir not in sys.path:
    sys.path.append(cur_dir)


def list_to_str(a_list):
    return "".join(list(map(str, a_list)))
