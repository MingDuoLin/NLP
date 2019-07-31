import os

"""
Reference: https://blog.csdn.net/weixin_40400177/article/details/79366065
"""

directory = './extract_wiki_text'
dire_list = [os.path.join(directory,x) for x in os.listdir(directory)]
out_dire = "./wiki_text"
out_dire_list = [os.path.join(out_dire, x) for x in os.listdir(directory)]

for i,dire in enumerate(dire_list):
	line = 'opencc -i {} -o {} -c t2s.json'.format(dire, out_dire_list[i])
	os.system(line)
	print('finish:{}'.format(line))
	
	