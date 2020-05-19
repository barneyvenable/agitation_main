#function to write a zero into a space
def write_zeroes(zero_date_to_write, sensor_data_output_file):
    f=open(sensor_data_output_file, "a+")
    f.write(zero_date_to_write.strftime("%Y-%m-%d %H:00:00,0\n"))
    f.close()
    
#function to write a one into a space
def write_values(value, one_date_to_write, sensor_data_output_file):
    f=open(sensor_data_output_file, "a+")
    date_to_write = one_date_to_write.strftime("%Y-%m-%d %H:00:00,")
    f.write(str(date_to_write) + str(value) + "\n")
    f.close()

    
    
#main
#creates various files which isolate data entries for each sensor
def all_sensors_per_hour():    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    warnings.filterwarnings('ignore')
    
    #reads in activity_total
    dataset = pd.read_csv('activity_total.csv')
    
    #REVERT SENSOR PER HOUR TO BE UNCOMMENTED LATER
    #creates a new ‘*location*_only.csv’ file to isolate the movement
    if dataset[dataset.location == 'pir-hallway'].shape[0] == 0 : #if the file is empty, keep '__only' file empty
        open('pir-hallway_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('pir-hallway_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'pir-hallway'].to_csv('pir-hallway_only.csv', encoding='utf-8', index=False)
    file1 = 'pir-hallway_only.csv'
    file2 = 'pir-hallway_only_output.csv'
    sensor_per_hour(file1, file2)
    
    if dataset[dataset.location == 'pir-living room'].shape[0] == 0 :
        open('pir-living_room_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('pir-living_room_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'pir-living room'].to_csv('pir-living_room_only.csv', encoding='utf-8', index=False)
    file1 = 'pir-living_room_only.csv'
    file2 = 'pir-living_room_only_output.csv'
    sensor_per_hour(file1, file2)

    if dataset[dataset.location == 'motion-bathroom'].shape[0] == 0 :
        open('motion-bathroom_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('motion-bathroom_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'motion-bathroom'].to_csv('motion-bathroom_only.csv', encoding='utf-8', index=False)
    file1 = 'motion-bathroom_only.csv'
    file2 = 'motion-bathroom_only_output.csv'
    sensor_per_hour(file1, file2)
    
    if dataset[dataset.location == 'motion-bedroom'].shape[0] == 0 :
        open('motion-bedroom_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('motion-bedroom_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'motion-bedroom'].to_csv('motion-bedroom_only.csv', encoding='utf-8', index=False)
    file1 = 'motion-bedroom_only.csv'
    file2 = 'motion-bedroom_only_output.csv'
    sensor_per_hour(file1, file2)
    
    if dataset[dataset.location == 'motion-kitchen'].shape[0] == 0 :
        open('motion-kitchen_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('motion-kitchen_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'motion-kitchen'].to_csv('motion-kitchen_only.csv', encoding='utf-8', index=False)
    file1 = 'motion-kitchen_only.csv'
    file2 = 'motion-kitchen_only_output.csv'
    sensor_per_hour(file1, file2)
    
    if dataset[dataset.location == 'door-front door'].shape[0] == 0 :
        open('door-front_door_only.csv', 'w').close() #clear sensors_collated.csv
        f=open('door-front_door_only.csv', "a+")
        f.write('datetime,element,location,value,date,time\n')
        f.close()
    else :
        dataset[dataset.location == 'door-front door'].to_csv('door-front_door_only.csv', encoding='utf-8', index=False)
    file1 = 'door-front_door_only.csv'
    file2 = 'door-front_door_only_output.csv'
    sensor_per_hour(file1, file2)
    
    file1 = 'bed_total.csv'
    file2 = 'bed_total_output.csv'
    sensor_per_hour(file1, file2)
    
    file1 = 'chair_total.csv'
    file2 = 'chair_total_output.csv'
    sensor_per_hour(file1, file2)
    
    
    #collate sensors has already been done for all files.
    #collate_sensors()
    
    
    
#currently just puts a 1 if they've been in the bed that hour, and a zero if not
def bed_chair_sensor_per_hour(sensor_data_input_file, sensor_data_output_file):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    from calendar import monthrange
    from datetime import datetime, timedelta

    dataset = pd.read_csv(sensor_data_input_file) #read text file into dataset

    first_date = datetime.strptime(dataset.loc[0, 'datetime'], "%Y-%m-%d %H:%M:%S") #retrieve the first date in the file
    prev_date = first_date

    open(sensor_data_output_file, 'w').close() #clears output file
    
    f=open(sensor_data_output_file, "a+")
    f.write('time_period,instances\n')
    f.close()
    
    #for i indexing through every line in the file
    for i in range(0, len(dataset)):
        if i == 0 :
            current_date = datetime.strptime(dataset.loc[i, 'datetime'], "%Y-%m-%d %H:%M:%S") #picks up the date on that line of the file
            current_value = dataset.loc[i, 'value']
        prev_date = current_date
        prev_value = current_value
        current_date = datetime.strptime(dataset.loc[i, 'datetime'], "%Y-%m-%d %H:%M:%S") #picks up the date on that line of the file
        current_value = dataset.loc[i, 'value']
        
        if i == 0 : #registers the first entry into the output file
                write_values(1, current_date, sensor_data_output_file)
                prev_date = current_date #stops prev_date, above, picking up value for last run's current date
            
        current_concat=current_date.strftime("%Y-%m-%d %H")
        prev_concat=prev_date.strftime("%Y-%m-%d %H")
    
        sweep_date = prev_date
        sweep_concat = prev_concat
        
        i=0
        #sweeping through from prev date to current date and inserting either zeroes or ones depending on the most recent 'value'
        while ((sweep_concat != current_concat) and (i < 20000)): #failsafe to stop it continuing forever
            if i > 0:
                if prev_value == -1 :
                    write_zeroes(sweep_date, sensor_data_output_file)
                else :
                    write_values(1, sweep_date, sensor_data_output_file)
            i+=1
            sweep_date += timedelta(hours=1)
            sweep_concat = sweep_date.strftime("%Y-%m-%d %H")
            #print(sweep_concat)
    
        if current_concat != prev_concat:
            write_values(1, current_date, sensor_data_output_file)   
            
    

    
    
    
    
#reads input file and returns a file with one value per hour from the first entry to the last
def sensor_per_hour(sensor_data_input_file, sensor_data_output_file):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    from calendar import monthrange
    from datetime import datetime, timedelta
    
            
    no_same_date = 0 # initialise no_same_date as 1
    dataset = pd.read_csv(sensor_data_input_file) #read text file into dataset
            
    open(sensor_data_output_file, 'w').close() #clears output file
    f=open(sensor_data_output_file, "a+")
    f.write('time_period,instances\n')
    f.close()
        
    if len(dataset) > 0 :
        first_date = datetime.strptime(dataset.loc[0, 'datetime'], "%Y-%m-%d %H:%M:%S") #retrieve the first date in the file
        prev_date = first_date

        #for i indexing through every line in the file
        #change i for testing purposes!
        #for i in range(0, 200): 
        for i in range(0, len(dataset)):                 
            if (i == 0) :
                current_date = datetime.strptime(dataset.loc[i, 'datetime'], "%Y-%m-%d %H:%M:%S") #picks up the date on that line of the file

            prev_date = current_date
            #prev date is 19
            current_date = datetime.strptime(dataset.loc[i, 'datetime'], "%Y-%m-%d %H:%M:%S") #picks up the date on that line of the file
            #current date is 19

            if (i == 0) : #registers the first entry into the output file
                prev_date = current_date #stops prev_date, above, picking up value for last run's current date

            current_concat=current_date.strftime("%Y-%m-%d %H")
            #current concat is 5
            prev_concat=prev_date.strftime("%Y-%m-%d %H")
            #prev concat is 19

            sweep_date = prev_date
            #sweep date is 19
            sweep_concat = prev_concat
            #sweep concat is 19


            #if its a new hour, set number of that date to 1
            if current_concat != prev_concat:
                write_values(no_same_date, prev_date, sensor_data_output_file) # write previous date
                no_same_date = 1 #number with that date = 1
            #if its the same hour
            elif current_concat == prev_concat:
                no_same_date = no_same_date + 1


            j=0
            #while the sweep date still hasn't found the current date, keep inserting zeroes
            #sweeping through from prev date to current date and...
            while ((sweep_concat != current_concat) and (j < 20000)): #failsafe to stop it continuing forever
                if j > 0:
                    write_zeroes(sweep_date, sensor_data_output_file)
                j+=1
                sweep_date += timedelta(hours=1)
                sweep_concat = sweep_date.strftime("%Y-%m-%d %H")
                #print(sweep_concat)

            #to ensure final date is written at end
            if i == (len(dataset) - 1) :
                write_values(no_same_date, current_date, sensor_data_output_file)
    
    else : #write an arbitraty date with value 0, in the case that the file was empty
        f=open(sensor_data_output_file, "a+")
        dummy_date = datetime.strptime("2017-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        f.write(str(dummy_date) + ",0\n")
        f.close()
    
            
        
        
        
        
def collate_sensors():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    from calendar import monthrange
    from datetime import datetime, timedelta
    
    
    #can't think of a way to do this without writing it out, since datasets won't pass in a 
    #all this repetitive mess could probably be tidied up somewhere down the line

    #create arrays for each sensor,for the dates of their starts and ends
    d_start = [0,0,0,0,0,0,0,0,0]
    d_end = [0,0,0,0,0,0,0,0,0]
    diff_start = [0,0,0,0,0,0,0,0,0]
    diff_end = [0,0,0,0,0,0,0,0,0]
    
    
    #could probably make more efficient by making multiple dataframes or an array of them (but initially didn't know how to do)
    
    dataset_1 = pd.read_csv('pir-hallway_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    #returns 2nd line of file since no deadings given but don't mind for now since we're only getting a date
    d_start[1] = datetime.strptime(dataset_1.iloc[0,0], "%Y-%m-%d %H:%M:%S") #start date is the first date in file
    d_end[1] = datetime.strptime(dataset_1.iloc[len(dataset_1)-1,0], "%Y-%m-%d %H:%M:%S") #end date of file
    diff_start[1] = abs((d_start[1] - ref_date).days) #no days between arbitrary reference date and start date
    diff_end[1] = abs((d_end[1] - ref_date).days) #no days between arbitrary reference date and end date
    #print(diff_start[1])
    #print(diff_end[1])
    #print(d_start[1])
    #print(d_end[1])
        
    dataset_2 = pd.read_csv('pir-living_room_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[2] = datetime.strptime(dataset_2.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[2] = datetime.strptime(dataset_2.iloc[len(dataset_2)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[2] = abs((d_start[2] - ref_date).days)
    diff_end[2] = abs((d_end[2] - ref_date).days)
    #print(diff_start[2])
    #print(diff_end[2])
    #print(d_start[2])
    #print(d_end[2])
    
    dataset_3 = pd.read_csv('motion-bathroom_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[3] = datetime.strptime(dataset_3.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[3] = datetime.strptime(dataset_3.iloc[len(dataset_3)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[3] = abs((d_start[3] - ref_date).days)
    diff_end[3] = abs((d_end[3] - ref_date).days)
    #print(diff_start[3])
    #print(diff_end[3])
    #print(d_start[3])
    #print(d_end[3])
    
    dataset_4 = pd.read_csv('motion-bedroom_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[4] = datetime.strptime(dataset_4.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[4] = datetime.strptime(dataset_4.iloc[len(dataset_4)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[4] = abs((d_start[4] - ref_date).days)
    diff_end[4] = abs((d_end[4] - ref_date).days)
    #print(diff_start[4])
    #print(diff_end[4])
    #print(d_start[4])
    #print(d_end[4])

    dataset_5 = pd.read_csv('motion-kitchen_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[5] = datetime.strptime(dataset_5.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[5] = datetime.strptime(dataset_5.iloc[len(dataset_5)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[5] = abs((d_start[5] - ref_date).days)
    diff_end[5] = abs((d_end[5] - ref_date).days)
    #print(diff_start[5])
    #print(diff_end[5])
    #print(d_start[5])
    #print(d_end[5])
    
    dataset_6 = pd.read_csv('door-front_door_only_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[6] = datetime.strptime(dataset_6.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[6] = datetime.strptime(dataset_6.iloc[len(dataset_6)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[6] = abs((d_start[6] - ref_date).days)
    diff_end[6] = abs((d_end[6] - ref_date).days)
    #print(diff_start[6])
    #print(diff_end[6])
    #print(d_start[6])
    #print(d_end[6])
    
    dataset_7 = pd.read_csv('bed_total_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[7] = datetime.strptime(dataset_7.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[7] = datetime.strptime(dataset_7.iloc[len(dataset_7)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[7] = abs((d_start[7] - ref_date).days)
    diff_end[7] = abs((d_end[7] - ref_date).days)
    #print(diff_start[7])
    #print(diff_end[7])
    #print(d_start[7])
    #print(d_end[7])
    
    dataset_8 = pd.read_csv('chair_total_output.csv')
    ref_date = datetime.strptime("2010-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    d_start[8] = datetime.strptime(dataset_8.iloc[0,0], "%Y-%m-%d %H:%M:%S")
    d_end[8] = datetime.strptime(dataset_8.iloc[len(dataset_8)-1,0], "%Y-%m-%d %H:%M:%S")
    diff_start[8] = abs((d_start[8] - ref_date).days)
    diff_end[8] = abs((d_end[8] - ref_date).days)
    #print(diff_start[8])
    #print(diff_end[8])
    #print(d_start[8])
    #print(d_end[8])
    #print("ok")

    
    #go through each sensor's start date, working out which date comes *FIRST*
    start_date = d_start[1]
    start_diff = diff_start[1]
    for i in range(1, 8):
        #print(start_date)
        #print("Start date:" + str(d_start[i]))
        #print(i)
        if diff_start[i+1] < diff_start[i]: #if date is earlier than previous one
            start_date = d_start[i+1]
            start_diff = diff_start[i+1]
    #print("start date is: " + str(start_date))
    #print("start diff is: " + str(start_diff))

    start_date = start_date.strftime("%Y-%m-%d 00:00:00") #begin at start of that day = start date!
    #print(i)
    #print(start_date)
            
    #obtain end date - from date which comes *LAST*
    end_date = d_end[1]
    end_diff = diff_end[1]
    #print("end date is: " + str(end_date))
    for i in range(1, 8):
        if diff_end[i+1] > end_diff: #logic: we're trying to find the biggest end_diff, and assign that dataset's latest date to the end_date
            end_date = d_end[i+1]
            end_diff = diff_end[i+1]
            #print("end date is: " + str(end_date))
    #print("end date is: " + str(end_date))
    #print("end diff is: " + str(end_diff))
    end_date = end_date.strftime("%Y-%m-%d 23:00:00") #end at end of that day - end date!
    #print(end_date)
    
    #UPDATE - not going to work...
    #create trackers for the positions of the chosen start date in each sensor's file
    tracker = [0,0,0,0,0,0,0,0]
    #tracker = [x+1 for x in tracker] #increment tracker

    
    #UPDATE - deleted section which indexes location of start date in files
    #TODO - BIG ISSUE - start dates are nowhere to be seen in these documents - SO now we're going through
    #find start values of each sensor file
    i=1
    
                    
            
    #added j=0 as a potential fix??
    #j=0        
        
    #NEW start_end_diff
    start_end_diff = end_diff - start_diff
    
    
    
    
    open('sensors_collated.csv', 'w').close() #clear sensors_collated.csv
    f=open('sensors_collated.csv', "a+")
    f.write('date_hour,pir-hallway,pir-living_room,motion-bathroom,motion-bedroom,motion-kitchen,door-front_door,bed_total,chair_total\n')
    f.close()
    
    
    #INSTEAD - while start date is not equal to end date
    i=0
    tracker = [0,0,0,0,0,0,0,0]
    sweep_date = start_date
    sweep_date = datetime.strptime(sweep_date, "%Y-%m-%d %H:%M:%S")
    #print("sweep date is: " + str(sweep_date))
    #print("end date is: " + str(end_date))
    while str(sweep_date) != end_date: #going through all dates from start to end (technically misses out the 23:00 hour)
        sensor_to_collate = [0,0,0,0,0,0,0,0] #the ouput for each hour
        j=0
        for dataset_sweep in (dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6, dataset_7, dataset_8): #for each sensor
            #print("sweep date: " + str(sweep_date))
            
            if tracker[j] < len(dataset_sweep): #if we haven't exceeded the length of the dataset
                #print(str(tracker[j]) + "th location in dataset " + str(j+1) + ": " + str(dataset_sweep.iloc[tracker[j],0])) 
            
                if str(dataset_sweep.iloc[tracker[j],0]) == str(sweep_date): #if that file's row line is the sweep date
                    sensor_to_collate[j] = dataset_sweep.iloc[tracker[j],1] #puts number of sensor readings for that time in the array
                    #print("MATCH!")
                    tracker[j] = tracker[j] + 1
                else:
                    sensor_to_collate[j] = 0  
            #else:
                #print("EoF reached")
           
            j=j+1
        #print(sensor_to_collate) #not working
        #print(tracker)
        
        #write to sensors_collated_file
        f=open('sensors_collated.csv', "a+")
        f.write(str(sweep_date) + "," + str(sensor_to_collate[0]) + "," + str(sensor_to_collate[1]) + "," + str(sensor_to_collate[2]) + "," + str(sensor_to_collate[3]) + "," + str(sensor_to_collate[4]) + "," + str(sensor_to_collate[5]) + "," + str(sensor_to_collate[6]) + "," +  str(sensor_to_collate[7]) + "\n") #write all the data to a line in the file
        f.close()
        
        sweep_date += timedelta(hours=1) #increments for the next hour

        #print("sweep date is: " + str(sweep_date))
        #print sensor_to_collate in file with the sweep_date
        
        #print("\n")
    
            
        
    

        
def create_df():
    df = pd.read_csv('sensors_collated.csv')
    
       
def get_flags_data_setup():
    
    #clear output file before we start
    open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags.csv", 'w').close()
    open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_false.csv", 'w').close()
    open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_true.csv", 'w').close()
    
    #set up the results file before iterating through each patient folder - this is now in the main location, in Individual Project, meaning that regardless of which folder we're in, it will add to this file
    f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags.csv", "a+")
    f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
    f.close()
    
    f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_true.csv", "a+")
    f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
    f.close()
    
    f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_false.csv", "a+")
    f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
    f.close()
    
    
        
        
#creates datasets of data up preceding an instance of a detected positive.
#[should probably run and be passed values to check but can edit that in later]
#flags being an instance of flagged/labelled data
def get_flags_data():
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    import time
    start_time = time.time()

    
    #read in file with flags
    flags_data = pd.read_csv('flags_total.csv')
    sensors_collated_df = pd.read_csv('sensors_collated.csv')
    #print(str(sensors_collated_df.iloc[0,0]))
    
    check_location = 0
    
    #for all the flags:
    for i in range(0, len(flags_data)):
        #print(flags_data.iloc[i,2])
        #if it's an instance of agitation
        if (flags_data.iloc[i,1] == 'tihm-agitation'):
            flags_datetime = flags_data.iloc[i,0] #string 
            
            if len(flags_datetime) > 19 : #if the string is longer than the standard format (should be 19 chars)
                num_to_cut = len(flags_datetime) - 19 #determine the number to cut off the end
                flags_datetime = flags_datetime[:-num_to_cut] #string - concatented
            
            flags_datetime = datetime.strptime(flags_datetime, "%Y-%m-%d %H:%M:%S") #datetime - converted to datetime
            flags_datetime = flags_datetime.strftime("%Y-%m-%d %H:00:00") #string
            print(str(flags_datetime))
            flags_datetime = str(flags_datetime)
            flags_value = flags_data.iloc[i,2]
            
            #irrelevant since we're writing straight to the Individual Project folder
            open('sensor_values_for_flags.csv', 'w').close()
            f=open('sensor_values_for_flags.csv', "a+")
            f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
            f.close()
            
            open('sensor_values_for_flags_true.csv', 'w').close()
            f=open('sensor_values_for_flags_true.csv', "a+")
            f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
            f.close()
            
            open('sensor_values_for_flags_false.csv', 'w').close()
            f=open('sensor_values_for_flags_false.csv', "a+")
            f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
            f.close()
            
            
            #find that time instance in sensors_collated file data
            for i in range(check_location, len(sensors_collated_df)):
                #print(flags_datetime)
                #print(sensors_collated_df.loc[i, 'date_hour'])
                if (sensors_collated_df.loc[i, 'date_hour'] == flags_datetime):
                    print(str(flags_datetime) + "," + str(flags_value) + " and i = " + str(i))
                    check_location = i
                    
                    print(str(flags_value))
                    
                    #os.chdir(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project")
                    #cwd = os.getcwd() #gets current location
                    #print("Location: " + str(cwd))
                    
                    #print(sensors_collated_df.iloc[i,1])
                    #save value of i for next search 
                    
                    #print sensor results to a file
                    f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags.csv", "a+")
                    f.write(str(flags_datetime) + "," + str(flags_value) + "," + str(sensors_collated_df.iloc[i-1,1]) + "," + str(sensors_collated_df.iloc[i-1,2]) + "," + str(sensors_collated_df.iloc[i-1,3]) + "," + str(sensors_collated_df.iloc[i-1,4]) + "," + str(sensors_collated_df.iloc[i-1,5]) + "," + str(sensors_collated_df.iloc[i-1,6]) + "," + str(sensors_collated_df.iloc[i-1,7]) + "," + str(sensors_collated_df.iloc[i-1,8]) + "," + str(sensors_collated_df.iloc[i-2,1]) + "," + str(sensors_collated_df.iloc[i-2,2]) + "," + str(sensors_collated_df.iloc[i-2,3]) + "," + str(sensors_collated_df.iloc[i-2,4]) + "," + str(sensors_collated_df.iloc[i-2,5]) + "," + str(sensors_collated_df.iloc[i-2,6]) + "," + str(sensors_collated_df.iloc[i-2,7]) + "," + str(sensors_collated_df.iloc[i-2,8]) + "," + str(sensors_collated_df.iloc[i-3,1]) + "," + str(sensors_collated_df.iloc[i-3,2]) + "," + str(sensors_collated_df.iloc[i-3,3]) + "," + str(sensors_collated_df.iloc[i-3,4]) + "," + str(sensors_collated_df.iloc[i-3,5]) + "," + str(sensors_collated_df.iloc[i-3,6]) + "," + str(sensors_collated_df.iloc[i-3,7]) + "," + str(sensors_collated_df.iloc[i-3,8]) + "\n") #write all the data to a line in the file
                    f.close()
                    
                    if (flags_value == 1) :
                        f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_true.csv", "a+")
                        f.write(str(flags_datetime) + "," + str(flags_value) + "," + str(sensors_collated_df.iloc[i-1,1]) + "," + str(sensors_collated_df.iloc[i-1,2]) + "," + str(sensors_collated_df.iloc[i-1,3]) + "," + str(sensors_collated_df.iloc[i-1,4]) + "," + str(sensors_collated_df.iloc[i-1,5]) + "," + str(sensors_collated_df.iloc[i-1,6]) + "," + str(sensors_collated_df.iloc[i-1,7]) + "," + str(sensors_collated_df.iloc[i-1,8]) + "," + str(sensors_collated_df.iloc[i-2,1]) + "," + str(sensors_collated_df.iloc[i-2,2]) + "," + str(sensors_collated_df.iloc[i-2,3]) + "," + str(sensors_collated_df.iloc[i-2,4]) + "," + str(sensors_collated_df.iloc[i-2,5]) + "," + str(sensors_collated_df.iloc[i-2,6]) + "," + str(sensors_collated_df.iloc[i-2,7]) + "," + str(sensors_collated_df.iloc[i-2,8]) + "," + str(sensors_collated_df.iloc[i-3,1]) + "," + str(sensors_collated_df.iloc[i-3,2]) + "," + str(sensors_collated_df.iloc[i-3,3]) + "," + str(sensors_collated_df.iloc[i-3,4]) + "," + str(sensors_collated_df.iloc[i-3,5]) + "," + str(sensors_collated_df.iloc[i-3,6]) + "," + str(sensors_collated_df.iloc[i-3,7]) + "," + str(sensors_collated_df.iloc[i-3,8]) + "\n") #write all the data to a line in the file
                        f.close()
                    else :
                        f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\sensor_values_for_flags_false.csv", "a+")
                        f.write(str(flags_datetime) + "," + str(flags_value) + "," + str(sensors_collated_df.iloc[i-1,1]) + "," + str(sensors_collated_df.iloc[i-1,2]) + "," + str(sensors_collated_df.iloc[i-1,3]) + "," + str(sensors_collated_df.iloc[i-1,4]) + "," + str(sensors_collated_df.iloc[i-1,5]) + "," + str(sensors_collated_df.iloc[i-1,6]) + "," + str(sensors_collated_df.iloc[i-1,7]) + "," + str(sensors_collated_df.iloc[i-1,8]) + "," + str(sensors_collated_df.iloc[i-2,1]) + "," + str(sensors_collated_df.iloc[i-2,2]) + "," + str(sensors_collated_df.iloc[i-2,3]) + "," + str(sensors_collated_df.iloc[i-2,4]) + "," + str(sensors_collated_df.iloc[i-2,5]) + "," + str(sensors_collated_df.iloc[i-2,6]) + "," + str(sensors_collated_df.iloc[i-2,7]) + "," + str(sensors_collated_df.iloc[i-2,8]) + "," + str(sensors_collated_df.iloc[i-3,1]) + "," + str(sensors_collated_df.iloc[i-3,2]) + "," + str(sensors_collated_df.iloc[i-3,3]) + "," + str(sensors_collated_df.iloc[i-3,4]) + "," + str(sensors_collated_df.iloc[i-3,5]) + "," + str(sensors_collated_df.iloc[i-3,6]) + "," + str(sensors_collated_df.iloc[i-3,7]) + "," + str(sensors_collated_df.iloc[i-3,8]) + "\n") #write all the data to a line in the file
                        f.close()
                    
                    
            #not necessary...        
            #should probably do search of sensors_collated from this date
            #datetimes are same format so can go ahead        
            
                
            #copy contents of sensor_values_for_flags.csv into previous directory...
            #in another part of code, clear that file.
            
            
            #copied - code to have multiple dataframes 
#             dates_list = [dt.datetime(2015,11,i+1) for i in range(3)]
#             month_day_list = [d.strftime("%m%d") for d in dates_list]

#             dataframe_collection = {} 

#             for month_day in month_day_list:
#                 new_data = np.random.rand(3,3)
#                 dataframe_collection[month_day] = pd.DataFrame(new_data, columns=["one", "two", "three"])

#             for key in dataframe_collection.keys():
#                 print("\n" +"="*40)
#                 print(key)
#                 print("-"*40)
#                 print(dataframe_collection[key])
            #copied end
              
    
    #times the search
    print("--- Search took %s seconds ---" % (time.time() - start_time))
    

    
    
def shuffle_sensor_values_for_flags():
    import pandas as pd
    import random
    from sklearn.utils import shuffle

    #shuffle the data by putting all lines in a random order into another file
    sensor_values_for_flags_true = pd.read_csv('sensor_values_for_flags_true_pre_shuffle.csv') #reading from a baseline file now, for upsampled data
    sensor_values_for_flags_false = pd.read_csv('sensor_values_for_flags_false.csv')
    sensor_values_for_flags = pd.read_csv('sensor_values_for_flags.csv')
    
    #Shuffle dataset
    sensor_values_for_flags_true = shuffle(sensor_values_for_flags_true)
    sensor_values_for_flags_false = shuffle(sensor_values_for_flags_false)
    sensor_values_for_flags = shuffle(sensor_values_for_flags)
    
    #sometime wasn't shuffling whole rows?
    #sensor_values_for_flags_true = sensor_values_for_flags_true.sample(frac=1)
    #sensor_values_for_flags_false = sensor_values_for_flags_false.sample(frac=1)
    #sensor_values_for_flags = sensor_values_for_flags.sample(frac=1)

    sensor_values_for_flags_true.to_csv('sensor_values_for_flags_true.csv', encoding='utf-8', header=True, index=False)
    #for i in range (0, 11): #oversamples it by writing it a load
    #    sensor_values_for_flags_true.to_csv('sensor_values_for_flags_true.csv', mode='a', header=False, encoding='utf-8', index=False)
    
    sensor_values_for_flags_false.to_csv('sensor_values_for_flags_false.csv', encoding='utf-8', index=False)
    sensor_values_for_flags.to_csv('sensor_values_for_flags.csv', encoding='utf-8', index=False)

    #print("Sensor values for flags data shuffled")
    
    

    
def prepare_data_for_algorithm(no_sensors, balance, no_flags_to_use):
    from datetime import datetime, timedelta
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    import os
    from os import listdir
    import random
    import time
    start_time = time.time()

    os.chdir(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project")
    flagged_dataset_true = pd.read_csv('sensor_values_for_flags_true.csv')
    flagged_dataset_false = pd.read_csv('sensor_values_for_flags_false.csv')
    flagged_dataset = pd.read_csv('sensor_values_for_flags.csv')
    
    test_sample_max = 100
    test_sample_count = 1
    
    
        


    open('algorithm_data.csv', 'w').close()
    f=open('algorithm_data.csv', "a+")
    f.write('datetime_for_agitation_flag,flag_value,pir-hallway-1,pir-living_room-1,motion-bathroom-1,motion-bedroom-1,motion-kitchen-1,door-front_door-1,bed_total-1,chair_total-1,pir-hallway-2,pir-living_room-2,motion-bathroom-2,motion-bedroom-2,motion-kitchen-2,door-front_door-2,bed_total-2,chair_total-2,pir-hallway-3,pir-living_room-3,motion-bathroom-3,motion-bedroom-3,motion-kitchen-3,door-front_door-3,bed_total-3,chair_total-3\n')
    f.close()
    
    #prepare algorithm_data file - write all sensor headings regardless
    
    
    
    
    #instead of writing line by line to a text file, can we create a new dataset then write the whole thing to a file?
    
    #algorithm_dataset = pd.DataFrame(columns=['datetime_for_agitation_flag','flag_value','pir-hallway-1','pir-living_room-1','motion-bathroom-1','motion-bedroom-1','motion-kitchen-1','door-front_door-1','bed_total-1','chair_total-1'])
    #print(algorithm_dataset)
    
    #Works but takes longer
    #start_time = time.time()
    #for i in range(0, 100) :
    #    algorithm_dataset.loc[2*i] = flagged_dataset_true.iloc[i]
    #    algorithm_dataset.loc[2*i+1] = flagged_dataset_false.iloc[i]
    #algorithm_dataset.to_csv('algorithm_dataset.csv', encoding='utf-8', index=False
    #print("--- Dataset sort took %s seconds ---" % (time.time() - start_time))

    
    #selects data to be used - may be able to be done by some scikit learn code though
    #determines the number of samples to be used
    #just takes the top 50 lines from alternating true and false files (already shuffled) 
    
    if (balance == 'balanced') :
        #start_time = time.time()
        for i in range(0, int(no_flags_to_use/2)) :
            if (no_sensors == 8) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset_true.iloc[i,0]) + "," + str(flagged_dataset_true.iloc[i,1]) + "," + str(flagged_dataset_true.iloc[i,2]) + "," + str(flagged_dataset_true.iloc[i,3]) + "," + str(flagged_dataset_true.iloc[i,4]) + "," + str(flagged_dataset_true.iloc[i,5]) + "," + str(flagged_dataset_true.iloc[i,6]) + "," + str(flagged_dataset_true.iloc[i,7]) + "," + str(flagged_dataset_true.iloc[i,8]) + "," + str(flagged_dataset_true.iloc[i,9]) + "\n")

                f.write(str(flagged_dataset_false.iloc[i,0]) + "," + str(flagged_dataset_false.iloc[i,1]) + "," + str(flagged_dataset_false.iloc[i,2]) + "," + str(flagged_dataset_false.iloc[i,3]) + "," + str(flagged_dataset_false.iloc[i,4]) + "," + str(flagged_dataset_false.iloc[i,5]) + "," + str(flagged_dataset_false.iloc[i,6]) + "," + str(flagged_dataset_false.iloc[i,7]) + "," + str(flagged_dataset_false.iloc[i,8]) + "," + str(flagged_dataset_false.iloc[i,9]) + "\n")

                f.close()
                #FOR NOW we just want the last 1 hour of data and to look at recall and accuracy for that 

            elif (no_sensors == 16) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset_true.iloc[i,0]) + "," + str(flagged_dataset_true.iloc[i,1]) + "," + str(flagged_dataset_true.iloc[i,2]) + "," + str(flagged_dataset_true.iloc[i,3]) + "," + str(flagged_dataset_true.iloc[i,4]) + "," + str(flagged_dataset_true.iloc[i,5]) + "," + str(flagged_dataset_true.iloc[i,6]) + "," + str(flagged_dataset_true.iloc[i,7]) + "," + str(flagged_dataset_true.iloc[i,8]) + "," + str(flagged_dataset_true.iloc[i,9]) + "," + str(flagged_dataset_true.iloc[i,10]) + "," + str(flagged_dataset_true.iloc[i,11]) + "," + str(flagged_dataset_true.iloc[i,12]) + "," + str(flagged_dataset_true.iloc[i,13]) + "," + str(flagged_dataset_true.iloc[i,14]) + "," + str(flagged_dataset_true.iloc[i,15]) + "," + str(flagged_dataset_true.iloc[i,16]) + "," + str(flagged_dataset_true.iloc[i,17]) + "\n")

                f.write(str(flagged_dataset_false.iloc[i,0]) + "," + str(flagged_dataset_false.iloc[i,1]) + "," + str(flagged_dataset_false.iloc[i,2]) + "," + str(flagged_dataset_false.iloc[i,3]) + "," + str(flagged_dataset_false.iloc[i,4]) + "," + str(flagged_dataset_false.iloc[i,5]) + "," + str(flagged_dataset_false.iloc[i,6]) + "," + str(flagged_dataset_false.iloc[i,7]) + "," + str(flagged_dataset_false.iloc[i,8]) + "," + str(flagged_dataset_false.iloc[i,9]) + "," + str(flagged_dataset_false.iloc[i,10]) + "," + str(flagged_dataset_false.iloc[i,11]) + "," + str(flagged_dataset_false.iloc[i,12]) + "," + str(flagged_dataset_false.iloc[i,13]) + "," + str(flagged_dataset_false.iloc[i,14]) + "," + str(flagged_dataset_false.iloc[i,15]) + "," + str(flagged_dataset_false.iloc[i,16]) + "," + str(flagged_dataset_false.iloc[i,17]) + "\n")

                f.close()

            elif (no_sensors == 24) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset_true.iloc[i,0]) + "," + str(flagged_dataset_true.iloc[i,1]) + "," + str(flagged_dataset_true.iloc[i,2]) + "," + str(flagged_dataset_true.iloc[i,3]) + "," + str(flagged_dataset_true.iloc[i,4]) + "," + str(flagged_dataset_true.iloc[i,5]) + "," + str(flagged_dataset_true.iloc[i,6]) + "," + str(flagged_dataset_true.iloc[i,7]) + "," + str(flagged_dataset_true.iloc[i,8]) + "," + str(flagged_dataset_true.iloc[i,9]) + "," + str(flagged_dataset_true.iloc[i,10]) + "," + str(flagged_dataset_true.iloc[i,11]) + "," + str(flagged_dataset_true.iloc[i,12]) + "," + str(flagged_dataset_true.iloc[i,13]) + "," + str(flagged_dataset_true.iloc[i,14]) + "," + str(flagged_dataset_true.iloc[i,15]) + "," + str(flagged_dataset_true.iloc[i,16]) + "," + str(flagged_dataset_true.iloc[i,17]) + "," + str(flagged_dataset_true.iloc[i,18]) + "," + str(flagged_dataset_true.iloc[i,19]) + "," + str(flagged_dataset_true.iloc[i,20]) + "," + str(flagged_dataset_true.iloc[i,21]) + "," + str(flagged_dataset_true.iloc[i,22]) + "," + str(flagged_dataset_true.iloc[i,23]) + "," + str(flagged_dataset_true.iloc[i,24]) + "," + str(flagged_dataset_true.iloc[i,25]) + "\n")

                f.write(str(flagged_dataset_false.iloc[i,0]) + "," + str(flagged_dataset_false.iloc[i,1]) + "," + str(flagged_dataset_false.iloc[i,2]) + "," + str(flagged_dataset_false.iloc[i,3]) + "," + str(flagged_dataset_false.iloc[i,4]) + "," + str(flagged_dataset_false.iloc[i,5]) + "," + str(flagged_dataset_false.iloc[i,6]) + "," + str(flagged_dataset_false.iloc[i,7]) + "," + str(flagged_dataset_false.iloc[i,8]) + "," + str(flagged_dataset_false.iloc[i,9]) + "," + str(flagged_dataset_false.iloc[i,10]) + "," + str(flagged_dataset_false.iloc[i,11]) + "," + str(flagged_dataset_false.iloc[i,12]) + "," + str(flagged_dataset_false.iloc[i,13]) + "," + str(flagged_dataset_false.iloc[i,14]) + "," + str(flagged_dataset_false.iloc[i,15]) + "," + str(flagged_dataset_false.iloc[i,16]) + "," + str(flagged_dataset_false.iloc[i,17]) + "," + str(flagged_dataset_false.iloc[i,18]) + "," + str(flagged_dataset_false.iloc[i,19]) + "," + str(flagged_dataset_false.iloc[i,20]) + "," + str(flagged_dataset_false.iloc[i,21]) + "," + str(flagged_dataset_false.iloc[i,22]) + "," + str(flagged_dataset_false.iloc[i,23]) + "," + str(flagged_dataset_false.iloc[i,24]) + "," + str(flagged_dataset_false.iloc[i,25]) + "\n")

                f.close()
            else :
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")

        
        
        
    elif (balance == 'imbalanced') : #if imbalanced, just use flagged dataset
        for i in range(0, int(no_flags_to_use/2)) :
            if (no_sensors == 8) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset.iloc[i,0]) + "," + str(flagged_dataset.iloc[i,1]) + "," + str(flagged_dataset.iloc[i,2]) + "," + str(flagged_dataset.iloc[i,3]) + "," + str(flagged_dataset.iloc[i,4]) + "," + str(flagged_dataset.iloc[i,5]) + "," + str(flagged_dataset.iloc[i,6]) + "," + str(flagged_dataset.iloc[i,7]) + "," + str(flagged_dataset.iloc[i,8]) + "," + str(flagged_dataset.iloc[i,9]) + "\n")
                f.close()
                #FOR NOW we just want the last 1 hour of data and to look at recall and accuracy for that 

            elif (no_sensors == 16) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset.iloc[i,0]) + "," + str(flagged_dataset.iloc[i,1]) + "," + str(flagged_dataset.iloc[i,2]) + "," + str(flagged_dataset.iloc[i,3]) + "," + str(flagged_dataset.iloc[i,4]) + "," + str(flagged_dataset.iloc[i,5]) + "," + str(flagged_dataset.iloc[i,6]) + "," + str(flagged_dataset.iloc[i,7]) + "," + str(flagged_dataset.iloc[i,8]) + "," + str(flagged_dataset.iloc[i,9]) + "," + str(flagged_dataset.iloc[i,10]) + "," + str(flagged_dataset.iloc[i,11]) + "," + str(flagged_dataset.iloc[i,12]) + "," + str(flagged_dataset.iloc[i,13]) + "," + str(flagged_dataset.iloc[i,14]) + "," + str(flagged_dataset.iloc[i,15]) + "," + str(flagged_dataset.iloc[i,16]) + "," + str(flagged_dataset.iloc[i,17]) + "\n")
                f.close()

            elif (no_sensors == 24) :
                f=open('algorithm_data.csv', "a+")
                f.write(str(flagged_dataset.iloc[i,0]) + "," + str(flagged_dataset.iloc[i,1]) + "," + str(flagged_dataset.iloc[i,2]) + "," + str(flagged_dataset.iloc[i,3]) + "," + str(flagged_dataset.iloc[i,4]) + "," + str(flagged_dataset.iloc[i,5]) + "," + str(flagged_dataset.iloc[i,6]) + "," + str(flagged_dataset.iloc[i,7]) + "," + str(flagged_dataset.iloc[i,8]) + "," + str(flagged_dataset.iloc[i,9]) + "," + str(flagged_dataset.iloc[i,10]) + "," + str(flagged_dataset.iloc[i,11]) + "," + str(flagged_dataset.iloc[i,12]) + "," + str(flagged_dataset.iloc[i,13]) + "," + str(flagged_dataset.iloc[i,14]) + "," + str(flagged_dataset.iloc[i,15]) + "," + str(flagged_dataset.iloc[i,16]) + "," + str(flagged_dataset.iloc[i,17]) + "," + str(flagged_dataset.iloc[i,18]) + "," + str(flagged_dataset.iloc[i,19]) + "," + str(flagged_dataset.iloc[i,20]) + "," + str(flagged_dataset.iloc[i,21]) + "," + str(flagged_dataset.iloc[i,22]) + "," + str(flagged_dataset.iloc[i,23]) + "," + str(flagged_dataset.iloc[i,24]) + "," + str(flagged_dataset.iloc[i,25]) + "\n")
                f.close()
            else :
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")
                print("NO. SENSORS ERROR - NOT 8, 16 OR 24")
    
    else :
        print("BALANCED ERROR - NOT BALANCED OR IMBALANCED")

        
    #print("--- File sort took %s seconds ---" % (time.time() - start_time))
            

                 
    
    
    
    
    
#NOT COMPLETE just storing here
def ml_algorithm_svc(no_sensors, no_flags_to_use, algorithm_C_value, algorithm_gamma_value, kernel, algorithm, k):
    #WE'RE gonna combine this with the code that selects from the file random lines, get 50 lines from each true and false, then feed into an algorithm

    from sklearn import svm
    from sklearn.naive_bayes import GaussianNB
    from sklearn.naive_bayes import MultinomialNB
    
    from sklearn import metrics
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import f1_score
    
    from matplotlib import pyplot as plt
    import pandas as pd
    import csv
    import time
    import statistics
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import cross_val_score
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import average_precision_score
    from sklearn.model_selection import KFold
    from sklearn.model_selection import RepeatedKFold


    start_time = time.time() # for timing it

    #do we need to just read selected lines? Could read in whole file and select later
    #algorithm_df = pd.read_csv('algorithm_data.csv', usecols=['flag_value', 'pir-hallway-1', 'pir-living_room-1', 'motion-bathroom-1', 'motion-bedroom-1'])

    algorithm_df = pd.read_csv('algorithm_data.csv')

    #THIS may well be of the form that we want for this 
    algorithm_array = algorithm_df.to_numpy()
    
    no_flags_to_use #max 200 for this document

    X = algorithm_array[0:no_flags_to_use,2:(no_sensors+2)] # rows 0-3 (4 rows) of columns 1-4 (first 4 sensors) of array (not of csv file)
    print(X.shape[1])

    y = algorithm_array[0:no_flags_to_use,1] # gets true/false from the flag_value column (column 1) for rows 0 to 3 (4 rows)
    y = [int(elem) for elem in y] # gets integer value of boolean variable

    total_correct = 0
    
    #moved to agitation_main
    #no_iterations = 1
    #accumulative_accuracy = 0
    #accumulative_precision = 0
    #accumulative_recall = 0
    #accumulative_f1 = 0
      
    #test train split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False) #I do my own shuffle thanks very much (to preserve support for true and false)

    if (algorithm == 'SVM') :
        #create svc
        clf = svm.SVC(C=algorithm_C_value, gamma=algorithm_gamma_value, kernel=kernel)
        #print("C value is: " + str(algorithm_C_value))
        
        #not using since k-fold
        #clf.fit(X_train, y_train) #originally used for making algorithm
        #predictions = clf.predict(X_test)
        
        #k-fold implementation
        kf = KFold(n_splits=k,shuffle=False)
        #kf = RepeatedKFold(n_splits=5, n_repeats=2, random_state=None) 
        kf.split(X)  
        # Iterate over each train-test split
        
        
        accuracy_model = []
        precision_model = []
        recall_model = []
        f1_score_model = []
        
        for train_index, test_index in kf.split(X):
            # Split train-test
            #print("Train:", train_index, "Validation:",test_index)
            X_train, X_test = X[train_index], X[test_index]
            count=0
            y_train = []
            y_test = []
            for index in train_index :
                y_train.append(y[index])
                
                #print(y_train)
                count = count + 1
                
            count=0
            for index in test_index :
                y_test.append(y[index])
                #print(y_test)
                count = count + 1
                
            # Train the model
            model = clf.fit(X_train, y_train)
            #predictions = clf.predict(X_test) #i added
            #print(predictions) # i added
            # Append to accuracy_model the accuracy of the model
            #print(y_test)
            #print(model.predict(X_test))
            #print(recall_score(y_test, model.predict(X_test)))
            
            accuracy_model.append(accuracy_score(y_test, model.predict(X_test), normalize=True))
            precision_model.append(precision_score(y_test, model.predict(X_test)))
            recall_model.append(recall_score(y_test, model.predict(X_test)))
            f1_score_model.append(f1_score(y_test, model.predict(X_test)))

        
        accuracy_score = statistics.mean(accuracy_model)
        print(accuracy_model)
        precision_score = statistics.mean(precision_model)
        recall_score = statistics.mean(recall_model)
        f1_score = statistics.mean(f1_score_model)
        
        
    else : 
        if (algorithm == 'GNB') :
            gnb = GaussianNB()
            
        elif (algorithm == 'MNB') :
            gnb = MultinomialNB()
            
        
        #k-fold implementation
        kf = KFold(n_splits=k,shuffle=False)
        #kf = RepeatedKFold(n_splits=5, n_repeats=2, random_state=None) 
        kf.split(X)  
        # Iterate over each train-test split
        
        
        accuracy_model = []
        precision_model = []
        recall_model = []
        f1_score_model = []
        for train_index, test_index in kf.split(X):
            # Split train-test
            #print("Train:", train_index, "Validation:",test_index)
            X_train, X_test = X[train_index], X[test_index]
            count=0
            for index in train_index :
                y_train[count] = y[index]
                #print(y_train)
                count = count + 1
                
            count=0
            for index in test_index :
                y_test[count] = y[index]
                #print(y_test)
                count = count + 1
                
            # Train the model
            model = gnb.fit(X_train, y_train)
            #predictions = clf.predict(X_test) #i added
            #print(predictions) # i added
            # Append to accuracy_model the accuracy of the model
            accuracy_model.append(accuracy_score(y_test, model.predict(X_test), normalize=True))
            precision_model.append(precision_score(y_test, model.predict(X_test)))
            recall_model.append(recall_score(y_test, model.predict(X_test)))
            f1_score_model.append(f1_score(y_test, model.predict(X_test)))

        
        accuracy_score = statistics.mean(accuracy_model)
        print(accuracy_model)
        precision_score = statistics.mean(precision_model)
        recall_score = statistics.mean(recall_model)
        f1_score = statistics.mean(f1_score_model)

    
    
    #manual accuracy calculation - same as the accuracy_score method
    #no_correct = 0
    #for i in range(0, len(y_test)):
    #    if y_test[i] == predictions[i] :
    #        no_correct = no_correct+1

    #print(no_correct/len(y_test))
    #total_correct = total_correct + (no_correct/len(y_test))


    #accuracy averager over no_iterations

    #moved to agitation_main
    #print("%.2f" % round(accuracy_score(y_test, predictions),2), "%.2f" % round(precision_score(y_test, predictions),2), "%.2f" % round(recall_score(y_test, predictions),2), "%.2f" % round(f1_score(y_test, predictions),2))

    #moved to agitation_main
    #accumulative_accuracy = accumulative_accuracy + accuracy_score(y_test, predictions)
    #precision averager over no_iterations
    #accumulative_precision = accumulative_precision + precision_score(y_test, predictions)
    #accumulative_recall = accumulative_recall + recall_score(y_test, predictions)
    #accumulative_f1 = accumulative_f1 + f1_score(y_test, predictions)

    


    #prints classification report
    #print(metrics.classification_report(y_test, predictions))
    
    #results = confusion_matrix(y_test, predictions)
    #print(results)



    #time the whole process
    #print("--- Creation of model took %s seconds ---" % (time.time() - start_time))
    
    return accuracy_model, precision_model, recall_model, f1_score_model
    
    
        
        
        
        
    
def run_algorithm(performance_test_results_file, variable_name, increment, end_value, iterations, no_sensors, no_flags_to_use, algorithm_C_value, algorithm_gamma_value, balance, kernel, algorithm, k):
    import numpy as np  
    import pandas as pd  
    import matplotlib.pyplot as plt  
    # %matplotlib inline #doesn't work - its a decorative thing
    
    
    #clears temp file for creating graph every time
    open('performance_results_temp.csv', 'w').close()
    #write first line - for all the values
    f=open('performance_results_temp.csv', "a+")
    f.write("no_sensors,no_flags_to_use,algorithm_C_value,algorithm_gamma_value,algorithm,k,value,metric\n")
    f.close()
    
    #no longer writing to that performance test results file
    if (variable_name == 'no_sensors'):
        value_sweep = no_sensors
        #f=open(performance_test_results_file, "a+")
        #f.write(str(variable_name) + ",Accuracy,Precision,Recall,F1Score,, Sensors," + str(no_sensors) + " - " + str(end_value) + ",,No. Flags," + str(no_flags_to_use) + ",,C," + str(algorithm_C_value) +"\n")
        #f.close()
    elif (variable_name == 'no_flags_to_use'):
        value_sweep = no_flags_to_use
        #f=open(performance_test_results_file, "a+")
        #f.write(str(variable_name) + ",Accuracy,Precision,Recall,F1Score,, Sensors," + str(no_sensors) + ",,No. Flags," + str(no_flags_to_use) + "-" + str(end_value) + ",,C," + str(algorithm_C_value) +"\n")
        #f.close()
    elif (variable_name == 'algorithm_C_value'):
        value_sweep = algorithm_C_value
        #f=open(performance_test_results_file, "a+")
        #f.write(str(variable_name) + ",Accuracy,Precision,Recall,F1Score,, Sensors," + str(no_sensors) + ",,No. Flags," + str(no_flags_to_use) + ",,C," + str(algorithm_C_value) + "-" + str(end_value) +"\n")
        #f.close()
    elif (variable_name == 'algorithm_gamma_value'):
        value_sweep = algorithm_gamma_value
        #f=open(performance_test_results_file, "a+")
        #f.write(str(variable_name) + ",Accuracy,Precision,Recall,F1Score,, Sensors," + str(no_sensors) + ",,No. Flags," + str(no_flags_to_use) + ",,C," + str(algorithm_C_value) + "-" + str(end_value) +"\n")
        #f.close()
    elif (variable_name == 'algorithm'):
        value_sweep = 0
    elif (variable_name == 'k'):
        value_sweep = k
       
    else :
        print("error in passing a variable value")
       
    
            
    spaces_count = 0
    while (value_sweep <= end_value) :    
        print("The value for " + str(variable_name) + " is: " + str(value_sweep))
        
        print(str(iterations) + " iterations, " + str(no_sensors) + " sensors, " + str(no_flags_to_use) + " flags used")
        print("Accuracy Precision Recall F1Score")
        no_iterations = iterations
        accumulative_accuracy = 0
        accumulative_precision = 0
        accumulative_recall = 0
        accumulative_f1 = 0
        
        
        for i in range(no_iterations) :
            shuffle_sensor_values_for_flags() #0.5 seconds
            prepare_data_for_algorithm(no_sensors, balance, no_flags_to_use) #0.6 seconds
            #print("The value for no_sensors is: " + str(no_sensors))
            accuracy_score = []
            precision_score = []
            recall_score = []
            f1_score = []
            accuracy_score, precision_score, recall_score, f1_score = ml_algorithm_svc(no_sensors, no_flags_to_use, algorithm_C_value, algorithm_gamma_value, kernel, algorithm, k)
            
    
            accumulative_accuracy = accumulative_accuracy + sum(accuracy_score)
            #precision averager over no_iterations
            accumulative_precision = accumulative_precision + sum(precision_score)
            accumulative_recall = accumulative_recall + sum(recall_score)
            accumulative_f1 = accumulative_f1 + sum(f1_score)
            
            print(accuracy_score)
            
            for i in range(0, k) :
                print("%.2f" % round(accuracy_score[i],2), "%.2f" % round(precision_score[i],2), "%.2f" % round(recall_score[i],2), "%.2f" % round(f1_score[i],2))
                
                #write that instance to the file
                f=open('performance_results_temp.csv', "a+")
                f.write(str(no_sensors) + ',' + str(no_flags_to_use) + ',' + str(algorithm_C_value) + ',' + str(algorithm_gamma_value) + ',' + str(algorithm) + ',' + str(k) + ',' + str(accuracy_score[i]) + ",accuracy_score" + "\n")
                f.write(str(no_sensors) + ',' + str(no_flags_to_use) + ',' + str(algorithm_C_value) + ',' + str(algorithm_gamma_value) + ',' + str(algorithm) + ',' + str(k) + ',' + str(precision_score[i]) + ",precision_score" + "\n")
                f.write(str(no_sensors) + ',' + str(no_flags_to_use) + ',' + str(algorithm_C_value) + ',' + str(algorithm_gamma_value) + ',' + str(algorithm) + ',' + str(k) + ',' + str(recall_score[i]) + ",recall_score" + "\n")
                f.write(str(no_sensors) + ',' + str(no_flags_to_use) + ',' + str(algorithm_C_value) + ',' + str(algorithm_gamma_value) + ',' + str(algorithm) + ',' + str(k) + ',' + str(f1_score[i]) + ",f1_score" + "\n")
                f.close()
            
            
        print("Averages:")
        print("%.2f" % round(accumulative_accuracy/no_iterations,2), "%.2f" % round(accumulative_precision/no_iterations,2), "%.2f" % round(accumulative_recall/no_iterations,2), "%.2f" % round(accumulative_f1/no_iterations,2), "\n")

        #create array of the variable sweep number and performance averages
        performances_averages_array = [value_sweep, accumulative_accuracy/no_iterations, accumulative_precision/no_iterations, accumulative_recall/no_iterations, accumulative_f1/no_iterations]
        #return performances_averages_array
        
        f=open(performance_test_results_file, "a+")
        f.write(str(performances_averages_array[0]) + "," + str(performances_averages_array[1]) + "," + str(performances_averages_array[2]) + "," + str(performances_averages_array[3]) + "," + str(performances_averages_array[4]) + "\n")
        f.close()
        

        #increment the sweep variable by the set increment
        if (variable_name == 'algorithm_C_value'):
            value_sweep = value_sweep * increment #if its C we're increasing, increase by a factor not an addition
        elif (variable_name == 'algorithm_gamma_value'):
            value_sweep = value_sweep + increment #if its gamma we're increasing, increase by a factor not an addition
        elif (variable_name == 'no_flags_to_use') :
            value_sweep = value_sweep + increment
        else :
            value_sweep = value_sweep + increment
            
        
        #increments relevant variable for the next iteration
        if (variable_name == 'no_sensors'):
            no_sensors = no_sensors + increment
        elif (variable_name == 'no_flags_to_use'):
            no_flags_to_use = no_flags_to_use+increment
        elif (variable_name == 'algorithm_C_value'):
            algorithm_C_value = algorithm_C_value*increment
        elif (variable_name == 'algorithm_gamma_value'):
            algorithm_gamma_value = algorithm_gamma_value+increment
        elif (variable_name == 'algorithm'):
            if (algorithm == 'SVM') :
                algorithm = 'GNB'
            elif (algorithm == 'GNB') :
                algorithm = 'MNB'
            #elif (algorithm == 'GNB') :
                #algorithm = *next one*
        elif (variable_name == 'k') :
            k = k + increment
        
        spaces_count = spaces_count + 1
        
        
        
    if (spaces_count < 18) :
        for i in range (0,(18-spaces_count)) :
            f=open(performance_test_results_file, "a+")
            f.write("\n")
            f.close()
    
    
    draw_box_plot(variable_name)
    
    
    
def draw_box_plot(variable_name):
    import numpy as np  
    import pandas as pd  
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    accuracy_df = pd.read_csv("performance_results_temp.csv") 
    accuracy_df.head()
    sns.set_style("whitegrid")
    flatui = ["#3498db", "#2ecc71", "#e74c3c", "orange", "#34495e", "#9b59b6"]
    #edited y axis to 0-1 for no_flags used
    box_plot = sns.boxplot(x = variable_name, y = 'value', hue = 'metric', hue_order=["accuracy_score", "precision_score", "recall_score", "f1_score"], saturation = 0.8, palette=flatui, fliersize = 3, linewidth = 0.6, width = 0.7, whis = 1.5, showmeans=True, meanline=True, meanprops={"color":"white", "linewidth":"0.6"}, data = accuracy_df).set_ylim([0, 1])
    
    #print(accuracy_df.groupby('value').variable_name.describe().unstack())
    
    medians = accuracy_df.groupby([variable_name])['value'].median()
    print(medians)
    
    #vertical_offset = accuracy_df['value'].median() * 0.05 # offset from median for display

    #for xtick in box_plot.get_xticks():
    #    box_plot.text(xtick,medians[xtick] + vertical_offset,medians[xtick], 
    #            horizontalalignment='center',size='x-small',color='w',weight='semibold')
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #fliersize = size of outlier marker
    #linewidth = width of lines
    #width = width of each block - smaller means more gaps between x values
    #whis = value above which a point will be considered an outlier (therefore as a dot thing)
    #ylim = max and min y values, brings uniformity for comparison
    #output_boxplot.savefig('ax.png')
    
    
    #fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    #ax = fig.add_subplot(111)
    # Create the boxplot
    #bp = ax.boxplot(accuracy_df)
    # Save the figure
    #fig.savefig('fig1.png', bbox_inches='tight')
    
    
    
    
    
#not using
def dataset_stats():
    import pandas as pd
        
    large_value = 10
    no_hours = 1
    iterations = 50
    
    
    for no_hours in range(1,4): 
        print("Results for " + str(no_hours) + " hours: ")
    
        zeroes_count_true_total = 0
        large_count_true_total = 0
        sum_true_total = 0

        for iterate in range(0,iterations) :
            shuffle_sensor_values_for_flags()
            stats_df_true = pd.read_csv('sensor_values_for_flags_true.csv')
            stats_array_true = stats_df_true.to_numpy()
            X = stats_array_true[0:100,2:26] #100 rows, 24 sensors

            zeroes_count_true = 0
            large_count_true = 0
            sum_true = 0

            for i in range(0,100) :
                large_row_true = 0
                for j in range(0,(8*no_hours)) :
                    if (X[i,j] == 0) :
                        zeroes_count_true = zeroes_count_true + 1
                    if (X[i,j]) > large_value :
                        large_row_true = 1
                        #print("True >10: " + str(i) + "," + str(j))
                    sum_true = sum_true + X[i,j]
                if (large_row_true == 1) :
                    large_count_true = large_count_true + 1

            zeroes_count_true_total = zeroes_count_true_total + zeroes_count_true
            large_count_true_total = large_count_true_total + large_count_true
            sum_true_total = sum_true_total + sum_true

        print("Total number of zeroes for true: " + str(zeroes_count_true_total/iterations))
        print("Number of rows with values greater than 10 for true: " + str(large_count_true_total/iterations))
        print("Total value of all true cells: " + str(sum_true_total/iterations))

        print("\n")



        zeroes_count_false_total = 0
        large_count_false_total = 0
        sum_false_total = 0

        for iterate in range(0,iterations) :
            shuffle_sensor_values_for_flags()
            stats_df_false = pd.read_csv('sensor_values_for_flags_false.csv')
            stats_array_false = stats_df_false.to_numpy()
            Y = stats_array_false[0:100,2:26] #100 rows, 24 sensors

            zeroes_count_false = 0
            large_count_false = 0
            sum_false = 0

            for i in range(0,100) :
                large_row_false = 0
                for j in range(0,(8*no_hours)) :
                    if (Y[i,j] == 0) :
                        zeroes_count_false = zeroes_count_false + 1
                    if (Y[i,j]) > large_value :
                        large_row_false = 1
                        #print("False >10: " + str(i) + "," + str(j))
                    sum_false = sum_false + Y[i,j]
                if (large_row_false == 1) :
                    large_count_false = large_count_false + 1

            zeroes_count_false_total = zeroes_count_false_total + zeroes_count_false
            large_count_false_total = large_count_false_total + large_count_false
            sum_false_total = sum_false_total + sum_false

        print("Total number of zeroes for false: " + str(zeroes_count_false_total/iterations))
        print("Number of rows with values greater than 10 for false: " + str(large_count_false_total/iterations))
        print("Total value of all false cells: " + str(sum_false_total/iterations))
        
        print("\n")
        print("\n")

    
    
    
    
    
    
    
    
def agitation_main():    
    import os
    from os import listdir
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings

    os.chdir(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project") #start in right directory
    cwd = os.getcwd() #gets current location
    #print(cwd)

    #initialise a csv file for all flags collated 
    open('flags_collated.csv', 'w').close() #clears output file    
    f=open('flags_collated.csv', "a+")
    f.write('datetime,flag_value\n')
    f.close()
    
    
    #muted for now since sensor_values_for_flags have been created
    #DONE
    #get_flags_data_setup()
    

    for patient_folder in os.listdir('patient_data'): #for each patient data file named OneDrive__
        cwd = os.getcwd() #gets current location
        newcwd = "".join([cwd, '\\', 'patient_data', '\\', patient_folder]) #create a string for the location to go into
        #print("Current directory: " + newcwd) #prints that string
        os.chdir(newcwd) # navigates into that patient's data folder
        #print(os.listdir(newcwd))

        #not sure if this is used
        cwd = os.getcwd()
        #print(cwd)
    
        #execute sensors for that folder - done now
        #DONE
        #all_sensors_per_hour()
        
        #already done for now
        #DONE
        #get_flags_data()
        
        
        #TEMP
        #flags_data = pd.read_csv('flags_total.csv')
        #for i in range(0, len(flags_data)):
        #    if (flags_data.iloc[i,1] == 'tihm-agitation'):
        #        flags_datetime = flags_data.iloc[i,0] #string 
        #        f=open(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project\just_flags_times.csv", "a+")
        #        f.write(str(flags_datetime) + "\n")
        #        f.close()

        
        os.chdir(r"C:\Users\barne\OneDrive\Documents\Surrey\Fourth Year\Individual Project") #go back to correct location afterwards

        
        
    #iterations, no_sensors (/8), no_flags_to_use (/200)        
            
    
    
    #BASIC TESTS - SHOULD SHOW BAD, OR AT LEAST UNRELIABLE RESULTS
    #print("BASIC TESTS - SHOULD SHOW BAD, OR AT LEAST UNRELIABLE RESULTS")
    #run_algorithm(10, 2, 20)
    #run_algorithm(10, 4, 20)
    #run_algorithm(10, 2, 50)
    #run_algorithm(10, 4, 50)
    
    #TESTING NO SENSORS
    #print("TESTING NO. SENSORS with 50 and then 200 flags used")
    #run_algorithm(30, 2, 50)
    #run_algorithm(30, 3, 50)
    #run_algorithm(30, 4, 50)
    #run_algorithm(30, 5, 50)
    #run_algorithm(30, 6, 50)
    #run_algorithm(30, 7, 50)
    #run_algorithm(30, 8, 50)
    
    #had to re run from halfway in
    #run_algorithm(30, 2, 200)
    #run_algorithm(30, 3, 200)
    #run_algorithm(30, 4, 200)
    #run_algorithm(30, 5, 200)
    #run_algorithm(30, 6, 200)
    #run_algorithm(30, 7, 200)
    #run_algorithm(30, 8, 200)

    
    #TESTING NO FLAGS USED
    #print("TESTING NO. FLAGS USED with 4 sensors and then 8 sensors")
    #run_algorithm(20, 4, 20)
    #run_algorithm(20, 4, 40)
    #run_algorithm(20, 4, 60)
    #run_algorithm(20, 4, 80)
    #run_algorithm(20, 4, 100)
    #run_algorithm(20, 4, 120)
    #run_algorithm(20, 4, 140)
    #run_algorithm(20, 4, 160)
    #run_algorithm(20, 4, 180)
    #run_algorithm(20, 4, 200)
    
    #run_algorithm(20, 6, 20)
    #run_algorithm(20, 6, 40)
    #run_algorithm(20, 6, 60)
    #run_algorithm(20, 6, 80)
    #run_algorithm(20, 6, 100)
    #run_algorithm(20, 6, 120)
    #run_algorithm(20, 6, 140)
    #run_algorithm(20, 6, 160)
    #run_algorithm(20, 6, 180)
    #run_algorithm(20, 6, 200)
    
    #run_algorithm(30, 8, 20)
    #run_algorithm(30, 8, 30)
    #run_algorithm(30, 8, 40)
    #run_algorithm(30, 8, 50)
    #run_algorithm(30, 8, 60)
    #run_algorithm(30, 8, 70)
    #run_algorithm(30, 8, 80)
    #run_algorithm(30, 8, 90)
    #run_algorithm(30, 8, 100)
    #run_algorithm(30, 8, 110)
    #run_algorithm(30, 8, 120)
    #run_algorithm(30, 8, 130)
    #run_algorithm(30, 8, 140)
    #run_algorithm(30, 8, 150)
    #run_algorithm(30, 8, 160)
    #run_algorithm(30, 8, 170)
    #run_algorithm(30, 8, 180)
    #run_algorithm(30, 8, 190)
    #run_algorithm(30, 8, 200)
    
    
    #create a function 'print dataset'
    
    #you decide what variable you're changing by inserting that as 'variable_value' when running run_algorithm, both in the first position and the position in which you want the variable to change.
    #variable_value, iterations, no_sensors (/8), no_flags_to_use (/200), algorithm_C_value)

    #MAYBE HAVE THE ABILITY TO CHOOSE NAME OF OUT PUT FILE
    performance_test_results_file = 'performance_test_results_7.csv'

    #clear performance_dataset.csv for writing
    open(performance_test_results_file, 'w').close()
    
    
        
    #run_algorithm(performance_test_results_file, variable_name, increment, end_value, iterations, no_sensors, no_flags_to_use, algorithm_C_value)
    #NOTE = C valuable liable to inconsistency so set it to end higher than desired end value
    
    #practices
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 2, 2, 20, 1.0)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 4, 2, 2, 20, 1.0)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 0.1, 1.5, 4, 4, 20, 0.5)
    
    f=open(performance_test_results_file, "a+")
    f.write("Sixth Test - no sensors increase with flags order columns 82713456\n")
    f.write("\n")
    f.close()
        
    #increase no_flags from 20 through 200 with different Cs and sensors=8
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 8, 20, 0.5)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 8, 20, 0.75)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 8, 20, 1.0)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 8, 20, 1.25)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 8, 20, 1.5)
    
    #increase no_flags from 20 through 200 with different Cs and sensors=4
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 4, 20, 0.5)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 4, 20, 0.75)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 4, 20, 1.0)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 4, 20, 1.25)
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 10, 4, 20, 1.5)
    
    #increase no_sensors from 2 through 8
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 100, 0.5)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 100, 1.0)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 100, 1.5)
    
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 50, 1.0)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 100, 1.0)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 10, 2, 200, 1.0)
    
    #increase C through 0.5 to 1.5 with no_flags=50, then 200 
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 0.1, 1.5, 10, 4, 50, 0.5)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 0.1, 1.5, 10, 4, 200, 0.5)
    
    
    #TEST 2
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 4, 50, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 4, 100, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 4, 200, 0.01)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 6, 50, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 6, 100, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 6, 200, 0.01)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 8, 50, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 8, 100, 0.01)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 10, 8, 200, 0.01)
    
    
    #NOTE - 'increment' for algorithm_C_value is a multiplier (i.e. should be 10)
    #run_algorithm(performance_test_results_file, variable_name, increment, end_value, iterations, no_sensors, no_flags_to_use, algorithm_C_value)
    
    #TEST 3
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 4, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 4, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 4, 200, 0.001)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 6, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 6, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 6, 200, 0.001)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 8, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 8, 200, 0.001)
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 10005, 30, 8, 200, 0.001)
    
    #TEST 5
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 1.0)

    #TEST 6
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 0.01)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 0.1)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 1.0)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 10)
    #run_algorithm(performance_test_results_file, 'no_sensors', 1, 8, 50, 2, 100, 100)
    
    #Test 7
    
    #dataset_stats()
    
    
    #NOTE - 'increment' for algorithm_C_value is a multiplier (i.e. should be 10)
    #NOTE - 'increment' for algorithm is 1 and end value is 1 for running SVM and GNB
    #NOTE - 'increment' for no_flags_to_use is a multiplier (i.e. should be 10)
    #run_algorithm(performance_test_results_file, variable_name, increment, end_value, iterations, no_sensors, no_flags_to_use, algorithm_C_value, algorithm_gamma_value, balance, kernel, algorithm, k)
    
    # k-fold testing
    #run_algorithm(performance_test_results_file, 'no_sensors', 8, 8, 1, 8, 20, 1.0, 'balanced', 'rbf', 'GNB')
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 200, 200, 50, 8, 200, 1.0, 'balanced', 'rbf', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 100, 10, 8, 200, 0.001, 0.001, 'balanced', 'poly', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'no_sensors', 8, 24, 10, 8, 200, 1, 0.01, 'balanced', 'rbf', 'SVM', 5)
    #run_algorithm(performance_test_results_file, 'no_sensors', 8, 8, 50, 8, 200, 1, 0.001, 'balanced', 'linear', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'k', 5, 5, 20, 8, 200, 1, 0.001, 'balanced', 'linear', 'MNB', 5)
    
    #run_algorithm(performance_test_results_file, 'k', 1, 10, 20, 8, 200, 1, 0.001, 'balanced', 'linear', 'SVM', 3)
    
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 120, 20, 8, 120, 1.0, 0.01, 'balanced', 'linear', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'k', 5, 5, 5, 8, 200, 1, 0.001, 'balanced', 'linear', 'MNB', 5)
    #run_algorithm(performance_test_results_file, 'algorithm', 1, 2, 50, 8, 200, 1, 0.001, 'balanced', 'poly', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'algorithm_C_value', 10, 100, 20, 8, 200, 0.001, 1, 'balanced', 'poly', 'SVM', 5)
    
    #run_algorithm(performance_test_results_file, 'k', 1, 10, 50, 8, 200, 1.0, 0.001, 'balanced', 'rbf', 'SVM', 2)
    run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 200, 50, 8, 20, 1.0, 0.001, 'balanced', 'linear', 'SVM', 5)
    
    #draw_box_plot('algorithm_C_value')
    #run_algorithm(performance_test_results_file, 'no_flags_to_use', 20, 120, 50, 8, 120, 1.0, 0.001, 'balanced', 'linear', 'SVM', 5)
    