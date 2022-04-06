# Two pointers
#Time Complexity: O(NlogN)
#Space Complexity: O(N) 
class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        left = 0
        right = len(people)-1

        boats_number = 0

        while(left<=left):
            if(left==right):
                boats_number+=1
                break
            if(people[left]+people[right]<=limit):
                left+=1

            right-=1
            boats_number+=1
        return boats_number

s = Solution()
print(s.numRescueBoats([1, 2], 3))
print(s.numRescueBoats([3, 2, 2, 1], 3))