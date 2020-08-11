class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sortedArray = self.mergeSort(prices)
        
        map = {}
        for x in range(0, len(prices)):
            map[prices[x]] = x
        
        if(map[sortedArray[0]] != len(sortedArray)-1):
               return sortedArray[-1] - sortedArray[0]
        
    def mergeSort(self,unsorted_list: List[int]) -> List[int]:
        if len(unsorted_list) <=1:
            return unsorted_list
        
        middle = len(unsorted_list)// 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]
        
        left_list = self.mergeSort(left_list)
        right_list = self.mergeSort(right_list)
        
        return self.mergeHalves(left_list, right_list)
    
    def mergeHalves(self,left_list: List[int] , right_list: List[int]) -> List[int]:
            res = []
            while len(left_list) > 0 and len(right_list) > 0 :
                if left_list[0] <= right_list[0]:
                    res.append(left_list[0])
                    left_list.pop(0)
                elif right_list[0] < left_list[0]:
                    res.append(right_list[0])
                    right_list.pop(0)
                
            if len(left_list) > 0:
                res = res+left_list
            
            elif len(right_list) > 0:
                res = res+right_list
                
            return res


print(Solution.maxProfit([7,1,5,3,6,4]))
                
                
                
        
    
        
        