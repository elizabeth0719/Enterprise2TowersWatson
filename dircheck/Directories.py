import os, sys, heapq, psutil, platform
#Your stuff is borken
trace  = lambda *pargs, **kargs: None    # or print or report
error  = lambda *pargs, **kargs: print(*pargs, file=sys.stderr, **kargs)
prompt = lambda text: input(text + ' ')
disks = []
partCount = 0


def treesize(root):
    alldirs = []

    try:
        allhere = os.listdir(root)
    except:
        allhere = []
        error('Error accessing dir (skipped):', root)
    
   
    for name in allhere:
        totalsize = 0
        for path, dirs, files in os.walk(root + name):
            for f in files:
                filename = os.path.join(path, f)
                try:
                    totalsize += os.path.getsize(filename)
                except: 
                    continue
        alldirs.append((root + " " + name, sizeof_fmt(totalsize)))
        
    alldirs.sort(key=lambda tup: tup[1], reverse=True) 
    return alldirs

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

if __name__ == '__main__':

    tempdic = {}
    for part in psutil.disk_partitions(all=False):
        if platform.system == 'Windows':
            disks.append(part.device)
        else: 
            disks.append(part.mountpoint) 

    dictArrs = []

    for disk in disks:
        dictArrs.append(treesize(disk))   
    
    dicts = {}
    for arrs in dictArrs:
        counter = 0
        dic = {}
        for val in arrs:
            if(counter==5):
                continue
            else:
                dic[val[0]] = val[1]
                counter+=1
        dicts[disks[dictArrs.index(arrs)]] = dic

    print(dicts)
    # counter = 0
    # for dir in alldirs:
    #     if(counter==5):
    #         continue
    #     else:
    #         tempdic[dir[0]] = sizeof_fmt(dir[1])
    #         counter+=1 

    # print(tempdic)
     