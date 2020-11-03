#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from taskw import TaskWarrior
w = TaskWarrior()
tasks = w.load_tasks()
tasksPending = (tasks['pending'])
lot = len(tasksPending)

def render_tasks():

  rend = str(lot)
  rend = rend + "|iconName=task-past-due-symbolic-symbolic \n---\n" 
  
  for i in range(len(tasks['pending'])):
            rend = rend + tasks['pending'][i]['description'] + " | bash='task " + str(i+1)  + "'" + '\n'
            # str(tasks['pending'][i]['tags']) +"\n"

  rend = rend + "---\n <span weight='bold'>Zobrazit všechny úkoly</span> | bash='task' iconName=task-past-due-symbolic-symbolic"
  return rend
  

print (render_tasks())
