import tkinter as tk
import random
import threading
import time


class CloseWindow:
    def __init__(self, window, timer):
        self.window = window
        self.timer = timer

    def close(self):
        self.window.destroy()

    #        print("窗口关闭了")

    def start(self):
        self.window.after(self.timer, self.close)


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('Happy Everyday')  # 弹窗的名字，都可以修改的
    window.geometry("360x50" + "+" + str(a) + "+" + str(b))  # 弹窗大小，不建议修改
    txt = ["小洋宝贝，今天也要快快乐乐哟！",
           "大洋宝，今天的你是世界上最美的",
           "小洋洋，老公厉害不厉害，爱你哟"]
    # color = ["red", "yellow", "blue", "green", "pink"] #背景颜色随机
    color = ["#CC0000", "#FF0000", "#FF3333", "#FF0066"]
    tk.Label(window,
             text=random.choice(txt),  # 标签的文字，随便改
             # bg='#CC0000',  # 背景颜色
             bg=random.choice(color),
             font=('楷体', 18),  # 字体和字体大小
             width=35, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    CloseWindow(window, 2000).start()  # 每个窗口延时关闭时间ms
    window.mainloop()


def main():
    threads = []
    n = 5  # 需要的弹框数量，别太多了，电脑不好会死机
    for i in range(n):
        t = threading.Thread(target=dow)
        threads.append(t)
        time.sleep(0.2)
        threads[i].start()


if __name__ == '__main__':
    main()
