# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\CMake\bin\cmake.exe

# The command to remove a file.
RM = C:\CMake\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build

# Include any dependencies generated for this target.
include CMakeFiles/schedule.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/schedule.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/schedule.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/schedule.dir/flags.make

CMakeFiles/schedule.dir/sched_main.cpp.obj: CMakeFiles/schedule.dir/flags.make
CMakeFiles/schedule.dir/sched_main.cpp.obj: F:/github/NIS1336-SMS/ori_codes/WIN-SOURCES/c_sources/sched_main.cpp
CMakeFiles/schedule.dir/sched_main.cpp.obj: CMakeFiles/schedule.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/schedule.dir/sched_main.cpp.obj"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/schedule.dir/sched_main.cpp.obj -MF CMakeFiles\schedule.dir\sched_main.cpp.obj.d -o CMakeFiles\schedule.dir\sched_main.cpp.obj -c F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_main.cpp

CMakeFiles/schedule.dir/sched_main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/schedule.dir/sched_main.cpp.i"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_main.cpp > CMakeFiles\schedule.dir\sched_main.cpp.i

CMakeFiles/schedule.dir/sched_main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/schedule.dir/sched_main.cpp.s"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_main.cpp -o CMakeFiles\schedule.dir\sched_main.cpp.s

CMakeFiles/schedule.dir/sched_manage.cpp.obj: CMakeFiles/schedule.dir/flags.make
CMakeFiles/schedule.dir/sched_manage.cpp.obj: F:/github/NIS1336-SMS/ori_codes/WIN-SOURCES/c_sources/sched_manage.cpp
CMakeFiles/schedule.dir/sched_manage.cpp.obj: CMakeFiles/schedule.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/schedule.dir/sched_manage.cpp.obj"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/schedule.dir/sched_manage.cpp.obj -MF CMakeFiles\schedule.dir\sched_manage.cpp.obj.d -o CMakeFiles\schedule.dir\sched_manage.cpp.obj -c F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_manage.cpp

CMakeFiles/schedule.dir/sched_manage.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/schedule.dir/sched_manage.cpp.i"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_manage.cpp > CMakeFiles\schedule.dir\sched_manage.cpp.i

CMakeFiles/schedule.dir/sched_manage.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/schedule.dir/sched_manage.cpp.s"
	C:\mingw64\bin\c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\sched_manage.cpp -o CMakeFiles\schedule.dir\sched_manage.cpp.s

# Object files for target schedule
schedule_OBJECTS = \
"CMakeFiles/schedule.dir/sched_main.cpp.obj" \
"CMakeFiles/schedule.dir/sched_manage.cpp.obj"

# External object files for target schedule
schedule_EXTERNAL_OBJECTS =

schedule.exe: CMakeFiles/schedule.dir/sched_main.cpp.obj
schedule.exe: CMakeFiles/schedule.dir/sched_manage.cpp.obj
schedule.exe: CMakeFiles/schedule.dir/build.make
schedule.exe: CMakeFiles/schedule.dir/linkLibs.rsp
schedule.exe: CMakeFiles/schedule.dir/objects1.rsp
schedule.exe: CMakeFiles/schedule.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable schedule.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\schedule.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/schedule.dir/build: schedule.exe
.PHONY : CMakeFiles/schedule.dir/build

CMakeFiles/schedule.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\schedule.dir\cmake_clean.cmake
.PHONY : CMakeFiles/schedule.dir/clean

CMakeFiles/schedule.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build F:\github\NIS1336-SMS\ori_codes\WIN-SOURCES\c_sources\build\CMakeFiles\schedule.dir\DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/schedule.dir/depend
