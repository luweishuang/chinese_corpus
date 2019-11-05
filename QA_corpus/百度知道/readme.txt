百度知道语料集
	链接: https://pan.baidu.com/s/19enwOww3rcdiDm1ysFn2DQ  密码: vd05

来自 https://github.com/SophonPlus/ChineseNlpCorpus, 语料做了加工处理：
	1.过滤了id、url、qid、reply_t、user字段
	2.对question、reply做了脱敏处理

code 示例
	import pandas as pd
	file_path = "文件所在路径"
	pd_all = pa.read_csv(file_path)
	pd_all.sample(n=20)
