def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: #주어진 범위를 벗어날 때 즉시 종료
        return False
    if graph[x][y]==0: #음료수 칸이 비어 있는 경우에만
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


n,m=map(int,input().split()) #input 값을 공백을 기준으로 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input()))) # input이 n번 발생하니까 n 만큼 반복하면서 각각 행에 input값 집어넣기

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)


