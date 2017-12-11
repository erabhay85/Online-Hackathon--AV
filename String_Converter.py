vStr = '144.2151.2127.8130.8110.3'

def fConString(Str):
    vData = vStr.split('.')
    vActData = []
    vLen = len(vData)
    x=0
    while x < vLen-1:
       if(x == 0):
          vActData.append(vData[x] + '.' + vData[x+1][0])
       else:
          vActData.append(vData[x][1:] + '.' + vData[x+1][0])
       x+=1
    return vActData

vData1 = fConString(vStr)

print vData1
