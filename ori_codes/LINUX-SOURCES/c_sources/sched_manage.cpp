#include "sched_manage.h"



/*----------------------*  TASK  *------------------------*/


string TASK::time_ttos(time_t time)
{
    tm* ptr = localtime(&time);
    char buffer[80];
    //格式化时间
    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", ptr);
    string str(buffer);
    return str;
}

TASK::TASK()
{
    string default_name = "undefine";
    task_name = default_name;
} 

TASK::TASK(int id, string name, int b, int c, time_t a, time_t d)
{
    task_name = name;
    task_id = id;
    start_time = a;
    prio = b;
    type = c;
    remind_time = d;
}

string TASK::type_itos(int type)
{
    switch(type)
    {
        case 1:
            return "学习";
            break;
        case 2:
            return "娱乐";
            break;
        case 3:
            return "生活";
            break;
        default:
            return "others";
    }
}

string TASK::prio_itos(int prio)
{
        switch (prio)
        {
        case 1:
            return "高";
            break;
        case 2:
            return "中";
            break;
        case 3:
            return "低";
            break;
        default:
            return "unknown";
        }
}

string TASK::get_info(void){
    ostringstream oss;
    oss << setw(4)  << left << task_id << " "
        << setw(20) << left << task_name << " "
        << setw(2)  << left << prio << " "
        << setw(2)  << left << type << " "
        << setw(10) << left << start_time << " "
        << setw(10) << left << remind_time << "\n";
    return oss.str();
}

string TASK::print_info(void){
    ostringstream oss;
    oss << setw(4)  << left << task_id << " "
        << setw(10) << left << task_name << " "
        << setw(2)  << left << prio_itos(prio) << " "
        << setw(2)  << left << type_itos(type) << " "
        << setw(19) << left << time_ttos(start_time) << " "
        << setw(19) << left << time_ttos(remind_time) << "\n";
    return oss.str();
}

/*----------------------*  USER  *------------------------*/

int ascii_sum_mod20(string str) {
    int sum = 0;
    for (char c : str) {
        sum += (int)c;
    }
    return sum % 20;
}

string hex_to_str(const string& hex_str)
{
    stringstream ss(hex_str);
    ss >> hex;
    string str;
    unsigned int byte;
    while (ss >> byte) {
        str += static_cast<char>(byte);
    }
    return str;
}

string str_to_hex(const string& str)
{
    stringstream ss;
    ss << hex;
    for (const char& c : str) {
        ss << static_cast<int>(c) << " ";
    }
    return ss.str();
}

USERS::USERS()
{
    users_num = 0;
    check = 0;

    ifstream infile("USERS/users.txt");

    if(infile.good()){
        infile >> users_num;

        for(int i=0; i<users_num; i++)
        {
            infile >> users[i];
        }
    }
    else{
        ofstream outfile("USERS/users.txt");
        outfile << "0" << endl;
        outfile.close();
    }

    infile.close();
}

int USERS::get_users_num()
{
    return users_num;
}

bool USERS::find_user(string user)
{
    for(int i = 0; i < users_num; i++)
    {
        if(users[i] == user)
        {
            return true;
        }
    }
    return false;
}

int USERS::check_psw(string user, string psw)
{
    ifstream infile("USERS/psw.txt");
    if (find_user(user) == false){
        return -2;
    }
    
    if(infile.good()){
        string line;
        while(getline(infile, line))
        {
            size_t pos = line.find_first_of(" ");
            string guest = line.substr(0, pos);
            string cipher = line.substr(pos+1);

            if(user == guest)
            {
                cur_user = user;
                string decrypted_psw = decrypt(user, cipher);
                if(decrypted_psw == psw){
                    srand(time(nullptr));
                    check = rand() % 10000;
                    infile.close();
                    cout << check;
                    return check;
                }
                else{
                    infile.close();
                    return -1;
                }
            }
        }

        infile.close();
        return -2;
    }
    else{
        infile.close();
        return -2;
    }
}

GUEST USERS::read_task(int input_check)
{
    if (input_check == check){
        return GUEST(cur_user);
    } else {
        throw runtime_error("Error: invalid login token.");
    }
}

void USERS::help(void)
{
    cout << "help" << endl;
    return;
}

bool USERS::create_user(string user, string psw)
{
    if (find_user(user))    return false;

    string encrypted_psw = encrypt(user,psw);
    ofstream outfile("USERS/psw.txt", ios::app);
    if(!outfile.good())     return false;
    outfile << user << " " << encrypted_psw << endl;
    outfile.close();

    users_num ++;
    users[users_num-1] = user;

    ofstream userfile("USERS/users.txt", ios::out);
    if(!userfile.good())    return false;
    userfile << users_num << endl;
    for(int i=0; i<users_num-1; i++)
    {
        userfile << users[i] << endl;
    }
    userfile << user << endl;
    userfile.close();
    
    return true;
}

string USERS::encrypt(string user, string psw)
{
    int key = ascii_sum_mod20(user);
    string cipher = psw;
    for (char& c : cipher) {
        c = (char)(c + key);
    }
    cipher = str_to_hex(cipher);
    return cipher;
}

string USERS::decrypt(string user, string cipher)
{
    cipher = hex_to_str(cipher);
    int key = ascii_sum_mod20(user);
    string psw = cipher;
    for (char& c : psw) {
        c = (char)(c - key);
    }
    return psw;
}


/*----------------------*  GUEST  *-----------------------*/

bool priority_compare(TASK a, TASK b){
   return a.get_prio() < b.get_prio();  
}

bool id_compare(TASK a, TASK b){
   return a.get_id() < b.get_id();  
}

bool type_compare(TASK a, TASK b){
   return a.get_type() < b.get_type();  
}

bool start_time_compare(TASK a, TASK b){
   return a.get_start_time() < b.get_start_time();  
}

void GUEST::readTasks_from_file()
{
    string filename = user;
    filename.append(".txt");
    filename.insert(0, "TASKS/");

    ifstream file;
    file.open(filename.c_str());
    if(!file){
        file.open(filename.c_str(), ios::trunc | ios::out); 
    };

    string line;

    int id;
    string name;
    int priority;
    int category;
    unsigned long long start_time;
    unsigned long long remind_time;
    

    // 读取文件每一行
    while (getline(file, line)) 
    {  
        stringstream ss(line);
        ss >> id >> name >> priority >> category >> start_time >> remind_time;
        max_id = max(id,max_id);
        TASK thistask(id, name, priority, category,start_time, remind_time);
        tasks[remind_time] = thistask;
    }
   
    file.close();
    return;
}

GUEST::GUEST(string in_user)
{
    user = in_user;
    readTasks_from_file();
    return;
}

int GUEST::addTask(int id, string name, int priority, int category, string start_time, string remind_time)
{
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        if (thisTask.get_name() == name)    return -1;
    }
    tm timeInfo = {};
    istringstream ss(start_time);
    ss >> get_time(&timeInfo, "%Y-%m-%d %H:%M:%S");
    time_t start = mktime(&timeInfo);

    istringstream rr(remind_time);
    rr >> get_time(&timeInfo, "%Y-%m-%d %H:%M:%S");
    time_t remind = mktime(&timeInfo);

    TASK thistask(id, name, priority, category, start, remind);    
    unsigned long long re = static_cast<unsigned long long>(remind);
    tasks[re] = thistask;
    Save_to_File();
    return thistask.get_id();
}

void GUEST::printTask_by_reminder_time()
{
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        cout << thisTask.print_info();
    }
    return;
}

void GUEST::printTask_by_priority()
{
    vector<TASK> thistasks;
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        thistasks.push_back(thisTask);
    }
    sort(thistasks.begin(), thistasks.end(), priority_compare);
    for (auto pair : thistasks) 
    {
        TASK thisTask = pair;
        cout << thisTask.print_info();
    }
    return;
}

void GUEST::printTask_by_type()
{
    vector<TASK> thistasks;
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        thistasks.push_back(thisTask);
    }
    sort(thistasks.begin(), thistasks.end(), type_compare);
    for (auto pair : thistasks) 
    {
        TASK thisTask = pair;
        cout << thisTask.print_info();
    }
    return;
}

void GUEST::printTask_by_start_time()
{
    vector<TASK> thistasks;
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        thistasks.push_back(thisTask);
    }
    sort(thistasks.begin(), thistasks.end(), start_time_compare);
    for (auto pair : thistasks) 
    {
        TASK thisTask = pair;
        cout << thisTask.print_info();
    }
    return;
}

void GUEST::printTask_by_id()
{
    vector<TASK> thistasks;
    for (auto pair: tasks) 
    {
        TASK thisTask = pair.second;  // task information
        thistasks.push_back(thisTask);
    }
    sort(thistasks.begin(), thistasks.end(), id_compare);
    for (auto pair : thistasks) 
    {
        TASK thisTask = pair;
        cout << thisTask.print_info();
    }
    return;
}

bool GUEST::deleteTask(int id)
{

    for (auto pair = tasks.begin(); pair != tasks.end(); ++pair) 
    {
        TASK thistask = pair->second;  
        if (thistask.get_id() == id) 
        {
            tasks.erase(pair);
            cout << id << " task has been removed" << endl;
            return true;
        }
    }
    cout << id << " task didn't found" << endl;
    Save_to_File();
    return false;
}

void GUEST::Save_to_File()
{
    string filename = user;
    filename.append(".txt");
    filename.insert(0, "TASKS/");
    ofstream file(filename.c_str());
    for (auto p : tasks) {  
        TASK thisTask = p.second;
        file << thisTask.get_info();
    }

    file.close();
    return;
}

GUEST::~GUEST()
{
    Save_to_File();
    return;
}

void GUEST::checktask()
{

    time_t now = time(NULL);
    for (auto it = tasks.begin(); it != tasks.end(); ) 
    {  
        TASK thisTask = it->second; 
        if(now > thisTask.get_remind_time()){
            cout << "MISS:" << thisTask.print_info(); 
            it = tasks.erase(it);  
        }  
        else break;   // 未删除则自增迭代器 
    }
    if (tasks.empty()) 
    {
        cout << "There is no left task now" << endl; 
        return;
    }
    TASK thisTask =  (*tasks.begin()).second;

    if (now == thisTask.get_remind_time())
    {
        cout << "TODO:" << thisTask.print_info();
        int id = thisTask.get_id();
        deleteTask(id);
    }
    return;
}

