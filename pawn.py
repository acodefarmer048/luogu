# luogu
# practice
def pawn(x,y,xlen,ylen):
    global maps,result
    if x==xlen and y==ylen:
        result+=1
        return 1
    else:
        one,two=0,0
        if x<xlen:
            if maps[x+1][y]==-1:
                one=pawn(x+1,y,xlen,ylen)
            elif maps[x+1][y]>=1:
                result+=maps[x+1][y]
                one=maps[x+1][y]
            else:
                one = maps[x + 1][y]
        if y<ylen:
            if maps[x][y+1]==-1:
                two=pawn(x,y+1,xlen,ylen)
            elif maps[x][y+1]>=1:
                result+=maps[x][y+1]
                two=maps[x][y+1]
            else:
                two = maps[x][y + 1]
        maps[x][y]=one+two
        return maps[x][y]
def main():
    global maps,result
    xlen,ylen,m,n=map(int,input().split())
    maps=[[-1 for i in range(ylen+1)] for j in range(xlen+1)]
    maps[m][n]=0
    leap=[[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    for i in range(8):
        refer_x=m+leap[i][0]
        refer_y=n+leap[i][1]
        if refer_x<=xlen and refer_x>=0 and refer_y<=ylen and refer_y>=0:
            maps[refer_x][refer_y]=0
    maps[xlen][ylen]=1
    result=0
    pawn(0,0,xlen,ylen)
    print(result)
main()
