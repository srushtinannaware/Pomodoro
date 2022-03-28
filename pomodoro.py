from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
win_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(win_timer)
    canvas.itemconfig(timerText,text="00:00")
    timer.config(text="Timer",fg=GREEN)
    checkmark.config(text="")
    start.config(state="normal")

    global REPS
    REPS= 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 8 ==0:
        countdown(long_break)
        timer.config(text="Break",fg=RED)
    elif REPS % 2 ==0:
        countdown(short_break)
        timer.config(text="Break",fg=PINK)
    else:
        countdown(work_sec)
        timer.config(text="Work",fg=GREEN)
        start.config(state="disabled")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timerText, text=f"{count_min}:{count_sec}")
    if count > 0:
        global win_timer
        win_timer = window.after(1000, countdown, count - 1)
    else:
        startTimer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# width and height in pixels
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0,command=startTimer)
start.grid(column=0, row=3)

reset = Button(text="Reset", highlightthickness=0,command = reset_timer)
reset.grid(column=3, row=3)

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=4)



window.mainloop()
