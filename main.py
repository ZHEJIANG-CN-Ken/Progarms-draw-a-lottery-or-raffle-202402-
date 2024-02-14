# -*- coding:utf-8 -*-

"""
*版权声明：

本程序由Gao Chenkai全部自主独立完成制作，···已经开源···，如有转载或抄袭，请务必注明出处，否则将追究相应的法律责任。
版权所有 © 2024 Gao Chenkai <https://github.com/kaiccc>
"""

import tkinter as tk
from tqdm.tk import tqdm, trange
from tkinter import messagebox
from time import sleep
from time import ctime as tt
from random import random, randint
from PIL import Image, ImageTk
from tkinter import ttk
import ctypes
import sv_ttk
import os
import logging
import sys

logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    datefmt="%d-%M-%Y %H:%M:%S",
    level=logging.DEBUG,
    encoding="UTF-8"
        )


def log(level, message):
    if level == "debug":
        logging.debug(message)
    elif level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "critical":
        logging.critical(message)
    else:
        messagebox.showerror("错误", "日志等级错误")

        raise ValueError("日志等级错误")


log("info", "程序开始运行")
log("info", "")
log("info", "")
log("info", "")

# 设置tkinter的缩放因子
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)

font_20 = ("微软雅黑", 20)
font_12 = ("微软雅黑", 12)
font_15 = ("微软雅黑", 15)


class Win(object):
    def __init__(self):
        self.show_log = None
        log("info", "程序开始运行 | 初始化开始")
        print(f"{tt()} | info | 程序开始运行 | 初始化开始")
        print()

        self.background_image = None
        self.slow = None
        self.num_quantity = None
        self.num_quantity_outside = None
        self.show = None
        self.i = None
        self.time = None
        self.win = None
        self.tk_num_list = None
        self.tk_num_ok = None
        self.tk_num_entry = None
        self.tk_num = None

        log("info", "变量初始化完成 | 接下来开始Tk窗口初始化")
        print(f"{tt()} | info | 变量初始化完成 | 接下来开始Tk窗口初始化")

        self.root = tk.Tk()
        self.root.title("智能抽奖 v0.0.1")
        self.root.geometry("500x200")

        # 调用api获得当前的缩放因子
        self.scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(1)

        # 设置缩放因子
        self.root.tk.call('tk', 'scaling', self.scaleFactor / 75)

        # sv_ttk.set_theme("dark")

        self.root.tk.call("source", "azure.tcl")
        self.root.tk.call("set_theme", "dark")

        log("info", "Tk窗口初始化完成 | 接下来开始界面布局")
        print(f"{tt()} | info | Tk窗口初始化完成 | 接下来开始界面布局")
        print()

        self.tk_way = tk.Frame(self.root)

        ttk.Label(self.tk_way, font=font_20).grid(row=1, column=1)

        ttk.Label(self.tk_way, text="请选择抽奖方式：", font=font_12).grid(row=2, column=1, padx=15, pady=15)

        ttk.Button(self.tk_way, text="号码抽奖", command=self.num_input, width=20).grid(row=3, column=1, padx=15, pady=15)
        ttk.Button(self.tk_way, text="奖品抽奖", command=self.prize_input, width=20).grid(row=3, column=2, padx=15, pady=15)

        self.tk_way.pack()

        print(f"{tt()} | info | 初始窗口已创建")
        print()

        log("info", "初始窗口已创建")

    def num_input(self):
        self.root.geometry("1000x150")

        log("info", "新窗口尺寸已适配")
        print(f"{tt()} | Info | 新窗口尺寸已适配")
        print()

        log("info", "用户选择了号码抽奖")
        print(f"{tt()} | Info |用户选择了号码抽奖")
        print()

        self.tk_way.destroy()
        self.tk_num = tk.Frame(self.root)

        self.num_quantity = tk.StringVar()

        ttk.Label(self.tk_num, text="请输入号码数量：", font=font_20).grid(row=1, column=1, padx=15, pady=50)

        self.tk_num_entry = ttk.Entry(self.tk_num, font=font_20, width=30, textvariable=self.num_quantity)
        self.tk_num_entry.grid(row=1, column=2, padx=15, pady=50)

        ttk.Button(self.tk_num, text="确定", command=self.num_ok).grid(row=1, column=3, padx=15, pady=50)

        self.tk_num.pack()

    def num_ok(self):
        self.root.attributes('-fullscreen', True)

        log("info", "号码抽奖开始")
        print(f"{tt()} | Info |号码抽奖开始")
        print()

        self.tk_num.destroy()
        self.tk_num_ok = tk.Frame(self.root)

        self.show = ttk.Label(self.tk_num_ok, text="", font=("039-上首至尊书法体", 100))
        self.show.pack()

        try:
            self.num_quantity_outside = int(self.num_quantity.get())
            self.win = randint(1, self.num_quantity_outside)
        except ValueError:
            log("error", "输入的不是int类型")
            print(f"{tt()} | Error | 输入的不是int类型")
            print()
            messagebox.showerror("错误", "输入的不是int类型")

            self.num_ok.destroy()
            self.num_input()

        if 10 > self.num_quantity_outside > 1:
            self.time = randint(4, 6)
            self.slow = 0.05
        elif 100 > self.num_quantity_outside >= 10:
            self.time = randint(3, 5)
            self.slow = 0.05
        elif 500 > self.num_quantity_outside >= 100:
            self.time = randint(2, 4)
            self.slow = 0.02
        elif 1000 > self.num_quantity_outside >= 500:
            self.time = randint(1, 2)
            self.slow = 0.02
        elif 5000 > self.num_quantity_outside >= 1000:
            self.time = 1
            self.slow = 0.01
        else:
            log("error", "输入的数字太大了/太小了")
            print(f"{tt()} | Error | 输入的数字太大了/太小了")
            print()
            messagebox.showerror("错误", "输入的数字太大了/太小了")

            self.root.destroy()

            self.__init__()

            log("info", "重新初始化成功")
            print(f"{tt()} | Info | 重新初始化成功")
            print()

        print(f"{tt()} | Info | 号码数量：{self.num_quantity_outside}")
        print(f"{tt()} | Info | 抽奖次数：{self.time}次")
        print(f"{tt()} | Info | 中奖号码：{self.win}")
        print()

        log("info", f"号码数量：{self.num_quantity_outside}")
        log("info", f"抽奖次数：{self.time}次")
        log("info", f"中奖号码：{self.win}")

        log("debug", "")
        log("debug", "")
        log("debug", "")

        self.i = 0

        self.tk_num_ok.pack()

        log("info", "显示循环开始")
        print(f"{tt()} | Info | 显示循环开始")
        print()

        self.show_log = []

        while self.i <= self.time:
            for k in range(1, self.num_quantity_outside + 1):
                self.show_log.append(k)

                # 现在是4:08 P.M. 2024.2.12 唯一的开发有种濒临猝死的感觉
                sleep(0.05)
                self.show.config(text=k)
                self.tk_num_ok.update()

                log("debug",
                    f"当前号码：{k} | 距离中奖号码：{abs(self.win - k)} | 还剩{self.time - self.i + 1}轮 | 显示循环进行中")
                print(
                    f"{tt()} | Debug | 当前号码：{k} | 距离中奖号码：{abs(self.win - k)} | 还剩{self.time - self.i + 1}轮 | 显示循环进行中 | 页面更新成功")

                if k == self.win:
                    self.i += 1

        log("info", "显示循环结束 | 中奖号码已展示")
        print(f"{tt()} | Info | 显示循环结束 | 中奖号码已展示")
        print()

        log("info", f"遍历途中最大号码：{max(self.show_log)}")
        log("info", f"遍历途中最小号码：{min(self.show_log)}")
        print(f"{tt()} | Info | 遍历途中最大号码：{max(self.show_log)}")
        print(f"{tt()} | Info | 遍历途中最小号码：{min(self.show_log)}")
        print()

        messagebox.showinfo("提示", "本次抽奖已完成，页面即将关闭，开始下一轮")
        log("info", "提示框已弹出，页面即将关闭，开始下一轮")
        print(f"{tt()} | Info | 提示框已弹出，页面即将关闭，开始下一轮")
        print()

        self.root.destroy()

        log("info", "页面已关闭，开始下一轮")
        print(f"{tt()} | Info | 页面已关闭，开始下一轮")
        print()

        self.__init__()

        log("info", "重新初始化成功")
        print(f"{tt()} | Info | 重新初始化成功")
        print()

    def prize_input(self):
        log("critical", "该功能尚未实现，请等待后续更新(┬┬﹏┬┬)")
        print(f"{tt()} | Critical | 该功能尚未实现，请等待后续更新(┬┬﹏┬┬)")

        messagebox.showerror("致命错误", "该功能尚未实现，请等待后续更新(┬┬﹏┬┬)")

        raise NotImplementedError("该方法尚未实现(┬┬﹏┬┬)")


if __name__ == '__main__':
    root = Win()
    root.root.mainloop()
