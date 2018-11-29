#coding:UTF-8

#身分證認證 確認一組身分證號碼是否合法?? 
#　　　(1)英文代號以下表轉換成數字 
#　　　A=10 台北市　　　J=18 新竹縣　　　S=26 高雄縣 
#　　　B=11 台中市　　　K=19 苗栗縣　　　T=27 屏東縣 
#　　　C=12 基隆市　　　L=20 台中縣　　　U=28 花蓮縣 
#　　　D=13 台南市　　　M=21 南投縣　　　V=29 台東縣 
#　　　E=14 高雄市　　　N=22 彰化縣　　* W=32 金門縣 
#　　　F=15 台北縣　　* O=35 新竹市　　　X=30 澎湖縣 
#　　　G=16 宜蘭縣　　　P=23 雲林縣　　　Y=31 陽明山 
#　　　H=17 桃園縣　　　Q=24 嘉義縣　　* Z=33 連江縣 
#　　* I=34 嘉義市　　　R=25 台南縣 
#　　　(2)英文轉成的數字, 個位數乘９再加上十位數 
#　　　(3)各數字從右到左依次乘１、２、３、４．．．．８ 
#　　　(4)求出(2),(3)之和 
#　　　(5)求出(4)除10後之餘數,用10減該餘數,結果就是檢查碼,
#         若餘數為0 檢查碼就是0 為正確

# 身分證字號規則： 
# 字母(ABCDEFGHJKLMNPQRSTUVXYWZIO)對應一組數(10~35)， 
# 令其十位數為X1，個位數為X2；( 如Ａ：X1=1 , X2=0 )；D表示2~9數字 
# Y = X1 + 9*X2 + 8*D1 + 7*D2 + 6*D3 + 5*D4 + 4*D5 + 3*D6 + 2*D7+ 1*D8 + D9 
# 如Y能被10整除，則表示該身分證號碼為正確，否則為錯誤。

print("====  python 程式設計50題測試範例-14 =====")
print(" 身分證認證 確認一組身分證號碼是否合法?? ")

while True:
     sP = input('請輸入一組身分證號碼 ：')
     try:
        sP = repr(sP)   #repr() 函式可以轉換任何的值成為一個字串
        # print (len(sP))
     except ValueError:
       print ('這是不合法的輸入.  請再輸入一次...')
       continue
        
     if len(sP) ==12 :   #ID 10位數 + 2個 '號  共12個
       break


sP=(sP[1:len(sP)-1])   #[ : ] 截取字符串中的一部分
print("=====================================")
print("輸入的身分證號碼是",sP)
Sum=0

s=list(sP)   #string to list

if s[0]=='A':
   Sum=Sum+1
elif s[0]=='B':
   Sum=Sum+10
elif s[0]=='C':
   Sum=Sum+19
elif s[0]=='D':
   Sum=Sum+28
elif s[0]=='E':
   Sum=Sum+37
elif s[0]=='F':
   Sum=Sum+46
elif s[0]=='G':
   Sum=Sum+55
elif s[0]=='H':
   Sum=Sum+64
elif s[0]=='I':
   Sum=Sum+39
elif s[0]=='J':
   Sum=Sum+73
elif s[0]=='K':
   Sum=Sum+82
elif s[0]=='L':
   Sum=Sum+2
elif s[0]=='M':
   Sum=Sum+11
elif s[0]=='N':
   Sum=Sum+20
elif s[0]=='O':
   Sum=Sum+48
elif s[0]=='P':
   Sum=Sum+29
elif s[0]=='Q':
   Sum=Sum+38
elif s[0]=='R':
   Sum=Sum+47
elif s[0]=='S':
   Sum=Sum+56
elif s[0]=='T':
   Sum=Sum+65
elif s[0]=='U':
   Sum=Sum+74
elif s[0]=='V':
   Sum=Sum+83
elif s[0]=='W':
   Sum=Sum+21
elif s[0]=='X':
   Sum=Sum+3
elif s[0]=='Y':
   Sum=Sum+12
elif s[0]=='Z':
   Sum=Sum+30  
else:
   Sum=Sum+0


Sum1=8*int(s[1])+7*int(s[2])+6*int(s[3])+5*int(s[4])+4*int(s[5])+3*int(s[6])+2*int(s[7])+1*int(s[8])+int(s[9])
Sum=Sum+Sum1
Sum=Sum%10

if Sum==0 :
   print("輸入的身分證號碼",sP,"是合法的")
else :

   print("輸入的身分證號碼",sP,"是不合法的")  
