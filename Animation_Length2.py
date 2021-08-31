#f = open('044_f02.maanim', 'r',encoding="utf-8")
import numpy as np
#raw = f.readline() # skip first junk

#f = stage1
#c = stage2
#s = stage3
#e = enemy
def getAniLength(name,stage):
    maximum = 0;
    warnmsg = 0
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
        garbage2 = f.readline()
        totalblock = int(f.readline())
        for i in range(0,totalblock):
            str2 = f.readline()
            str2 = str2.split(',')
            loop = int(str2[2])
            if (warnmsg==0 and loop!=1):
                warnmsg = 1
                print(str2)
                print("This case exist loop more than 1, be aware if it's correct!")
            nxtline = int(f.readline())
            str4 = f.readline()
            str4 = str4.split(',')
            firstframe =  int(str4[0])
            for i in range(1,nxtline):
                str5 = f.readline() #Skip Central detail
            str5 = str(str5)
            str5 = str5.replace('\n','')
            str5 = str5.replace("'",'')
            str5 = str5.replace('[','')
            str5 = str5.replace(']','')
            str5 = str5.split(',')
#            print(str5)
            if nxtline!=1:
                finalframe = int(str5[0])
            else:
                finalframe = firstframe
            totalframe = finalframe-firstframe
#            print(totalframe)
            totalframe = totalframe * loop
#            print(str(firstframe)+"  "+str(finalframe)+"  "+str(totalframe))
            if totalframe > maximum:
                maximum = totalframe
#                print()
    return maximum

'''
first, get linenum n, which means next n line would be same part.








ダミー = dummy 
'''
