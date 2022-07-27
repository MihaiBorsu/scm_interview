!/usr/bin/env python3

cuvant = input('Cuvant: ')
cuvandNou=""

for litera in cuvant :
    cuvandNou+=litera
    if litera in "aeiou":
        cuvandNou+="p"+litera

print("Cuvantul in pasareasca:", cuvandNou)




# int decToBinary(int n)
# {
#     int binaryNum[32];
#     int i = 0;
#     while (n > 0) {
#         binaryNum[i] = n % 2;
#         n = n / 2;
#         i++;
#     }
#     int sum = 0;
#     for (int j = i - 1; j >= 0; j--) {
#     sum = sum + binaryNum[j];
#     }


#     return sum;
# }


# def decToBinary(n):
#     binaryNum = [0]*33
#     i = 0
#     while n > 0 :
#         binaryNum[i] = n % 2
#         n = n // 2
#         i += 1
#     sum = 0
#     for j in binaryNum:
#         sum += j
#     return sum



# def solution(X, Y):
#     Suma = 0
#     for n in range(X,Y+1):
#         Suma += decToBinary(n)
#     print(Suma)

# solution(11,50)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")




# vector<int> solution(vector<int> &givenArray, int sum)
# {​​​​​
#     int left, right;
#     int arraySize = givenArray.size();

#     sort(givenArray.begin(),givenArray.end());

#     for (auto i = 0; i < arraySize - 2; i++) {​​​​​
#         left = i + 1;
#         right = arraySize - 1;
#         while (left < right) {​​​​​
#             if (givenArray[i] + givenArray[left] + givenArray[right] == sum) {​​​​​
#                 cout << givenArray[i] <<" "<< givenArray[left] << " " << givenArray[right] << "\n";
#                 auto backupMultiply = givenArray[i] * givenArray[left] * givenArray[right];
#                 cout << "Backup multiply:" << backupMultiply;
#                 return givenArray;
#             }​​​​​
#             else if (givenArray[i] + givenArray[left] + givenArray[right] < sum)
#                 left++;
#             else
#                 right--;
#         }​​​​​
#     }​​​​​
#     return {​​​​​}​​​​​;
# }​​​​​



# def solution(givenArray, sum):
#     left = 0
#     right = 0
#     arraySize = len(givenArray)
#     # print("givenArray",givenArray)
#     givenArray.sort()
#     # print("givenArray",givenArray)
#     for i in range(arraySize-1):
#         print("i",i)
#         left = i+1
#         right = arraySize - 1
#         while left < right :
#             if givenArray[i] + givenArray[left] + givenArray[right] == sum :
#                 print(givenArray[i], givenArray[left], givenArray[right])
#                 return [givenArray[i], givenArray[left], givenArray[right]]
#                 # backupMultiply = givenArray[i]*givenArray[left]*givenArray[right]
#                 # return backupMultiply
#             elif givenArray[i] + givenArray[left] + givenArray[right] < sum :
#                 left += 1
#             else :
#                 right -= 1




# # solution( [5, 2, 4, 1, 8, 16, 6, 10, 7, 13]  , 20 )
# solution( [20,30,14,15]  , 20 )