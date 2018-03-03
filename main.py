
class Problem:
    def __init__(self):
        self.result=[0,0,0,0,0,0,0,0,0,0]
        self.test_arr=[0,0,0,0,0,0,0,0,0,0]
        self.error_flag=0
        pass

    def G(self,index):
        return self.result[index]
    
    def S(self,index,val):
        # self.result[index]=val
        self.test_arr[index]=val

    def solve1(self):
        self.S(0,1)
    
    def min_num(self):
        the_min_num=9
        for i in range(0,4):
            test=self.result.count(i)
            if(the_min_num>test):
                the_min_num=test
        # print(the_min_num)
        return the_min_num        
    
    def min_num_index(self):
        the_min_num=9
        index=-1
        for i in range(0,4):
            test=self.result.count(i)
            if(the_min_num>test):
                the_min_num=test
                index=i
        return index    
    
    def max_num(self):
        the_max_num=-1
        for i in range(0,4):
            test=self.result.count(i)
            if(the_max_num<test):
                the_max_num=test
        return the_max_num

    def three_equal(self,val1,val2,val3):
        if(val1==val2):
            if(val1==val3):
                return True
        return False

    def three_not_completely_equal(self,val0,val1,val2,val3):
        if(val0==val1):
            return False
        if(val0==val2):
            return False
        if(val0==val3):
            return False
        return True


    def solve2(self):
        if(self.G(4)==0):
            self.S(1,2)
        elif(self.G(4)==1):
            self.S(1,3)
        elif(self.G(4)==2):
            self.S(1,0)
        elif(self.G(4)==3):
            self.S(1,1)
        else:
            self.error_flag=1

    def solve3(self):
        if(self.three_not_completely_equal(self.G(3),self.G(2),self.G(5),self.G(1))):
            self.S(2,3)
        elif(self.three_not_completely_equal(self.G(1),self.G(2),self.G(5),self.G(3))):
            self.S(2,2)
        elif(self.three_not_completely_equal(self.G(5),self.G(2),self.G(1),self.G(3))):
            self.S(2,1)
        elif(self.three_not_completely_equal(self.G(2),self.G(5),self.G(1),self.G(3))):
            self.S(2,0)
        else:
            self.error_flag=1

    def solve4(self):
        if(self.G(0)==self.G(4)):
            self.S(3,0)
        elif(self.G(1)==self.G(6)):
            self.S(3,1)
        elif(self.G(0)==self.G(8)):
            self.S(3,2)
        elif(self.G(5)==self.G(9)):
            self.S(3,3)
        else:
            self.error_flag=1
            

    def solve5(self):        
        if(self.G(4)==self.G(7)):
            self.S(4,0)
        elif(self.G(4)==self.G(3)):
            self.S(4,1)
        elif(self.G(4)==self.G(8)):
            self.S(4,2)
        elif(self.G(4)==self.G(6)):
            self.S(4,3)
        else:
            self.error_flag=1

    def solve6(self):        
        if(self.three_equal(self.G(1),self.G(3),self.G(7))):
            self.S(5,0)
        elif(self.three_equal(self.G(0),self.G(5),self.G(7))):
            self.S(5,1)
        elif(self.three_equal(self.G(2),self.G(9),self.G(7))):
            self.S(5,2)
        elif(self.three_equal(self.G(4),self.G(8),self.G(7))):
            self.S(5,3)
        else:
            self.error_flag=1

    def solve7(self):
        a= self.min_num_index()
        if(a==0):
            self.S(6,2)
        elif(a==1):
            self.S(6,1)
        elif(a==2):
            self.S(6,0)
        elif(a==3):
            self.S(6,3)
        else:
            self.error_flag=1

    def solve8(self):
        if( abs(self.G(0)-self.G(6))>=2):
            self.S(7,0)
        elif(abs(self.G(0)-self.G(4))>=2):
            self.S(7,1)
        elif(abs(self.G(0)-self.G(1))>=2):
            self.S(7,2)
        elif(abs(self.G(0)-self.G(9))>=2):
            self.S(7,3)
        else:
            self.error_flag=1

    def solve9(self):
        a=(self.G(0)==self.G(5))
        for i in [5,9,1,8]:
            b=(self.G(4)==self.G(i))
            if(a!=b):
                if(i==5):
                    self.S(8,0)
                elif(i==9):
                    self.S(8,1)
                elif(i==1):
                    self.S(8,2)
                elif(i==8):
                    self.S(8,3)
                else:
                    self.error_flag=1

    def solve10(self):
        a=self.max_num()
        b=self.min_num()
        if(a-b==1):
            self.S(9,3)
        elif(a-b==2):
            self.S(9,1)
        elif(a-b==3):
            self.S(9,0)
        elif(a-b==4):
            self.S(9,2)
        else:
            self.error_flag=1

    def compare(self):
        for i in range(0,10):
            if(self.result[i]!=self.test_arr[i]):
                return False
        return True

    def solve(self):
        self.test_arr=self.result[:]
        self.error_flag=0
        self.solve1()
        self.solve2()
        self.solve3()
        self.solve4()
        self.solve5()
        self.solve6()
        self.solve7()
        self.solve8()
        self.solve9()
        self.solve10()
        return self.error_flag

    def show(self,arr= None ):
        if(arr==None):
            arr=self.result
        print("[" , end='')
        for i in range(len(arr)):
            if(arr[i]==0):
                print("A",end='')
            elif(arr[i]==1):
                print("B",end='')
            elif(arr[i]==2):
                print("C",end='')
            elif(arr[i]==3):
                print("D",end='')
            print(", ",end=' ')
        print("]")

    def test(self):
        test_result=[0,0,0,0,0,0,0,0,0,0]
        i=0
        j=0
        while test_result.count(3)!=10 :
            test_result[0]+=1
            for i in range(0,10):
                if(test_result[i]==4):
                    test_result[i]=0
                    test_result[i+1]+=1
            self.result=test_result[:]
            flag=self.solve()
            if(flag):
                continue
            if(self.compare()):
                self.show()
                # break
                    
    def test_one(self,arr):
        self.result=arr
        self.show(self.result)
        test=self.solve()
        # if(test==1):
        self.show(self.test_arr)
            
if __name__ == '__main__':
    problem =Problem()
    # problem.test_one([1,2,0,2,0,2,3,0,1,0])
    problem.test()