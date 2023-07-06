###项目名称：
    Schedule-Management Software

###项目团队
    麻家乐 黄天浩 刘灿

###项目内容：
    使用C++语言开发一个有用而且有趣的日程管理软件，结合python进行图形化编程

###项目功能：
    1、账户管理：管理账号与密码，密码以密文形式保存
    2、任务录入；当用户登录后进行任务录入
    3、任务保存：当对任务进行修改后可以进行保存
    4、任务加载：用户登录后，从文件加载任务列表，保存到内存；
    5、任务删除：根据任务id删除任务；
    6、任务显示：以任务的任一属性进行排序；
    7、任务提醒：在约定的提醒时间屏幕打印提醒；

###使用说明 —— WINDOWS版本
    1、首先需要对need_make文件夹进行make操作；
    2、若您的电脑中没有make命令，可以尝试mingw32-make；
    3、若mingw32-make也出现 "不是内部或外部命令",请确认环境变量是否添加正确
    4、可以使用根目录下的mingw-get-setup.exe进行安装MinGW
    5、使用命令行进行 make 或 mingw32-make 成功后，将得到的schedule.exe覆盖放入SMS-WIN文件夹
    6、点击根目录下SMS.exe的快捷方式即可使用WINDOWS版本的SMS

###安装MinGW说明
    第一步，在出现这个界面时，点击右上角的×，然后会弹出一个弹框，点击Review Change 

<div><center>
<img src=docs/click.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图1 点击右上角的×</font>
</strong>
</center></div>

    第二步，点击Apply，这一步时间较长，等待完成即可。注意：记得添加环境变量

<div><center>
<img src=docs/click.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图2 点击Apply</font>
</strong>
</center></div>

###使用说明 —— LINUX版本
    1、首先需要对need_make文件夹进行make操作；
    2、若您的电脑中没有make命令，使用sudo apt install make命令进行make的安装；
    3、使用命令行进行 make 成功后，将得到的schedule覆盖放入SMS-LINUX文件夹
    4、在SMS-LINUX目录下在命令行中进行./SMS即可使用SMS

###页面介绍
    1、登录界面：输入账号和密码进行使用本日程管理软件

<div><center>
<img src=docs/login.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图3 登录界面</font>
</strong>
</center></div>

    2、注册界面:注册用户

<div><center>
<img src=docs/register.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图4 注册界面</font>
</strong>
</center></div>

    3、管理界面：对日程的添加与删除，排序显示，到点提醒等功能

<div><center>
<img src=docs/main.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图5 管理界面</font>
</strong>
</center></div>

    4、添加任务界面：添加一个任务，可以点击Default获取默认值

<div><center>
<img src=docs/add.png width=70% height=70% >
<br>
<strong><font face="仿宋" size=2>图6 添加任务</font>
</strong>
</center></div>

