# Cilin  
利用同义词词林进行词语相似度计算

## 实验数据
NLPCC2016 词语相似度任务（500对词）和Chinese ploymous words （401）对词
## 实验方法
利用词向量（word）、词素向量（lexeme）、同义词集向量（sysnet）分别计算余弦相似度，求得词语直接相似度
通过线性函数将余弦相似度[-1,1]转化为[0,10]之间的数，利用斯皮尔曼相关系数（Spearman rank）求得结果
## 词林
哈工大同义词词林1.0版本
## 运行程序
python Spearman.py  
