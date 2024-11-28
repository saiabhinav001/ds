def TowersOfHanoi(n,source,destination,auxilary):
    if n==1:
        print("Move the disk 1 from source",source,"to destination",destination)
        return
    TowersOfHanoi(n-1,source,auxilary,destination)
    print("Move the disk",n,"from source",source,"to destination",destination)
    TowersOfHanoi(n-1,auxilary,destination,source)

n=3
TowersOfHanoi(n,"A","B","C")

