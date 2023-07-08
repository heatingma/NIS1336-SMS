#include <iostream>
#include <cstring>
#include "sched_manage.h"

using namespace std;

// login acc psw
// register acc psw
// show_tasks user id/type/priority/remind/
// add_task name prio type sttimme rdtime
// delete_task user id

int main(int argc, char* argv[])
{
    USERS users;
    string acc;
    string psw;
    GUEST user;
    string name;
    int prio;
    int type;
    string sttime;
    string rdtime;
    int id;
    int check;
    string user_name;
    int max_id;
    if (argc < 2) {
        return -1;
    }
    if (strcmp(argv[1], "login") == 0) {
        acc = argv[2];
        psw = argv[3];
        check = users.check_psw(acc,psw);
        cout << check;
        return 0;
    }
    if (strcmp(argv[1], "register") == 0) {
        acc = argv[2];
        psw = argv[3];
        cout << users.create_user(acc,psw);
        return 0;
    }
    if (strcmp(argv[1], "add_task") == 0) {  
        name = argv[2];
        prio = stoi(argv[3]);
        type = stoi(argv[4]);
        sttime = argv[5];
        rdtime = argv[6];
        user_name = argv[7];
        user = GUEST(user_name);
        max_id = user.get_max_id();
        max_id = max_id + 1;
        id = user.addTask(max_id,name,prio,type,sttime,rdtime);
        cout << id;
        return 0;
    }
    if (strcmp(argv[1], "show_tasks") == 0) {
        user_name = argv[2]; 
        user = GUEST(user_name);
        if (strcmp(argv[3], "id") == 0)
            user.printTask_by_id();
        if (strcmp(argv[3], "priority") == 0)
            user.printTask_by_priority();
        if (strcmp(argv[3], "remind") == 0)
            user.printTask_by_reminder_time();
        if (strcmp(argv[3], "start") == 0)
            user.printTask_by_start_time();
        if (strcmp(argv[3], "type") == 0)
            user.printTask_by_type();
        return 0;
    }
    if (strcmp(argv[1], "delete_task") == 0) {  
        id = stoi(argv[3]);
        user_name = argv[2];
        user = GUEST(user_name);
        id = user.deleteTask(id);
        return 0;
    }
    if (strcmp(argv[1], "check_remind") == 0) {  
        user_name = argv[2];
        user = GUEST(user_name);
        check = user.checktask();
        if (check == 1){
            cout << "MISS" << endl;}
        else if (check == 2){
            cout << "TODO" << endl;}
        return 0;
    }
}
