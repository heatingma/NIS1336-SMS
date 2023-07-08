# -*- coding: utf-8 -*-
import pygame as pg
import sys
import subprocess
import time
from datetime import datetime
import webbrowser
#############################################################
####                    BASIC FUNCTION                   ####
#############################################################

def check_event(button:list,input:list=None,dropdown:list=None,timedropdown:list=None,lists:list=None):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pg.mouse.get_pos()
            for i in range(len(button)):
                if button[i].show:
                    button[i].check_active(mouse_x,mouse_y)
            if lists:
                for i in range(len(lists)):
                    lists[i].check_selected_box(mouse_x,mouse_y)
                    lists[i].check_delete_box(mouse_x,mouse_y)
            if input:
                for i in range(len(input)):
                    input[i].click = False
                for i in range(len(input)):
                    input[i].check_active(mouse_x,mouse_y)
            if dropdown:
                for i in range(len(dropdown)):
                    dropdown[i].handle_event(event)
            if timedropdown:
                for i in range(len(timedropdown)):
                    timedropdown[i].handle_event(event)
        elif event.type == pg.KEYDOWN:
            if(event.key == 13):
                if(button[0].msg == "Submit" or button[0].msg == 'Register'):
                    button[0].active = True
            if(input):
                for i in range(len(input)):
                    if input[i].click:
                        input[i].handle_event(event)    

def check_timer(timers:list):
    for i in range(len(timers)):
        if timers[i].show == False:
            continue
        time_str = timers[i].get_time()
        if time_str == timers[i].last_active_time:
            break
        if is_multiple_of_ten(time_str):
            timers[i].active = True
            timers[i].last_active_time = time_str

def is_multiple_of_ten(time_str):
    dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    if dt.second % 10 == 0:
        return True
    else:
        return False

def format_str(id, name, priority, type, sttime, rdtime):
    return f'{id:^5}{name:^25}{priority:^15}{type:^15}{sttime:^25}{rdtime:^25}'

def format_str_title(id, name, priority, type, sttime, rdtime):
    return f'{id:^5}{name:^18}{priority:^12}{type:^20}{sttime:^25}{rdtime:^20}'

def parse_time(time_str):
    time_parts = time_str.split(' ')
    date_parts = time_parts[0].split('-')
    time_parts = time_parts[1].split(':')
    year = str(date_parts[0])
    month = str(date_parts[1])
    day = str(date_parts[2])
    hour = str(time_parts[0])
    minute = str(time_parts[1])
    return year, month, day, hour, minute

def get_seconds(year, month, day, hour, minute):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    start_time = datetime(1970, 1, 1, 0, 0, 0)
    end_time = datetime(year, month, day, hour, minute, 0)
    time_delta = end_time - start_time
    return int(time_delta.total_seconds())

def format_date_time(year, month, day, hour, minute):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    dt = datetime(year, month, day, hour, minute)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def type_to_num(input_str):
    if input_str == "学习":
        return '1'
    elif input_str == "娱乐":
        return '2'
    elif input_str == "生活":
        return '3'
    else:
        return '4'

def type_to_EN(input_str):
    if input_str == "学习":
        return 'STUDY'
    elif input_str == "娱乐":
        return 'JOY'
    elif input_str == "生活":
        return 'LIFE'
    else:
        return 'OTHER'
    
def priority_to_num(priority_str):
    if priority_str == "高":
        return '1'
    elif priority_str == "中":
        return '2'
    elif priority_str == "低":
        return '3'
    else:
        return '4'
    
def priority_to_EN(priority_str):
    if priority_str == "高":
        return 'HIGH'
    elif priority_str == "中":
        return 'MEDUIM'
    elif priority_str == "低":
        return 'LOW'
    else:
        return 'UNKNOWN'

def full_to_abbr(full:str):
    fulls = ["ID","PROIRITY","TYPE","START TIME","REMIND TIME"]
    abbrs = ["id","priority","type","remind","start"]
    for i in range(5):
        if full == fulls[i]:
            return abbrs[i]
    return "id"

def parse_tasks_string(tasks_string):
    tasks_list = tasks_string.strip().split('\n')
    tasks = []
    for task in tasks_list:
        task_parts = task.split()
        sttime = task_parts[4] + " " + task_parts[5]
        rdtime = task_parts[6] + " " + task_parts[7]
        task_obj = TASK(task_parts[0], task_parts[1], priority_to_EN(task_parts[2]), type_to_EN(task_parts[3]), sttime, rdtime)
        tasks.append(task_obj)
    return tasks

#############################################################
####                    MAIN CLASS                       ####
#############################################################

class SM():
    def __init__(self):
        self.page = "menu"
        self.check = False
        self.shell = cmds()
        self.screen_size = (1000,700)
        self.screen_color = pg.Color((230,230,230))
        self.screen = pg.display.set_mode(self.screen_size)
        self.title = textBox(200, 80, 600, 70, font=40, color=self.screen_color, font_color='red')
        self.exit_button = Button(800, 600, 100, 30, "EXIT", font=16, button_color='silver', text_color='black', border_color='darkgray')
        self.home_button = Button(800, 550, 100, 30, "HOME", font=16, button_color='silver', text_color='black', border_color='darkgray')
        
    def exit(self):
        sys.exit()                 
       
    def page_change(self,page:str):
        self.page = page
              
    def menu_init(self):        
        self.acc_label = textBox(280, 200, 100, 30, font=20, color=self.screen_color, font_color='black')
        self.psw_label = textBox(280, 250, 100, 30, font=20, color=self.screen_color, font_color='black')
        self.acc_input = textBox(400, 200, 200, 30, font=24, color="#eeeeee", font_color='black', x_format='left')
        self.psw_input = textBox(400, 250, 200, 30, font=24, color="#eeeeee", font_color='black', x_format='left')
        self.sub_button = Button(650, 250, 100, 30, "Submit", font=16, button_color='silver', text_color='black', border_color='darkgray')
        self.tip_box = textBox(250, 310, 500, 40, font=18, color=self.screen_color, font_color='red')
        self.team_button = Button(400, 385, 200, 40, "TEAM", font=20, button_color='#afeeee', text_color='black', border_color="#87ceeb")
        self.help_button = Button(400, 440, 200, 40, "HELP", font=20, button_color='#afeeee', text_color='black', border_color="#87ceeb")
        self.login_button = Button(400, 495, 200, 40, "LOGIN", font=20, button_color='#afeeee', text_color='black', border_color="#87ceeb")
        self.register_button = Button(400, 550, 200, 40, "REGISTER", font=20, button_color='#afeeee', text_color='black', border_color="#87ceeb")

    def menu_action(self):
        self.psw_label.input("Password:")
        self.acc_label.input("Account:")
        while(True):
            check_event(button = [self.sub_button,self.exit_button,self.team_button,self.login_button,\
                        self.help_button,self.register_button],input= [self.psw_input,self.acc_input])
            if self.exit_button.active:
                self.exit()
            elif self.sub_button.active:
                self.sub_button.active = False
                acc = self.acc_input.text
                psw = self.psw_input.text
                if (acc == "" or psw == ""):
                    self.tip_box.input("Account or password cannot be empty")
                else:
                    result = self.shell.login(acc,psw)
                    if result == -1:
                        self.tip_box.input("Password Error")
                    elif result == -2:
                        self.tip_box.input("Account Does Not Exist")
                    if result >= 0:
                        self.check = True
                        self.user = acc
                        self.tip_box.input("You can click LOGIN button to use the software")
            elif self.team_button.active:
                self.team_button.active = False
                self.page = "team"
                break
            elif self.help_button.active:
                self.help_button.active = False
                self.page = "help"
                break
            elif self.login_button.active:
                self.login_button.active = False
                if self.check:
                    self.page = "main"
                    break
                else:
                    self.tip_box.show = True
                    self.tip_box.input("You must input the right account and password")
            elif self.register_button.active:
                self.register_button.active = False
                self.page = "register"
                break
            self.update_screen([self.title,self.acc_label,self.psw_label,self.acc_input,self.register_button,
                                self.psw_input,self.sub_button,self.exit_button,self.team_button,\
                                self.login_button,self.help_button,self.tip_box]) 
            
    def main_init(self): 
        self.show_state = False
        self.timer_box = textBox(100, 200, 50, 30, font=18, color=self.screen_color, font_color='black')
        self.timer = Timer(150, 200, 200, 30, bg_color=self.screen_color)
        self.task_lists = LISTS(100, 250,[50,180,100,100,180,180] , 40, title=["ID","TASK","PROIRITY","TYPE","START TIME","REMIND TIME"], \
            title_font=16, font=16, color="#dddddd",font_color='black')
        self.last_button = Button(400, 200, 90, 30, "LAST", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.next_button = Button(500, 200, 90, 30, "NEXT", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.show_button = Button(600, 200, 90, 30, "SHOW", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.add_button = Button(700, 200, 90, 30, "ADD", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.delete_button = Button(800, 200, 90, 30, "DELETE", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.tip_box = textBox(200, 520, 300, 30, font=18, color=self.screen_color, font_color='black')
        self.remind_box = textBox(300, 250, 400, 200, font=20, color="#dfeeee", font_color='blue',
                                  font_name='FONTS/STKAITI.TTF', ttf=True, bold=False,border=True,border_color="blue")
        self.ok_button = Button(630, 400, 50, 30, "OK", font=16, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
    
    def main_action(self):
        self.timer_box.input("TIME:")
        self.next_button.show = False
        self.last_button.show = False
        self.remind_box.show = False
        self.ok_button.show = False
        while(True):
            check_event( button = [self.home_button,self.exit_button,self.show_button,self.add_button,
                                   self.delete_button,self.next_button,self.last_button,self.ok_button], lists=[self.task_lists])
            check_timer(timers=[self.timer])
            
            if self.exit_button.active:
                self.exit()
            
            elif self.timer.active:
                self.timer.active = False
                result = self.timer.shell_action(self.shell,self.user)
                if result[-6:-2] == "MISS" or result [-6:-2] == "TODO":
                    self.show_button.active = True
                    self.task_lists.clean_all()
                    self.show_state = False
                    if result[-6:-2] == "MISS":
                        message = "错过提醒:\n"
                    else:
                        message = "任务提醒:\n"
                    message += "任务名称       开始时间\n"
                    message += result[:-6]
                    self.remind_box.input(message)
                    self.ok_button.show = True
                    self.remind_box.show = True
            
            elif self.ok_button.active:
                self.ok_button.active = False
                self.ok_button.show = False
                self.remind_box.show = False  
                self.remind_box.input("")          
                
            elif self.home_button.active:
                self.home_button.active = False
                self.page = "menu"
                break
            
            elif self.add_button.active:
                self.add_button.active = False
                self.page = "add"
                break
            
            elif self.delete_button.active:
                self.delete_button.active = False
                if self.show_state:
                    num = self.task_lists.delete_num
                    tasks_id = self.task_lists.delete_box
                    if num > 0:
                        for i in range(num):
                            self.shell.delete_tasks(self.user,tasks_id[i])
                    self.task_lists.delete_box = []
                    self.show_button.active = True
                    self.task_lists.clean_all()
                    self.task_lists.delete_num = 0
                    self.show_state = False
                    
                    if num == 1:
                        message = "successfully delete the task whose ID is {}".format(tasks_id) 
                        self.tip_box.input(message) 
                    elif num > 1:
                        message = "successfully delete the tasks whose ID are {}".format(tasks_id) 
                        self.tip_box.input(message) 
                              
            if self.show_button.active:
                self.show_button.active = False
                if self.show_state == False:
                    self.show_state = True
                    self.next_button.show = True
                    self.last_button.show = True
                    self.show_button.change_color("orange")
                    selected_box = self.task_lists.get_selected_box()
                    selected_box.change_color("orange")
                    selected_name = full_to_abbr(selected_box.text)
                    result = self.shell.show_tasks(self.user,selected_name)
                    if result is not None:
                        for i in range(len(result)):
                            self.task_lists.add_row(result[i].get_task_list())
                else:
                    self.show_state = False
                    self.task_lists.clean_all()
                    self.show_button.change_color("#dfeeee")
            
            elif self.next_button.active:
                self.next_button.active = False
                if self.task_lists.begin < self.task_lists.row - 5:
                    self.task_lists.change_begin(self.task_lists.begin + 5)
                    
            elif self.last_button.active:
                self.last_button.active = False
                if self.task_lists.begin > 0:
                    self.task_lists.change_begin(self.task_lists.begin - 5)
                       
            elif self.task_lists.active:
                self.task_lists.active = False
                if self.show_state:
                    selected_box = self.task_lists.get_selected_box()
                    selected_box.change_color("orange")
                    selected_name = full_to_abbr(selected_box.text)
                    result = self.shell.show_tasks(self.user,selected_name)
                    if result is not None:
                        self.task_lists.clean_all()
                        for i in range(len(result)):
                            self.task_lists.add_row(result[i].get_task_list())
                
            self.update_screen([self.title,self.timer,self.timer_box,self.exit_button,self.home_button,
                                self.show_button,self.delete_button,self.add_button,self.task_lists,
                                self.next_button,self.last_button,self.tip_box,self.remind_box,self.ok_button]) 
                                      
    def add_task_init(self):
        self.timer_box = textBox(160, 200, 50, 30, font=18, color=self.screen_color, font_color='black')
        self.timer = Timer(210, 200, 200, 30, bg_color=self.screen_color)
        self.prio_box = textBox(150, 260, 100, 30, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='black')
        self.prio_drop = Dropdown(260, 260, 100, 30, label="选择", options=["高", "中", "低", "未知"], font=18, font_name='FONTS/STKAITI.TTF', ttf=True,
                                bg_color=self.screen_color, border_color='gray')
        self.type_box = textBox(370, 260, 80, 30, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='black')
        self.type_drop = Dropdown(460, 260, 120, 30, label="选择", options=["学习", "娱乐", "生活", "其他"], font=18, font_name='FONTS/STKAITI.TTF', ttf=True,
                                bg_color=self.screen_color, border_color='gray')
        self.name_box = textBox(150, 320, 100, 30, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='black')
        self.name_input_box = textBox(260, 320, 400, 30, font=18, font_name='FONTS/STKAITI.TTF', ttf=True, color="#eeeeee", font_color='black')

        self.sttime_box = textBox(150, 370, 100, 30, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='black')
        self.sttime_drop = TimeDropdown(260, 370, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, bg_color=self.screen_color)
        self.rdtime_box = textBox(150, 420, 100, 30, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='black')
        self.rdtime_drop = TimeDropdown(260, 420, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, bg_color=self.screen_color)

        self.tip_box = textBox(200, 490, 450, 150, font=20, font_name='FONTS/STKAITI.TTF', ttf=True, color=self.screen_color, font_color='blue', bold=False)

        self.return_button = Button(800, 200, 90, 30, "RETURN", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.default_button = Button(600, 200, 90, 30, "DEFAULT", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        self.add_button = Button(700, 200, 90, 30, "ADD", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
    
    def add_task_action(self):
        self.timer_box.input("TIME:")
        self.name_box.input("任务名称")
        self.prio_box.input("优先级")
        self.type_box.input("种类")
        self.sttime_box.input("开始时间")
        self.rdtime_box.input("提醒时间")
        while(True):
            check_event( button  = [self.default_button,self.add_button,self.return_button,self.exit_button],
                         input   = [self.name_input_box],
                        dropdown = [self.prio_drop,self.type_drop], 
                    timedropdown = [self.sttime_drop,self.rdtime_drop])
            if self.exit_button.active:
                self.exit()
            elif self.return_button.active:
                self.return_button.active = False
                self.page = "main"
                break
            elif self.default_button.active:
                self.default_button.active = False
                time = self.timer.get_time()
                yy,mm,dd,hh,ss = parse_time(time)
                self.sttime_drop.set_time(yy,mm,dd,hh,ss)
                self.rdtime_drop.set_time(yy,mm,dd,hh,ss)
                self.type_drop.set_selected("学习")
                self.prio_drop.set_selected("高")
                self.name_input_box.input("task")
            elif self.add_button.active:
                self.add_button.active = False
                task_name = self.name_input_box.text.replace(" ","_")
                task_type = type_to_num(self.type_drop.selected)
                task_prio = priority_to_num(self.prio_drop.selected)
                sttime = self.sttime_drop.get_time()
                rdtime = self.rdtime_drop.get_time()
                result = self.shell.add_task(task_name,task_prio,task_type,sttime,rdtime,self.user)
                if (result == -1):
                    message = "Task {} already exists".format(task_name)
                    self.tip_box.change_font_color("red")
                    self.tip_box.change_font_size(24)
                else:
                    self.tip_box.change_font_color("blue")
                    message = "Add a new task successfully\n"
                    message += "任务ID: {}  任务名称: {}  优先级: {} 类别: {}\n".format(result,task_name,
                                self.prio_drop.selected,self.type_drop.selected)
                    message += "开始时间: {}  提醒时间: {}\n".format(sttime,rdtime)
                    self.tip_box.change_font_size(20)
                self.tip_box.input(message)
                

            self.update_screen([self.title,self.timer,self.tip_box,self.timer_box,self.exit_button,self.return_button,self.add_button,\
                                self.default_button,self.rdtime_box,self.rdtime_drop,self.sttime_box,self.sttime_drop,
                                self.name_box,self.name_input_box,self.type_box,self.type_drop,self.prio_box,self.prio_drop]) 
    
    def register_init(self):
        self.info_box = textBox(250, 200, 500, 40, font=18, color=self.screen_color, font_color='blue')
        self.acc_label = textBox(250, 270, 130, 30, font=20, color=self.screen_color, font_color='black')
        self.psw_label = textBox(250, 320, 130, 30, font=20, color=self.screen_color, font_color='black')
        self.acc_input = textBox(400, 270, 200, 30, font=20, color="#dddddd", font_color='black', x_format='left')
        self.psw_input = textBox(400, 320, 200, 30, font=20, color="#dddddd", font_color='black', x_format='left')
        self.register_button = Button(400, 480, 200, 40, "REGISTER", font=20, button_color='#afeeee', text_color='black')
        self.tip_box = textBox(300, 370, 400, 100, font=18, color=self.screen_color, font_color='red')
    
    def register_action(self):
        self.info_box.input("Please input account_name and password to create an account")
        self.psw_label.input("Password:")
        self.acc_label.input("Account:")
        self.tip_box.show = False
        while(True):
            check_event(button = [self.home_button,self.sub_button,self.exit_button,self.register_button],\
                input= [self.psw_input,self.acc_input])
            if self.exit_button.active:
                self.exit()
            elif self.home_button.active:
                self.home_button.active = False
                self.page = "menu"
                break
            elif self.register_button.active:
                self.register_button.active = False
                acc = self.acc_input.text
                psw = self.psw_input.text
                if (acc == "" or psw == ""):
                    self.tip_box.input("Account or password cannot be empty")
                else:
                    result = self.shell.register(acc,psw)
                    if result:
                        self.tip_box.show = True
                        message = "Successfully create an account\n"
                        message += "Account:  {} \n".format(acc)
                        message += "Password: {} ".format(psw)
                        self.tip_box.input(message)
                    else:
                        self.tip_box.input("Account already exists")
                self.acc_input.input("")
                self.psw_input.input("")
                
            self.update_screen([self.title,self.acc_label,self.psw_label,self.acc_input,self.register_button,
                                self.psw_input,self.exit_button,self.home_button,self.tip_box,self.info_box]) 
    
    def team_init(self):
        message  = "Schedule Management Software\n\n"
        message += "Software Version:   1.0.0\n\n"
        message += "Team Members:    heatingma   ccliu-u    hth\n\n"
        message += "Github: https://github.com/heatingma/NIS1336-SMS"
        self.team_box = textBox(280,220,500,200,font=18,color=self.screen_color,font_color='blue',x_format='left',y_format='up')
        self.team_box.input(message)
    
    def team_action(self):
        while(True):
            check_event([self.home_button,self.exit_button])
            if self.home_button.active:
                self.home_button.active = False
                self.page = "menu"
                break
            elif self.exit_button.active:
                self.exit()
            self.update_screen([self.title,self.home_button,self.team_box,self.exit_button]) 
    
    def help_init(self):
        self.web_button = Button(800, 500, 100, 30, "MORE", font=18, button_color='#dfeeee', text_color='black', border_color="#b0ceeb")
        message  = "Step 1: Click LOGIN and input your Account and password to use the softwareEnter\n\n"
        message += "Step 2: Click SHOW to display a list of all current tasks\n\n"
        message += "Step 3: Click ADD to add a new task\n\n"
        message += "Step 4: Select a task ID and click DELETE to delete the task\n\n"
        message += "Note 1: If you don't have an account, you can click REGISTER to register it\n\n"
        message += "Note 2: Click MORE for more information"
        self.help_box = textBox(150,190,600,300,font=18,color=self.screen_color,font_color='black',x_format='left',y_format='up')
        self.help_box.input(message)
        
    def help_action(self):
        while(True):
            check_event([self.web_button,self.home_button,self.exit_button])
            if self.home_button.active:
                self.home_button.active = False
                self.page = "menu"
                break
            elif self.exit_button.active:
                self.exit()
            elif self.web_button.active:
                self.web_button.active = False
                webbrowser.open('https://github.com/heatingma/NIS1336-SMS')
            self.update_screen([self.title,self.home_button,self.help_box,self.exit_button,self.web_button]) 
    
    def update_screen(self,list:list):
        self.screen.fill(self.screen_color)
        self.title.input("Schedule Management")
        for i in range(len(list)):
            if list[i].show:
                list[i].draw(self.screen)
        pg.display.flip()
  
class TASK:
    def __init__(self,id,name,prio,type,sttime,rdtime):
        self.id = id
        self.name = name
        self.prio = prio
        self.type = type
        self.sttime = sttime
        self.rdtime = rdtime
        
    def get_task_list(self):
        return [self.id,self.name,self.prio,self.type,self.sttime,self.rdtime]
  
class cmds:
    def __init__(self):
        self.procs = dict()
        self.pids = dict()
                 
    def run_command(self, command, command_name):
        proc = subprocess.Popen(command,stdout=subprocess.PIPE)
        time.sleep(0.1)
        self.pids[command_name] = proc.pid
        self.procs[command_name] = proc
        time.sleep(0.1)
        return proc
    
    def login(self,acc,psw):
        command = ['./schedule', 'login', acc, psw]
        proc = self.run_command(command,"login")
        output = ''
        while proc.poll() is None:
            output += proc.stdout.readline().decode('utf-8')
        output += proc.stdout.read().decode('utf-8')
        return int(output)
    
    def register(self,acc,psw):
        command = ['./schedule', 'register', acc, psw]
        proc = self.run_command(command,"register")
        output = ''
        while proc.poll() is None:
            output += proc.stdout.readline().decode('utf-8')
        output += proc.stdout.read().decode('utf-8')
        return int(output)
    
    def add_task(self,name,prio,type,sttime,rdtime,user_name):
        command = ['./schedule', 'add_task', name, prio, type, sttime, rdtime, user_name]
        proc = self.run_command(command,"add_task")
        output = ''
        while proc.poll() is None:
            output += proc.stdout.readline().decode('utf-8')
        output += proc.stdout.read().decode('utf-8')
        return int(output)
    
    def show_tasks(self,user_name,method="id"):
        command = ['./schedule', 'show_tasks', user_name, method]
        proc = self.run_command(command,"show_tasks")
        output = ''
        while proc.poll() is None:
            output += proc.stdout.readline().decode('utf-8')
        output += proc.stdout.read().decode('utf-8') 
        if output == '':
            return None
        output = parse_tasks_string(output) 
        return output
    
    def delete_tasks(self,user_name:str,id:str):
        command = ['./schedule', 'delete_task', user_name,id]
        self.run_command(command,"delete_task")       
        return

    def check_remind(self,user_name):
        command = ['./schedule', 'check_remind', user_name]
        proc = self.run_command(command,"check_remind")
        output = ''
        while proc.poll() is None:
            output += proc.stdout.readline().decode('utf-8')
        output += proc.stdout.read().decode('utf-8') 
        return output
               
    
#############################################################
####                    BASIC CLASS                      ####
#############################################################

class Button:
    def __init__(self, x, y, w, h, msg, font_name="Georgia", font=24, button_color=(0, 255, 0), text_color=(255, 255, 255),
                 border_radius=15, border_width=2, border_color=(255, 255, 255, 128)):
        self.active = False
        self.check = False
        self.button_color = pg.Color(button_color)
        self.text_color = pg.Color(text_color)
        self.border_radius = border_radius
        self.border_width = border_width
        self.border_color = pg.Color(border_color)
        self.font = pg.font.SysFont(font_name, font)
        self.rect = pg.Rect(x, y, w, h)
        self.msg = msg
        self.show = True
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def change_color(self, color):
        self.button_color = color
        self.prep_msg(self.msg)

    def draw(self, screen):
        if self.show:
            border_rect = self.rect.copy()
            border_rect.inflate_ip(self.border_width * 2, self.border_width * 2)
            pg.draw.rect(screen, self.border_color, border_rect, border_radius=self.border_radius)
            pg.draw.rect(screen, self.button_color, self.rect, border_radius=self.border_radius)
            screen.blit(self.msg_image, self.msg_image_rect)

    def check_active(self, x, y):
        if self.check == False:
            if self.rect.collidepoint(x, y):
                self.active = True
            
class textBox:
    def __init__(self, x, y, w, h, font=20,color='white',font_color='black'
                 ,font_name="Times New Roman",ttf=False,x_format='center',y_format='center'
                 ,x_space=5,y_space=5,border_radius=10,bold=True,italic=False,
                 border=False,border_width=2,border_color="black"):
        self.rect = pg.Rect(x, y, w, h)
        self.click =  False
        self.color = pg.Color(color)
        self.font_color = pg.Color(font_color)
        self.text = ""
        self.write = True
        self.ttf = ttf
        self.bold = bold
        self.italic = italic
        self.font_name = font_name
        self.border = border
        self.border_width = border_width
        self.border_color = border_color
        if self.ttf:
            self.FONT = pg.font.Font(self.font_name,font)
            self.FONT.set_bold(self.bold)
            self.FONT.set_italic(self.italic)
        else:
            self.FONT = pg.font.SysFont(name=self.font_name,size=font,bold=self.bold,italic=self.italic)
        self.x_format = x_format
        self.y_format = y_format
        self.x_space = x_space
        self.y_space = y_space
        self.border_radius = border_radius
        self.show = True
        
    def check_active(self,x,y):
        if(self.click == False):
            if self.rect.collidepoint(x,y):
                self.click = True  
                  
    def change_font_size(self,font_size):            
        if self.ttf:
            self.FONT = pg.font.Font(self.font_name,font_size)
            self.FONT.set_bold(self.bold)
            self.FONT.set_italic(self.italic)
        else:
            self.FONT = pg.font.SysFont(name=self.font_name,size=font_size,bold=self.bold,italic=self.italic)
            
    def input(self,input):
        if self.write:
            self.text = input
    
    def clear(self):
        self.text = ""
        
    def change_font_color(self,color):
        self.font_color = pg.Color(color)        
    
    def change_color(self,color):
        self.color = pg.Color(color)
    
    def handle_event(self,event:pg.event.Event):
        if self.write:
            if (event.key == pg.K_BACKSPACE):
                self.text = self.text[0:-1]
            elif(event.key == pg.K_ESCAPE):
                sys.exit()
            elif(event.key == 13):
                pass
            elif(event.key >= 0 and event.key <= 128):
                letter = chr(event.key)
                self.text += letter             
           
    def draw(self, screen):
        if self.border:
            border_rect = self.rect.copy()
            border_rect.inflate_ip(self.border_width * 2, self.border_width * 2)
            pg.draw.rect(screen, self.border_color, border_rect, border_radius=self.border_radius)
            pg.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        else:
            pg.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
            # 绘制文本
        self.texts = []
        current_text = ''
        for i in range(len(self.text)):
            if(self.text[i] != '\n'):
                current_text += self.text[i]
            else:
                self.texts.append(current_text)
                current_text = ''
        self.texts.append(current_text)
        length = len(self.texts)
        for i in range(length):
            current_text = self.texts[i]
            text_surface = self.FONT.render(current_text,True,self.font_color)
            text_surface_rect = text_surface.get_rect()
            if(self.x_format == 'center'):
                text_surface_rect.centerx = self.rect.centerx
            elif(self.x_format == 'left'):
                text_surface_rect.x = self.rect.x + self.x_space
            if(self.y_format == 'center'):
                space_height = (self.rect.h - length * text_surface_rect.h)/(length+1)
                text_surface_rect.y = self.rect.y + space_height*(i+1) + text_surface_rect.h*i
            elif(self.y_format == 'up'):
                space_height = self.y_space
                text_surface_rect.y = self.rect.y + space_height*(i+1) + text_surface_rect.h*i
            screen.blit(text_surface,text_surface_rect)
              
class ListBoxes:
    def __init__(self,x,y,w,h,title=None,title_font=24,font=20,color='white',font_color='black',
                 font_name="Times New Roman",ttf=False,x_format='center',y_format='center'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.begin = 0        
        self.len = 0
        self.font = font
        self.color = color
        self.font_color = font_color
        self.font_name = font_name
        self.ttf = ttf
        self.x_format = x_format
        self.y_format = y_format
        self.show = True
        self.rects = []
        self.rects.append(textBox(x,y,w,h,title_font,color,font_color,font_name,ttf,'center','center'))
        if(title):
            self.rects[0].input(title)
        else:
            self.rects[0].input("List")
    
    def clean_box(self):
        for _ in range(self.len):
            self.rects.pop()
        self.len = 0
    
    def add_box(self,input=None):
        self.len += 1
        yy = (self.h+2) * ((self.len-1)%5 + 1)  + self.y  
        box = textBox(self.x,yy,self.w,self.h,self.font,self.color,
                      self.font_color,self.font_name,self.ttf,self.x_format,self.y_format)
        if input:
            box.input(input)
        self.rects.append(box)            
                
    def delete_box(self,id=None):
        self.len -= 1
        if id is None:
            self.rects.pop()
        else:
            del self.rects[id]
            
    def input(self,id,input):
        self.rects[id].input(input)

    def handle_event(self,event):
        if self.len >= 1:
            for i in range(self.len):
                self.rects[i+1].handle_event(event)
                                    
    def draw(self, screen):
        self.rects[0].draw(screen)
        for i in range(min(self.len-self.begin,5)):
            self.rects[i+self.begin+1].draw(screen)

class LISTS:
    def __init__(self,x,y,w:list,h,title:list,title_font=24,font=20,color='white',font_color='black',
                 font_name="Times New Roman",ttf=False,x_format='center',y_format='center'):
        self.lists = list()
        self.row = 0
        self.show = True
        self.begin = 0
        self.len = len(w)
        self.color = color
        self.active = False 
        self.delete_num = 0
        self.delete_box = []
        for i in range(self.len):
            self.lists.append(ListBoxes(x, y, w[i], h, title[i], title_font, font, color, font_color, font_name, ttf, x_format, y_format))
            x = x+w[i]
        self.selected_box = self.lists[0].rects[0]

    def get_selected_box(self):
        return self.selected_box
    
    def restore_color(self):
        for i in range(self.len):
            self.lists[i].rects[0].change_color(self.color)
    
    def clean_all(self):
        self.row = 0
        for i in range(self.len):
            self.lists[i].clean_box()
    
    def add_row(self,input:list):
        self.row += 1
        for i in range(self.len):
            self.lists[i].add_box(input[i])           
                
    def delete_list(self,id=None):
        del self.lists[id].rects[id]
        
    def delete_row(self,id=None):
        self.row -= 1
        for i in range(self.len):
            self.lists[i].delete_box(id)
            
    def input(self,id,input):
        self.rects[id].input(input)

    def handle_event(self,event):
        for i in range(self.len):
            self.lists[i].handle_event(event)
    
    def check_selected_box(self,x,y):
        for i in range(self.len):
            if(self.lists[i].rects[0].rect.collidepoint(x,y)):
                if self.selected_box != self.lists[i].rects[0]:
                    self.selected_box = self.lists[i].rects[0]
                    self.active = True
                    self.restore_color()
    
    def check_delete_box(self,x,y):
        if self.row == 0:
            return
        length = min((self.row-self.begin),5)
        for i in range(length):
            cur_box = self.lists[0].rects[i+1+self.begin]
            if(cur_box.rect.collidepoint(x,y)):
                if self.delete_num == 0:
                    self.delete_num += 1
                    cur_box.change_color("orange")
                    self.delete_box.append(cur_box.text)
                else:
                    flag = True
                    for j in range(self.delete_num):
                        if self.delete_box[j] == cur_box.text:
                            cur_box.change_color(self.color)
                            self.delete_box.remove(cur_box.text)
                            self.delete_num -= 1
                            flag  = False
                            break
                    if flag:
                        cur_box.change_color("orange")
                        self.delete_box.append(cur_box.text)
                        self.delete_num += 1
    
    def change_begin(self,begin):
        self.begin = begin
        for i in range(self.len):
            self.lists[i].begin = begin                
                                        
    def draw(self, screen):
        for i in range(self.len):
            self.lists[i].draw(screen)       
    
class Dropdown:
    def __init__(self, x, y, w, h, label, options=["None"], font=20, font_name="Hack",ttf=False,
                 label_color="#999999", font_color="black", bg_color="white", border_color="black",
                 click_color="orange", border_radius=10, max_options=4):
        self.rect = pg.Rect(x, y, w, h)
        self.options = options
        self.label = label
        self.label_color = label_color
        if ttf:
            self.font = pg.font.Font(font_name, font)
        else:
            self.font = pg.font.SysFont(name=font_name, size=font)
        self.font_color = font_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.click_color = click_color
        self.border_radius = border_radius
        self.active = False
        self.selected = None
        self.show = True
        self.max_options = max_options
        self.first_option_index = 0

    def change_options(self, options):
        self.option = options
        self.first_option_index = 0

    def set_selected(self,selected):
        self.selected = selected
        
    def draw(self, surface):
        if self.show:
            pg.draw.rect(surface, self.bg_color, self.rect, border_radius=self.border_radius)
            pg.draw.rect(surface, self.border_color, self.rect, 1, border_radius=self.border_radius)

            if self.selected is None:
                text = self.font.render(self.label, True, self.label_color)
            else:
                text = self.font.render(self.selected, True, self.font_color)

            text_rect = text.get_rect()
            text_rect.center = self.rect.center
            surface.blit(text, text_rect)

            if self.active:
                max_visible_options = min(self.max_options, len(self.options))
                options_rect = pg.Rect(self.rect.left, self.rect.bottom, self.rect.w, self.rect.h * max_visible_options)
                pg.draw.rect(surface, self.bg_color, options_rect, border_radius=self.border_radius)
                pg.draw.rect(surface, self.border_color, options_rect, 1, border_radius=self.border_radius)

                for i in range(self.first_option_index, self.first_option_index + max_visible_options):
                    if i >= len(self.options):
                        break
                    option = self.options[i]
                    option_rect = pg.Rect(self.rect.left, self.rect.bottom + (i - self.first_option_index) * self.rect.h,
                                          self.rect.w, self.rect.h)
                    if option_rect.collidepoint(pg.mouse.get_pos()):
                        pg.draw.rect(surface, self.click_color, option_rect, border_radius=self.border_radius)
                    else:
                        pg.draw.rect(surface, self.bg_color, option_rect, border_radius=self.border_radius)

                    option_text = self.font.render(option, True, self.font_color)
                    option_text_rect = option_text.get_rect()
                    option_text_rect.center = option_rect.center
                    surface.blit(option_text, option_text_rect)

    def handle_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.active = not self.active
        elif self.active:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 4:
                # Scroll up
                self.first_option_index = max(0, self.first_option_index - 1)
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 5:
                # Scroll down
                max_visible_options = min(self.max_options, len(self.options))
                last_visible_option_index = self.first_option_index + max_visible_options - 1
                if last_visible_option_index < len(self.options) - 1:
                    self.first_option_index += 1
            else:
                for i in range(self.first_option_index, len(self.options)):
                    option_rect = pg.Rect(self.rect.left, self.rect.bottom + (i - self.first_option_index) * self.rect.h,
                                          self.rect.w, self.rect.h)
                    if option_rect.collidepoint(event.pos):
                        self.selected = self.options[i]
                        self.active = False
                        break
    
class TimeDropdown:
    def __init__(self,x,y,bg_color="white",font=16,font_name='Hack',ttf=False):
        self.x = x
        self.y = y
        self.bg_color = bg_color
        self.show = True
        self.font = font
        self.font_name = font_name
        self.ttf = ttf
        self.create()
        
    def create(self):
        self.yy_box = textBox(self.x+50,self.y,30,30,font=self.font,color=self.bg_color,
                              font_color='black',font_name=self.font_name,ttf=self.ttf)
        self.yy_box.input("年")
        self.yy_drop = Dropdown(self.x,self.y,50,30,label="year",options=[str(year) for year in range(2023, 2034)],
                                bg_color=self.bg_color,border_color='gray') 
        self.mm_box = textBox(self.x+130,self.y,30,30,font=self.font,color=self.bg_color,
                              font_color='black',font_name=self.font_name,ttf=self.ttf)
        self.mm_box.input("月")
        self.mm_drop = Dropdown(self.x+80,self.y,50,30,label="month",options=[str(month) for month in range(1,13)],
                                bg_color=self.bg_color,border_color='gray')  
        self.dd_box = textBox(self.x+210,self.y,30,30,font=self.font,color=self.bg_color,
                              font_color='black',font_name=self.font_name,ttf=self.ttf)
        self.dd_box.input("日")
        self.dd_drop = Dropdown(self.x+160,self.y,50,30,label="day",options=[str(day) for day in range(1, 31)],
                                bg_color=self.bg_color,border_color='gray')
        self.hh_box = textBox(self.x+290,self.y,30,30,font=self.font,color=self.bg_color,
                              font_color='black',font_name=self.font_name,ttf=self.ttf)
        self.hh_box.input("时")
        self.hh_drop = Dropdown(self.x+240,self.y,50,30,label="hour",options=[str(hour) for hour in range(0, 24)],
                                bg_color=self.bg_color,border_color='gray') 
        self.ss_box = textBox(self.x+380,self.y,30,30,font=self.font,color=self.bg_color,
                              font_color='black',font_name=self.font_name,ttf=self.ttf)
        self.ss_box.input("分")
        self.ss_drop = Dropdown(self.x+320,self.y,60,30,label="second",options=[str(second) for second in range(1, 61)],
                                bg_color=self.bg_color,border_color='gray')
        self.obj_list = [self.yy_box,self.yy_drop,self.mm_box,self.mm_drop,self.dd_box,self.dd_drop,\
                         self.hh_box,self.hh_drop,self.ss_box,self.ss_drop]
        self.handle_list = [self.yy_drop,self.mm_drop,self.dd_drop,self.hh_drop,self.ss_drop]
        
    def draw(self,surface):
        for i in range(len(self.obj_list)):
            self.obj_list[i].draw(surface)
    
    def handle_event(self,event:pg.event.Event):
        for i in range(len(self.handle_list)):
            self.handle_list[i].handle_event(event)
    
    def set_time(self,yy=None,mm=None,dd=None,hh=None,ss=None):
        if yy is not None:
            self.yy_drop.set_selected(yy)
        if mm is not None:
            self.mm_drop.set_selected(mm)
        if dd is not None:
            self.dd_drop.set_selected(dd)
        if hh is not None:
            self.hh_drop.set_selected(hh)        
        if ss is not None:
            self.ss_drop.set_selected(ss)   
            
    def get_time(self):
        yy = self.yy_drop.selected
        mm = self.mm_drop.selected  
        dd = self.dd_drop.selected
        hh = self.hh_drop.selected
        ss = self.ss_drop.selected
        if (yy is None or mm is None or dd is None or hh is None or ss is None):
            return None
        else:
            return format_date_time(yy,mm,dd,hh,ss)

class Timer:
    def __init__(self, x, y, w, h, font_name='Times New Roman', font_size=20, font_color="black", bg_color="white"):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.font = pg.font.SysFont(font_name, font_size)
        self.font_color = font_color
        self.bg_color = bg_color
        self.show = True
        self.active = False
        now = datetime.now()
        self.time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        self.last_active_time = now.strftime('%Y-%m-%d %H:%M:%S')
        
    def draw(self, screen):
        now = datetime.now()
        self.time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        time_text = self.font.render(self.time_str, True, self.font_color, self.bg_color)
        time_rect = time_text.get_rect()
        time_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        pg.draw.rect(screen, self.bg_color, (self.x, self.y, self.width, self.height))
        screen.blit(time_text, time_rect)
    
    def get_time(self):
        return self.time_str

    def shell_action(self,shell:cmds,user_name):
        return shell.check_remind(user_name)

                     
#############################################################
####                     SOFTWARE                        ####
#############################################################

def main():
    pg.init()
    pg.display.set_caption("Schedule Manage")
    work = SM()
    while True:
        if work.exit_button.active:
            sys.exit()
        if(work.page == 'menu'):
            work.menu_init()
            work.menu_action()
        elif(work.page == 'main'):
            work.main_init()
            work.main_action()
        elif(work.page == 'add'):
            work.add_task_init()
            work.add_task_action()
        elif(work.page == 'help'):
            work.help_init()
            work.help_action()
        elif(work.page == 'team'):
            work.team_init()
            work.team_action()
        elif(work.page == 'register'):
            work.register_init()
            work.register_action()
            
if __name__ == "__main__":
    main()

   