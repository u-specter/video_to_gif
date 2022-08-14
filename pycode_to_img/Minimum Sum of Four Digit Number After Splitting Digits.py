class Solution(object):
    def minimumSum(self, num):
        lst = [i for i in str(num)]
    
        a,  b, c, d = sorted(lst)
        return int(a+d)+int(b+c)
        