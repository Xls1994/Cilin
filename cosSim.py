# coding: utf-8

def cos(vector1,vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        print normA
        return dot_product / ((normA*normB)**0.5)

def cosNumpy(A,B):
    import  numpy as np
    A = np.array(A,dtype='float32')
    B = np.array(B,dtype='float32')
    num =A.dot(B.T)

    denom =np.linalg.norm(A)* np.linalg.norm(B)
    print np.linalg.norm(A)
    return (num/denom)

def loadSys(path,repath):
    import  codecs
    re =codecs.open(repath,'w',encoding='utf-8')
    with codecs.open(path,'r',encoding='utf-8')as f:
        for line in f:
            arr =line.strip().split(' ')
            w =arr[0].split(',')
            for ww in w:
                if ww==u'对':
                    re.write(line)
                elif ww==u'对于':
                    re.write(line)
    re.close()

def loadDict(path):
    import codecs
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
    return words
if __name__=='__main__':

    import  numpy as np
    from Spearman import calcutaWord
    # A =np.loadtxt('vec.txt',delimiter=' ',dtype='float32')
    #
    # print cos(A,A)
    #
    # print cosNumpy(A,A)
    embeddings =loadDict('dicts.txt')
    calcutaWord('11',embeddings)
# path =['vectors/sysnet.txt','dicts.txt']
# loadSys(path[0],path[1])