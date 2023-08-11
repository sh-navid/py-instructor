import random
from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این برنامه مشابه برنامه قبلی است با این تفاوت که نام تصادفی
# در یک "برچسب" نمایش داده میشود
# چطور میتوانیم کاری کنیم که "کاغذ" را با تعداد
# دفعات بیشتری ببینیم؟
# یعنی میخواهیم کاری کنیم احتمال اینکه عبارت "کاغذ" را ببینیم
# افزایش پیدا کند

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
choices = ["سنگ", "کاغذ", "قیچی"]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label = Label()
label.config(text=random.choice(choices))
label.pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()