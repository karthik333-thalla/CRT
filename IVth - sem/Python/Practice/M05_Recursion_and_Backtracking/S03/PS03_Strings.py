#string: collection of characterss enclosed ' '," ", """ """
s = "python"
print(s[2])
print(s[1:])

print(s.captalize())
print(s)

#s[0] = 'p'
# s = s.replace("p")

# st =input()
# res =""
# stop =-1*(len(st)+1)
# for i in range(-1,stop,-1):

def Reverse_String(st):
    res1 =""
    for ch in st:
        res1 = ch+res1
    return res1
def is_palindrome(st):
    return st == Reverse_String(st)

print(is_palindrome("abc"))
print(is_palindrome("madam"))


def frequency_count(s):
    d ={}
    for ch in s:
        if ch not in d :
            d[ch]=1
        else:
            d[ch]+=1
    return d
print(frequency_count("abcabc")) #{'a':2,'b':2,'c:2}
def is_Anagarams(st1,st2):
    return frequency_count(st1) == frequency_count(st2)
print(is_Anagarams("space","paces"))#True
print(is_Anagarams("abc","abcabc"))#false
#leetcode questions28,43,165,389