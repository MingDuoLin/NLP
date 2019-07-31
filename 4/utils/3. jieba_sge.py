import os
import json
import jieba
from string import punctuation


add_punc='·，。、【 】 “”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥「」′° —『』'
all_punc=punctuation+add_punc

directory = "./wiki_text"
file_list = [os.path.join(directory, x) for x in os.listdir(directory)]
out_dire = "./wiki_text_seg"
out_file_list = [os.path.join(out_dire, x) for x in os.listdir(directory)]

for i,file in enumerate(file_list):
	#if i == 1: break
	fp_re = open(file,'r', encoding = "utf-8")
	fp_wr = open(out_file_list[i], 'w', encoding = "utf-8")
	for line in fp_re.readlines():
		# 分词
		line_seg = " ".join(jieba.cut(line))
		# 移除标点符号
		item_list = [item.strip() for item in line_seg if item.strip() not in all_punc if not item.strip().isdigit()]
		# 再次分词
		line_seg_ = " ".join(jieba.cut(''.join(item_list)))
		fp_wr.write(line_seg_)
	
	fp_re.close()
	fp_wr.close()
	print('{}:{} Finish'.format(i, file))