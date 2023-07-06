CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11

SRCS = sched_main.cpp sched_manage.cpp
OBJS = $(SRCS:.cpp=.o)

all: schedule

schedule: $(OBJS)
	$(CXX) $(CXXFLAGS) $(OBJS) -o $@

sched_main.o: sched_main.cpp sched_manage.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

sched_manage.o: sched_manage.cpp sched_manage.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) schedule
