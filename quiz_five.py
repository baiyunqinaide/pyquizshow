#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6] 

#运行过程:for i in a,每个i是【1,2】,【3,4】,【5,6】,for jin i,每个j就是1，2,3,4,5,6,合并后就是结果

a=[[1,2],[3,4],[5,6]] 
X=[j for i in a for j in i] 
print(x)
