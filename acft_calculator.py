import time
from datetime import datetime

#global variables w/o input information
admin_arr=[] #Array used to find what times/reps to look for per age/gender
score_arr = []
wait = time.sleep(1)
total = 0 #Total score of points
power_throw_temp = int(0) #Temporary palceholder used incase score falls in between two scores.
pushup_temp = int(0) #Temporary palceholder used incase score falls in between two scores.
plank_score = int(0) #Used to print individual event score
plank_temp = int(0) #Temporary palceholder used incase score falls in between two scores.
plank_temp_time = datetime.strptime("00:00", "%M:%S") #Temporary palceholder used incase score falls in between two scores.
sprint_score = int(0) #Used to print individual event score
sprint_temp = int(0) #Temporary palceholder used incase score falls in between two scores.
sprint_temp_time = datetime.strptime("00:00", "%M:%S") #Temporary palceholder used incase score falls in between two scores.
run_score = int(0) #Used to print individual event score
run_temp = int(0) #Temporary palceholder used incase score falls in between two scores.
run_temp_time = datetime.strptime("00:00", "%M:%S") #Temporary palceholder used incase score falls in between two scores.
i = 0 #Variable used to create admin array, as well as for handling scores in between two scores.

#Intro prompt
print('Welcome to the ACFT Calculater.')
wait
gender=input(r'Graded for Male or Female? m/f: ')
wait
age=int(input('How old are you?: '))

#Ask for specific scores, and retrieve scores per category
#Deadlift lbs, Power Throw, Pushups, Plank, Sprint, Run

deadlift = int(input(r'What was the weight you deadlifted? 200 : '))
wait
power_throw = float(input(r'What was the distance of your Standing Power Throw? 0.0 : '))
wait
pushup = int(input(r'How many push ups did you do?: '))
wait
sprint = datetime.strptime((input(r'What was your Sprint Drag Carry time? MM:SS : ')), "%M:%S")
wait
plank = datetime.strptime((input(r'What was the time on your Plank? MM:SS : ')), "%M:%S")
wait
run = datetime.strptime((input(r'What was your 2-mile run time? MM:SS : ')), "%M:%S")
wait

#Format inputted Age to match admin line from deadlift.txt
if 16<age<22:
    age=1721
elif 22<age<27:
    age=2226
elif 26<age<32:
    age=2731
elif 31<age<37:
    age=3236
elif 36<age<42:
    age=3741
elif 41<age<47:
    age=4246
elif 46<age<52:
    age=4751
elif 51<age<57:
    age=5256
elif 56<age<62:
    age=5761
elif age==62:
    age=62
else:
    print(r'Age is outside of acceptable range\.')

#Format deadlift score to usable score
if gender == 'M' and deadlift <= 80:
    deadlift = 80
elif gender == 'F' and deadlift <= 60:
    deadlift = 60
else:
    deadlift == (int(deadlift/10)*10)

#Error checking gender value
if gender == 'm':
    gender = 'M'
elif  gender == 'f':
    gender = 'F'
elif gender != 'M' or gender != 'F':
    print('Wrong input for gender. Please enter either M or F respectively.')

#Deadlift with Admin
with open('~\Python\acft_raw_plank.txt', 'r') as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        if i == 0:
            admin_arr = (line.split(" "))
            i+=1
        else:
            score_list = []
            score_list.append(line.split(" "))
            score_arr.append(score_list)
    #Create Admin list to use to limit number score options
    index=admin_arr.index(str(age)+gender)
    #Find Points for total for deadlift
    for list in score_arr:
        for score in list:
            if score[index] == str(deadlift):
                total += int(score[0])
                deadlift = int(score[0])
                break
            else:
                continue

#Power Throw with Admin
with open('./acft_raw_power_throw.txt', 'r') as file:
    score_arr = []
    lines = file.readlines()
    i = 0
    for line in lines:
        line.strip()
        if i == 0:
            for item in line:
                admin_arr.append(item)
            i+=1
        else:
            score_list = []
            for word in line:
                score_list.append(line.split(" "))
            score_arr.append(score_list)
    #Find Points for total for power_throw
    for list in score_arr:
        for score in list:    
            if score[index] == '---' or score[index] == '---\n' or power_throw < float(score[index]):
                continue
            elif power_throw == float(score[index]):
                total += int(score[0])
                power_throw = int(score[0])
                break
            elif power_throw > float(score[index]):
                if power_throw_temp < int(score[0]):
                    power_throw_temp = int(score[0])
                    i += 1
                else:
                    continue
                break
        if i > 1:
            if power_throw_temp > power_throw:
                total += power_throw_temp
                power_throw = power_throw_temp


#Pushup
with open('./acft_raw_pushup.txt', 'r') as file:
    score_arr = []
    i = 1
    lines = file.readlines()
    for line in lines:
        line.strip()
        score_list=[]
        for word in line:
            score_list.append(line.split(" "))
        score_arr.append(score_list)
    #Find Points for total for pushup
    for list in score_arr:
        for score in list:
            if score[index] == '---' or score[index]  == '---\n' or pushup < int(score[index]):
                continue
            elif pushup == int(score[index]):
                total += int(score[0])
                pushup = int(score[0])
                break
            elif pushup < int(score[index]):
                continue
            elif pushup > int(score[index]):
                if pushup_temp < int(score[0]):
                    pushup_temp = int(score[0])
                    i += 1
                else:
                    continue
                break
        if i > 1:
            if pushup_temp > pushup:
                total += pushup_temp
                pushup = pushup_temp

#Plank
with open('./acft_raw_plank.txt', 'r') as file:
    score_arr = []
    i = 1
    lines = file.readlines()
    for line in lines:
        line.strip()
        score_list=[]
        for word in line:
            score_list.append(line.split(" "))
        score_arr.append(score_list)
    #Find Points for total for plank
    for list in score_arr:
        for score in list:
            if score[index] == '---' or score[index] == '---\n' or plank < datetime.strptime(score[index], "%M:%S"):
                continue
            elif plank == datetime.strptime(score[index], "%M:%S"):
                total += int(score[0])
                plank_score = int(score[0])
                break
            elif plank > datetime.strptime(score[index], "%M:%S"):
                if plank_temp_time < datetime.strptime(score[index], "%M:%S"):
                    plank_temp_time = datetime.strptime(score[index], "%M:%S")
                    plank_temp = int(score[0])
                    i += 1
                else:
                    continue
                break
        if i > 1:
            if plank_temp > plank_score:
                total += plank_temp
                plank_score = plank_temp

#Sprint
with open('./acft_raw_sprint_drag_carry.txt', 'r') as file:
    score_arr = []
    i = 1
    lines = file.readlines()
    for line in lines:
        line.strip()
        score_list=[]
        for word in line:
            score_list.append(line.split(" "))
        score_arr.append(score_list)
    #Find Points for total for sprint
    for list in score_arr:
        for score in list:
            if score[index] == '---' or score[index] == '---\n' or sprint > datetime.strptime(score[index], "%M:%S"):
                continue
            elif sprint == datetime.strptime(score[index], "%M:%S"):
                total += int(score[0])
                sprint_score = int(score[0])
                break
            elif sprint < datetime.strptime(score[index], "%M:%S"):
                if sprint_temp_time < datetime.strptime(score[index], "%M:%S"):
                    sprint_temp_time = datetime.strptime(score[index], "%M:%S")
                    sprint_temp = int(score[0])
                    i += 1
                else:
                    continue
                break
        if i > 1:
            if sprint_temp > sprint_score:
                total += sprint_temp
                sprint_score = sprint_temp
#Run
with open('./acft_raw_run.txt', 'r') as file:
    score_arr = []
    i = 1
    lines = file.readlines()
    for line in lines:
        line.strip()
        score_list=[]
        for word in line:
            score_list.append(line.split(" "))
        score_arr.append(score_list)
    #Find Points for total for run
    for list in score_arr:
        for score in list:
            if score[index] == '---' or score[index] == '---\n' or run > datetime.strptime(score[index], "%M:%S"):
                continue
            elif run == datetime.strptime(score[index], "%M:%S"):
                total += int(score[0])
                run_score = int(score[0])
                break
            elif run < datetime.strptime(score[index], "%M:%S"):
                if run_temp_time < datetime.strptime(score[index], "%M:%S"):
                    run_temp_time = datetime.strptime(score[index], "%M:%S")
                    run_temp = int(score[0])
                    i += 1
                else:
                    continue
                break
        if i > 1:
            if run_temp > run_score:
                total += run_temp
                run_score = run_temp

#Print scores per category and finally total score and 
# if the individual passed or failed.
print("Your scores for each event are as follows...")
wait
print(f"Deadlift : {deadlift}")
print(f"Power Throw : {power_throw}")
print(f"Push Up : {pushup}")
print(f"Plank : {plank_score}")
print(f"Sprint Drag Carry : {sprint_score}")
print(f"Run : {run_score}")
wait

if deadlift > 70 or power_throw > 70 or pushup > 70 or plank_score > 70 or sprint_score > 70 or run_score > 70:
    if total > 400:
        print(f"You passed the ACFT with a score of {total}")
    else:
        print("You failed the ACFT due to your overall score being less than 400")
else:
    print(f"You failed the ACFT due to not achieveing at least 70 points in each event. Total Score: {total}")