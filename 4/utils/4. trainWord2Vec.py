import os
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import multiprocessing


directory = "./wiki_text_seg"
dire_list = [os.path.join(directory, x) for x in os.listdir(directory)]
output1 = './wiki_seg.100_30_200.model'
output2 = './wiki_seg.100_30_200.vector'


print('-----------Train Word2Vec-------------\n')
print('multiprocessing.cpu_count: {}\n'.format(multiprocessing.cpu_count()))
for i, dire in enumerate(dire_list):
	print('{}.train {}\n'.format(i,dire))
	model = Word2Vec(LineSentence(dire), size=100, window=30, min_count=200,workers=multiprocessing.cpu_count())

model.save(output1)
model.wv.save_word2vec_format(output2, binary=False)
	
