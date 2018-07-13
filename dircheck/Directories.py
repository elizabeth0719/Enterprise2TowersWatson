import os, sys, heapq
#Your stuff is borken
trace  = lambda *pargs, **kargs: None    # or print or report
error  = lambda *pargs, **kargs: print(*pargs, file=sys.stderr, **kargs)
prompt = lambda text: input(text + ' ')
toproot = '/'

def treesize(root, alldirs, allfiles, counts):
    

    sizehere = 0
    try:
        allhere = os.listdir(toproot)
    except:
        allhere = []
        error('Error accessing dir (skipped):', root)

    for name in allhere:
        path = os.path.join(root, name)

        if os.path.islink(path):
           trace('skipping link:', path) 

        elif os.path.isfile(path):
            trace('file:', path)
            counts[1] += 1
            filesize = os.path.getsize(path)
            allfiles.append((path, filesize))
            sizehere += filesize
            
        elif os.path.isdir(path):
            trace('subdir', path)
            counts[0] += 1
            subsize = treesize(path, alldirs, allfiles, counts)
            sizehere += subsize

        else:
            # error('Unknown file type (skipped):', path)   # fifo, etc.
            continue

        alldirs.append((name, sizehere))
    return sizehere

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

if __name__ == '__main__':

    # collect sizes
    alldirs, allfiles = [], []
    counts = [1, 0]
    tempdic = {}
   
    totsize = treesize(toproot, alldirs, allfiles, counts)
    alldirs.sort(key=lambda tup: tup[1], reverse=True)    
    counter = 0
   
    for dir in alldirs:
        if(counter==5):
            continue
        else:
            tempdic[dir[0]] = sizeof_fmt(dir[1])
            counter+=1 

    print(tempdic)
