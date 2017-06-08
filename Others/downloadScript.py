from urllib import request

with open('imageLinks') as openfileobject:
    count = 0;
    for line in openfileobject:
        if line!="" or line!="\n" :
            print(line)
        f = open(str(count)+'.jpg', 'wb')
        f.write(request.urlopen("http://www.gunnerkrigg.com/comics/00000001.jpg").read())
        f.close()
        count+=1

