# encoding=UTF-8
import numpy as np
import pandas as pd
import codecs
# dataFrame =pd.read_excel('testData.xls')
def linear(x):
    y =5.0*x+5.0
    return y

def gx(x):
    y=0
    if x<=0.0:
        y =x
    elif  x>0.0:
        y =10.0*x
    return y
def evalSpearman(Path,newPath):

    dataFrame =pd.read_excel(Path)
    x =dataFrame[['score','similarity']]
    x.to_excel(newPath)
    print x
    print  dataFrame.corr('spearman')

def cosSim(A,B):
    A =np.array(A,dtype='float32')
    B =np.array(B,dtype='float32')
    num =A.dot(B.T)
    denom =np.linalg.norm(A) *np.linalg.norm(B)
    cos = num/denom
    # sim =0.5 + 0.5 * cos
    # return sim
    return cos

def euclideanSim(A,B):
    dist = np.linalg.norm(A - B)
    # sim =1.0/ (1.0+dist)
    sim = dist
    return sim

def mySpearman(A,B):
    N =np.shape(A)[1]
    def rank(A):
        XRank =np.zeros((1,N))
        for i in range(N):
            count1=1
            count2 =-1
            for j in range(N):
                if A[0,i]<A[0,j]:
                    count1=count1+1
                elif A[0,i]==A[0,j]:
                    count2=count2+1
            XRank[0,i]=count1+(count2)/2.0
        return XRank
    XRank =rank(A)
    YRank =rank(B)
    print XRank
    fenzi =6*np.sum((XRank-YRank)**2)
    fenmu =N *(N**2-1)
    coeff =1.0-fenzi/fenmu
    print coeff

def toUnicode(oldpath,newpath):
    f =codecs.open(oldpath,'r',encoding='gbk')
    l =codecs.open(newpath,'w',encoding='utf-8')
    for line in f:
        print line
        l.write(line)
    f.close()
    l.close()

def loadW2v(path,dim):
    f =codecs.open(path,'r',encoding='gbk')
    word =codecs.open('vectors/word.txt','w',encoding='utf-8')
    sysnet =codecs.open('vectors/sysnet.txt','w',encoding='utf-8')
    lexeme =codecs.open('vectors/lexeme.txt','w',encoding='utf-8')
    for line in f :
        if len(line.strip().split(' '))!=dim+1:
            print line
            continue
        if line.split(' ')[0].__contains__(','):
            sysnet.write(line)
        elif line.split(' ')[0].__contains__('-'):
            lexeme.write(line)
        else:
            word.write(line)

    f.close()
    word.close()
    sysnet.close()
    lexeme.close()

def loadDicts(path):
    f =codecs.open(path,'r','utf-8')
    words ={}
    embeddings =[]
    n=0
    for line in f:
        n+=1
        arrays =line.strip().split(' ')
        for w in arrays[1:]:
            embeddings.append(float(w))
        embeddings =np.asarray(embeddings,dtype='float32')
        if not words.has_key(arrays[0]):
            words[arrays[0]]=embeddings
        else:
            print arrays[0]
        embeddings=[]
    f.close()
    print len(words)
    print n
    # print words.get(u'匹夫,个人,')
    # print type(words.get(u'匹夫,个人,'))
    return words
#计算相似度
def calcutaWord(path,embeddings={},dataset='sysnet',savePath=''):
    dataFrame = pd.read_csv(path, sep=' ', names=['word1', 'word2', 'similarity'],encoding='utf-8')
    print dataFrame.head()

    set1,set2 =[],[]
    dataFrame['score']=1
    for i in range(len(dataFrame)):
        maxSim=0
        w1 =dataFrame.iloc[i,0]
        w2 =dataFrame.iloc[i,1]
        for key in embeddings.keys():
            if dataset=='sysnet':
                arrs =key.split(',')
                for a in arrs:
                    if w1==a:
                        set1.append(embeddings.get(key))
                    elif w2 ==a:
                        set2.append(embeddings.get(key))
            elif dataset=='word':
                arrs =key.split(' ')
                for a in arrs:
                    if w1 == a:
                        set1.append(embeddings.get(key))
                    elif w2 == a:
                        set2.append(embeddings.get(key))
            elif dataset=='lexeme':
                arrs =key.split('-')
                for a in arrs:
                    if w1 == a:
                        set1.append(embeddings.get(key))
                    elif w2 == a:
                        set2.append(embeddings.get(key))

        # flag =0
        # for w in set1:
        #     for w2 in set2:
        #         if np.array_equal(w,w2)==True:
        #             flag =1
        if len(set1)==0 or len(set2)== 0:
            maxSim=0
        # elif flag==1:
        #      maxSim =1
        else:
            maxSim=0
            for em in set1: #choose max value as the similarity
                for em2 in set2:
                    sim =cosSim(em,em2)  #余弦距离
                    # sim =euclideanSim(em,em2)  #欧拉距离
                    print sim
                    def toSim(sim):
                        if sim>=1 :
                            sim=1
                        elif sim<=-1:
                            sim=-1
                        else:
                            sim =sim
                        return sim
                    if sim>=maxSim:
                        maxSim=sim
        # if maxSim>=1:
        #     print i
        if maxSim >=1.0:
            maxSim =10
        else:
            maxSim=gx(maxSim)
        # print maxSim
        # maxSim =('%.2f' %maxSim)
        maxSim=round(maxSim,2)
        dataFrame.iloc[i,3]=maxSim
        set1=[];set2=[]

        # sim =cs.similarity(w1,w2)
        # dataFrame.iloc[i,3]=sim
    dataFrame.to_excel(savePath,encoding='utf-8')
if __name__=='__main__':
    print 'hello world...'
    Train =0

    # A =np.asarray([1,2,3],dtype='int32')
    # B = np.asarray([1,3,1],dtype='int32')
    # sim =euclideanSim(A,B)
    # sim2 =cosSim(A,B)
    # print sim,sim2
    # print np.dot(A,B)
    if Train ==1:
        print 'train...'
        embeddings = loadDicts('vectors/lexeme.txt')
        calcutaWord('nlpcc2016.txt',embeddings,'lexeme','nlpcc.xls')
    elif Train==0:
        print 'eval....'
        path =['nlpcc.xls','sp.xls']
        evalSpearman(path[0],path[1])
    def calSenseEmbedding():
        #Autoextend 将auto生成的词向量分解成同义词集、词跟向量
        #加载词向量，利用余弦相似度计算得分
        loadW2v('vectors/outputVectors.txt',300)
        embeddings =loadDicts('vectors/sysnet.txt')
        calcutaWord('ploymous.txt',embeddings)
