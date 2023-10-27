# 1 2 4 8 16 32 64 128 256 ...
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #還沒寫完,不要送出...
        if n <= 0: return False
        while n > 1: #因為1是220不用再除了
            if n%2 !=0: #竟然榆樹不是0
                return False #失敗
            n = n // 2
            #經過樓上的檢查,都沒有出錯的話
        return True #就是成功