from tkinter import *

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این برنامه یک ابزار نقاشی در ساده ترین حالت ممکن است
# آیا میتوانید این برنامه را اجرا و تست کنید؟
# آیا میتوانید سایز خطی که در برنامه رسم میشود را تغییر دهید؟
# آیا میتوانید رنگ خطی که در برنامه رسم میشود را تغییر دهید؟
# چه تغییر دیگری میتوانید در این برنامه ایجاد کنید؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این دو متغیر مکان قبلی موس را برای ما نگه میدارند، به این شکل
# زمانی که موس حرکت میکند میدانیم از کدام نقطه قبلی باید به
# مکان فعلی موس یک خط ریسم کنیم
x, y = None, None

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# زمانی که دکمه سمت چپی موس فشرده میشود این تابع صدا زده میشود
def mouse_click(e):
    global x, y
    x, y = e.x, e.y

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# زمانیکه موس حرکت میکند این تابع صدا زده میشود
def mouse_move(e):
    global x, y
    boom.create_line(x, y, e.x, e.y, width=5, fill="red")
    x, y = e.x, e.y


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window = Tk()
Label(window, text="بر روی صفحه نقاشی کنید").pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# کنوس کامپوننتی است که به ما اجازه میدهد بر روی آن رسم کنیم
boom = Canvas(width=500, height=500)
boom.pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# این دو ایونت (رویداد) هستند
# زمانی که موس کلیک میکند یا حرکت میکند، توابع متناظر با این
# دو رویداد صدا زده میشوند
window.bind("<ButtonPress-1>", mouse_click)
window.bind("<B1-Motion>", mouse_move)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
