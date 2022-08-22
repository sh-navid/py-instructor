import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 1
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# "---".join(["A", "BB", "CC"]) -> A---BB---CC
# upper(), lower(), swapcase()
# ---------------------------------------------------------------

my_list = ["Hello", "My", "World"]

"""
با توجه به راهنمایی بالا چطور در خروجی این عبارت را چاپ کنیم
HELLO@MY@WORLD
hello$my$world
hELLO~mY~wORLD
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 2
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# replace()
# ۰۱۲۳۴۵۶۷۸۹
# ---------------------------------------------------------------

s = "4433۶۶"

"""
تصور کنید کاربر برای شما اعدادی را وارد کرده است اما اشتباها
بعضی از اعداد بصورت فارسی و برخی نیز بصورت انگلیسی وارد شده
اند. چطور همه این اعداد را به فارسی یا به انگلیسی تبدیل کنیم؟
443366
یا
۴۴۳۳۶۶
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 3
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# random(), choice(), shuffle()
# ---------------------------------------------------------------

coin = ["Back","Front"]

"""
فرض کنیم یک سکه داریم. این سکه را اگر پرتاب کنیم به رو یا پشت
قرار میگیرد. این دو مقدار در
coin
ذخیره شده است. چطور با پایتون کدی بنویسیم که بصورت تصادفی یکی
از این دو مقدار را انتخاب کند؟
چطور کاری کنیم که احتمال اینکه رو بیاید بیشتر از احتمال پشت
باشد؟
"""


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# مساله 4
# ---------------------------------------------------------------
# راهنمایی
# ---------------------------------------------------------------
# splitlines(), split(":")
# ---------------------------------------------------------------

s = """Hi:Hello
Bye:GoodBye
"""

"""
متن بالا را خط به خط جدا کنید
در هر خط کلمات را نیز از هم جدا کرده و نمایش دهید

برای مثال
['Hi', 'Hello']
['Bye', 'GoodBye']
"""