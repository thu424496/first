## select sort
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def swap(arr,i,j):
    arr[i] = arr[i]^arr[j]
    arr[j] = arr[i]^arr[j]
    arr[i] = arr[i]^arr[j]


## sort
def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 

for i in range(n): 
    print ("%d" %arr[i]),


# 堆

def heapify(arr,index,head_index):
    left = index*2+1
    while left<head_index:
        # 从左右子节点选出最大者
        largest =left+1 if arr[left]<arr[left+1] && left+1<head_index else left
        # 将最大子节点和父节点比较
        largest = index if arr[largest]<arr[index] else largest
        if largest==index:
            break
        swap(arr,index,largest)
        index = largest
        left = index*2+1
