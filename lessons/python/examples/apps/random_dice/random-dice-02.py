import random
from tkinter import *

window = Tk()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# برنامه زیر یک عدد تصادفی بین 1 تا 6 را بر روی یک برچسب نمایش
# میدهد
# آیا میتوانید برنامه را به شکلی تغییر دهید که دو عدد تصادفی بر
# روی برچسب نمایش داده شود؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.geometry("250x110")
window.title("یک عدد تصادفی")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers = [1, 2, 3, 4, 5, 6]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# زمانیکه بر روی دکمه کلیک میشود این تابع صدا زده میشود
def choose_a_random_number():
    number = random.choice(numbers)
    label.config(text=str(number))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# دکمه ای ساختیم که بتوانیم از آن برای انتخاب یک عدد تصادفی
# استفاده کنیم
button = Button()
button.config(text="کلیک کنید")
button.config(command=choose_a_random_number)
button.place(x=10, y=15, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک برچسب ساختیم که از آن برای نمایش یک عدد استفاده کنیم
label = Label()
label.config(font=("", 25))
label.config(text="هیچی")
label.place(x=10, y=55, width=230)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
