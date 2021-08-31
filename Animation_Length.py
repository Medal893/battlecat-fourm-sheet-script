#f = open('044_f02.maanim', 'r',encoding="utf-8")
import numpy as np
#raw = f.readline() # skip first junk

#f = stage1
#c = stage2
#s = stage3
#e = enemy
def getAniLength(name,stage):
    maximum = 0;
    times = 0;
    totaltime = 0
    intname = int(name)
    intname = intname-1 #Shit Shift between module definition(start from 0) and unit definition(start from 1)
    if intname<=9:
        strname = "00"+str(intname)
    elif intname<=99:
        strname = "0"+str(intname)
    else:
        strname = str(intname)
    if stage ==0:
        filename = strname + "_f02.maanim"
    if stage ==1:
        filename = strname + "_c02.maanim"
    if stage ==2:
        filename = strname + "_s02.maanim"
#    filename =strname+'_c02.maanim'
#    filename = '025_c02.maanim'
#    filename = '025_c02.maanim'
    filename = "Simplier/"+filename
    print(filename)
    with open(filename,encoding="utf-8") as f:
        #025_c02.maanim
        garbage = f.readline()
        nxtline = f.readline()
        for line in f:
            str2 = line

            str2 = str2.replace('\n','')
            str2 = str2.split(',')
 #           print(str2[0])  #Time/Rotate/Posx/Posy
            try:
                k = str2[1] #try to get error
            except:
                #This is real need to make
                times = int(str2[0])
                totaltime = totaltime+1
                continue
            if(times==0):
                continue
            times = times-1
            try:
                k = str2[1] #tryturerror
                k2 = int(str2[0])
    #            print("k2=  "+str(k2))
                try:
                    if(k2>maximum):
                        maximum = k2;
                except:
                    print("cp error")
            except:
                print("error")


#    print("maximum+1 = ")
#    print(maximum+1)
#    print(totaltime)
    return maximum
#            print(str2)
#        result = np.array_split(str2)
#        k = [i.split(',')[0] for i in str2]
#        print(k)
#        print("line:" + str2.split())
#f.close();

#This Case, 68 frame

'''
first, get linenum n, which means next n line would be same part.








ダミー = dummy 
'''
