class Min_Max:

    def Max_Algo(self, array):
        List = array
        print(List)
        temp = []
        if len(List) == 1:
            return temp
        for i in range(0, len(List) - 1,2):

            if(List[i]<List[i+1]):
                temp.append(List[i+1])
            elif(List[i]>List[i+1]):
                temp.append(List[i])
            i=i+1;
        self.Min_Algo(temp)
    def Min_Algo(self,array):
        List = array
        print(List)
        temp = []
        if len(List) == 1:
            return temp
        for i in range(0, len(List) - 1,2):
            if(List[i]<List[i+1]):
                temp.append(List[i])
            elif(List[i]>List[i+1]):
                temp.append(List[i+1])
            i=i+1;
        self.Max_Algo(temp)

def main():
    obj = Min_Max()
    list = [4,0,6,2,6,0,3,9,5,2,7,3,1,0,7,2,4,6,3,0]
    print(obj.Max_Algo(list))

main()
