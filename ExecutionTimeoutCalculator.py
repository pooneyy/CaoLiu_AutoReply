import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkFont
from datetime import datetime, timedelta

FONT_SIZE = 12
SPINBOX_WIDTH = 4

def calculate_timeout(event=None):
    try:
        account_count = int(account_count_entry.get())
        reply_limit = int(reply_limit_entry.get())
        time_interval_end = float(time_interval_end_entry.get())
        # polling_time = float(polling_time_entry.get())
        # 组合时间字符串
        start_time_str = f"{start_time_hour.get()}:{start_time_minute.get()}:{start_time_second.get()}"
        # 将时间字符串转换为 datetime 对象
        start_time = datetime.strptime(start_time_str, "%H:%M:%S")
        # start_time = datetime.strptime(start_time_entry.get() ,"%H:%M:%S")

        now = datetime.now()
        if now > start_time:
            start_time = start_time + timedelta(days=1)
        # 用于修正计算结果，当账户数 < 1，timeout = 0
        account_count_coefficient = 0 if account_count < 1 else 1
        # 5为登录重试次数，60为重试等待时间上限（秒）
        timeout = ( 5 * 60 * account_count + time_interval_end * (reply_limit + 1) ) * account_count_coefficient

        end_time = start_time + timedelta(seconds=timeout)

        result_label.config(text=f"执行超时时间：{int(timeout)} 秒\n计划启动时间：{start_time.time()}\n最迟结束时间：{end_time.time()}")

        if timeout > 86400:
            messagebox.showwarning("超时时间过长", "计算得到的超时时间已经超过了云函数可允许的最大超时时间（86400秒）。请重新调整输入参数。")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字参数。")

# 创建主窗口
root = tk.Tk()
root.title("云函数执行超时时间计算器")

# 创建自定义字体
font = tkFont.Font(family="SimSun", size=FONT_SIZE)

# 创建输入参数的标签和文本框

account_count_label = tk.Label(root, text="账户数量：", font=font)
account_count_label.grid(row=0, column=0, padx=5, pady=5)
account_count_entry = tk.Entry(root, font=font)
account_count_entry.grid(row=0, column=1, padx=5, pady=5)
account_count_entry.insert(0, "1")

reply_limit_label = tk.Label(root, text="回复次数限制：", font=font)
reply_limit_label.grid(row=1, column=0, padx=5, pady=5)
reply_limit_entry = tk.Entry(root, font=font)
reply_limit_entry.grid(row=1, column=1, padx=5, pady=5)
reply_limit_entry.insert(0, "10")

time_interval_end_label = tk.Label(root, text="两次回复的时间间隔最大值（秒）：", font=font)
time_interval_end_label.grid(row=2, column=0, padx=5, pady=5)
time_interval_end_entry = tk.Entry(root, font=font)
time_interval_end_entry.grid(row=2, column=1, padx=5, pady=5)
time_interval_end_entry.focus_set()  # 焦点位于输入框

# polling_time_label = tk.Label(root, text="循环间隔（秒）：", font=font)
# polling_time_label.grid(row=3, column=0, padx=5, pady=5)
# polling_time_entry = tk.Entry(root, font=font)
# polling_time_entry.grid(row=3, column=1, padx=5, pady=5)
# polling_time_entry.insert(0, "5")

start_time_label = tk.Label(root, text="计划启动时间（时:分:秒）：", font=font)
start_time_label.grid(row=4, column=0, padx=5, pady=5)

start_time_frame = ttk.Frame(root)
start_time_frame.grid(row=4, column=1, padx=5, pady=5)
start_time_hour = ttk.Spinbox(start_time_frame, from_=0, to=23, width=SPINBOX_WIDTH, font=font)
start_time_minute = ttk.Spinbox(start_time_frame, from_=0, to=59, width=SPINBOX_WIDTH, font=font)
start_time_second = ttk.Spinbox(start_time_frame, from_=0, to=59, width=SPINBOX_WIDTH, font=font)
start_time_hour.set('08')
start_time_minute.set('30')
start_time_second.set('00')
start_time_hour.grid(row=0, column=0, padx=5, pady=5)
start_time_minute.grid(row=0, column=1, padx=5, pady=5)
start_time_second.grid(row=0, column=2, padx=5, pady=5)

# start_time_entry = tk.Entry(root, font=font)
# start_time_entry.grid(row=3, column=1, padx=5, pady=5)
# start_time_entry.insert(0, "08:30:00")

# 创建计算按钮
calculate_button = tk.Button(root, text="计算超时时间", command=calculate_timeout, font=font)
calculate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# 创建结果展示标签
result_label = tk.Label(root, heigh=3, text="", font=font)
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# 绑定回车键与计算事件
root.bind("<Return>", calculate_timeout)

# 启动主循环
root.mainloop()