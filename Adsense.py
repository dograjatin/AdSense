import matplotlib.pyplot  as plt    # library for plotting and visualisation
import pandas as pd                 # library for handling csv files or spreadsheets
from collections import Counter
#print(pd.__version__)


class app:

    # Class hold properties of Apps Used by the people (App Data) 
    def __init__(self,app_name,op_time,duration,browse_cat):
        self.app_name = app_name    # the name of the app used
        self.op_time = op_time      # the opening time of app
        self.duration = duration    #the duration for which the app was used
        self.browse_cat = browse_cat        # the catagory of content they browsed
    
    
class person:

    # Class hold properties of People (People Data) 
    def __init__(self,f_name,age,gender,occupation):
        self.name = f_name      #name of the person
        self.age = age          # age of the person
        self.gender = gender    # gender of the person
        self.occupation = occupation        #occupation of the person


#Read the CSV FIle
sample_data = pd.read_csv("C:\\Users\\jatin\\Desktop\\Development\\Python\\AppData.csv")

app_user_count = pd.value_counts(sample_data['app_name'])   # user count of every app .. type = Series
#plt.plot(app_user_count)
#plt.show()

age_user_count = sample_data.groupby('age')['app_name'].value_counts()
edu_lvl_user_count = sample_data.groupby('education')['app_name'].value_counts()
occup_user_count = sample_data.groupby('occupation')['app_name'].value_counts()
mrt_sts_user_count = sample_data.groupby('marital_status')['app_name'].value_counts()

genre_user_count = sample_data.groupby('genre')['app_name'].value_counts()
tv_user_count = genre_user_count['TV/Entertainment']
beauty_user_count = genre_user_count['Beauty']
food_user_count = genre_user_count['Food']
music_user_count = genre_user_count['Music']
'''plt.hist(tv_user_count)
plt.plot(beauty_user_count)
plt.plot(food_user_count)
plt.plot(music_user_count)
plt.plot(['TV/Entertainment','Beauty','Food','Music'])
plt.show()'''

print(genre_user_count)








    



    


