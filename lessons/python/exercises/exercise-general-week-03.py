import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 1
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# my_list[0]/=2
# len(my_list)
# ---------------------------------------------------------------
my_list = [2, 4, 6]

"""
با توجه به راهنمایی، لیست بالا و یک حلقه فور به شکلی محتویات
لیست را بروزرسانی کنید که به شکل زیر تبدیل شود

[4, 8, 12]
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 2
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# answer=input("Enter a name: ")
# in, not in, ==, !=
# ---------------------------------------------------------------
user_list = ["user1", "user2", "user3"]
pass_list = ["pass1", "pass2", "pass3"]  # Bad Practice - Just as an Example
"""
از کاربر "نام کاربری" و "رمز عبور" را دریافت کنید
سپس بررسی کنید آیا کاربری با این نام کاربری و رمز
عبور موجود هست یا خیر و برای آن یک پیغام مناسب چاپ
کنید

دقت کنید که هر نام کاربری متناظر با پسورد مقابلش
است
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 3
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# num_list[0]=2
# number//=1
# number+=1
# ---------------------------------------------------------------
num_list = [2.1, 4.6, 5.7, 8.9, 9.1, 0.3]
"""
حلقه ای بنویسید که لیست بالا را بصورت زیر تغییر دهد
[2.0, 4.0, 5.0, 8.0, 9.0, 0.0]

اگر بخواهید از لیست اول لیست زیر را بدست بیاورید چه؟
[3.0, 5.0, 6.0, 9.0, 10.0, 1.0]
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 4
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# bin(100)                      -> 0b1100100
# bin(10)                       -> 0b1010
# "1010".zfill(8)               -> 00001010
# "hello".replace("llo","n")    -> hen
# ---------------------------------------------------------------
my_list = [0, 50, 100, 150, 200, 250]

"""
با توجه به لیست بالا و راهنمایی بالا، لیست زیر را بدست آورید
['00000000', '00110010', '01100100', '10010110', '11001000', '11111010']
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 5
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# int("00110010",2)     -> 50
# ---------------------------------------------------------------
my_list = ["00000000", "00110010", "01100100", "10010110", "11001000", "11111010"]

"""
این مساله دقیقا برعکس مساله بالا است
با توجه به لیست بالا و راهنمایی بالا، لیست زیر را بدست آورید
[0, 50, 100, 150, 200, 250]
"""