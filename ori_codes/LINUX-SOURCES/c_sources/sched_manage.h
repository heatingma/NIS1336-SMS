#ifndef SCHED_MANAGE_H
#define SCHED_MANAGE_H

#include <string>
#include <fstream>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

class TASK
{
    private:
        int task_id;
        string task_name;
        time_t start_time; 
        int prio; //1 高，2 中，3 低
        int type; //1 学习，2 娱乐，3 生活
        time_t remind_time;

    public:
        TASK();
        TASK(int id, string name,int b,int c, time_t a, time_t d);
        string type_itos(int type);
        string prio_itos(int prio);
        string time_ttos(time_t time);   //格式：YYYY-MM-DD HH:MM:SS
        int get_prio(void){return prio;}
        time_t get_remind_time(void){return remind_time;}
        int get_id(void){return task_id;}
        int get_type(void){return type;}
        time_t get_start_time(void){return start_time;}
        string get_name(void){return task_name;}
        string get_info(void);
        string print_info(void);


};

class GUEST
{
    private:
        int max_id = 0;
        string user;
        int num_of_task;
        map<unsigned long long, TASK> tasks;

    public:
        GUEST(string in_user);
        GUEST(){};
        ~GUEST();
        void readTasks_from_file();
        void Save_to_File();
        int addTask(int id, string name,int priority, int category, string start_time,  string reminder_time);
        void printTask_by_reminder_time();
        void printTask_by_id();
        void printTask_by_start_time();
        void printTask_by_type();
        void printTask_by_priority();
        bool deleteTask(int id);
        void checktask();
        int get_max_id(){return max_id;}
};

class USERS
{
    private:
        int users_num;
        int check;
        string cur_user;
        string users[10];
    public:
        USERS();
        int get_users_num();
        bool find_user(string user);
        int check_psw(string user, string psw);
        GUEST read_task(int input_check);
        void help(void);
        bool create_user(string user, string psw);
        string encrypt(string user, string psw);
        string decrypt(string user, string cipher);

};



#endif
