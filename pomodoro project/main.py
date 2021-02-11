from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
ROW = 3
timer = None


# ---------------------------- TIMER Reset ------------------------------- #
def timer_reset():
    global reps
    reps = 0
    label.config(text="TIMER", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down_time(long_break)
        label.config(text="BREAK", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down_time(short_break)
        label.config(text="BREAK", fg=PINK, bg=YELLOW)
    else:
        count_down_time(work_sec)
        label.config(text="WORK", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down_time(seconds):
    minutes = math.floor(seconds / 60)
    secs = seconds % 60
    if secs < 10:
        secs = f"0{secs}"
    if secs == 0:
        secs = "00"
    canvas.itemconfig(timer_text, text=f"{minutes}:{secs}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down_time, seconds - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=200, pady=50, bg=YELLOW)

label = Label(window, text="TIMER")
label.config(font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

start = Button(text="Start", command=start_timer)
start.config(font=(FONT_NAME, 10, "bold"))
start.grid(row=2, column=0)
Reset = Button(text="Reset", command=timer_reset)
Reset.config(font=(FONT_NAME, 10, "bold"))
Reset.grid(row=2, column=2)
window.mainloop()
