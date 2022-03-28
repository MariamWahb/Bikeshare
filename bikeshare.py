import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("kindly select a city by copying chicago , new york city or washington: \n ").lower()
     #if the user write a different input in CITY_DATA....
    while city not in CITY_DATA.keys():
        print("\n that's invalid input...")
        city = input("kindly select a city by copying chicago , new york city or washington: \n ").lower()

   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    print('"'*40)
    
    # TO DO: get user input for month (all, january, february, ... , june)
     # make a list with name of month or all......
    Months = ['janury', 'february', 'march', 'april', 'may', 'june', 'all']
    month =input("select a month: \n1.janury \n2.february \n3.march \n4.april \n5.may \n6.june \n7.all : \n").lower()
    
    #validate the user input...
    while month not in Months:
        print("\n that's invalid input...")
        month =input("select a month: \n1.janury \n2.february \n3.march \n4.april \n5.may \n6.june \n7.all : \n").lower()
        
    print('"'*40)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # make a list with day of week.....
    Days = ['saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday', 'friday' , 'all']
    day =input("select a day: \n1.saturday  \n2.sunday  \n3.monday  \n4.tuesday  \n5.wednesday  \n6.thursday  \n7.friday \n8.all :\n").lower()
    
    while day not in Days:
        print("\n that's invalid input...")
        day =input("select a day: \n1.saturday  \n2.sunday  \n3.monday  \n4.tuesday  \n5.wednesday  \n6.thursday  \n7.friday \n8.all :\n").lower()
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour # extract hour to creat new columns
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        Months = ['janury', 'february', 'march', 'april', 'may', 'june', 'all']
        month = Months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        
    return df

    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print(df['month'].mode()[0])
    print('-'*40) #separator
    # TO DO: display the most common day of week
    # the day_of_week had been add in the load_data , put it as it is in the load_data
    print(df['day_of_week'].mode()[0])
    print('-'*40) #separator
    # TO DO: display the most common start hour
    print(df['hour'].mode()[0])
    print('-'*40) #separator

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("most common start station: ",most_common_start_station)
    print('-'*40) #separator


    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])
    print('-'*40) #separator

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station= df[['Start Station' , 'End Station']].mode().loc[0]
    print("the most start end station is:{} , {} \n".format(most_common_start_end_station[0] , most_common_start_end_station[1]))
                              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time 
    # using sum() to calculating       
    total_travel= df['Trip Duration'].sum()
    print("Total travel:" , total_travel)

    # TO DO: display mean travel time
    # using mean() to calculating the mean time         
    mean_travel= df['Trip Duration'].mean()
    print("Mean travel:", mean_travel)

    # display data from the dataframe...
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n")
    start_loc = 0
    while (True):
       print(df.iloc[start_loc : start_loc+5])
       start_loc += 5
       view_display = input("Do you wish to continue?: ").lower()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ##print("the counts of the user types :{} ,{}\n".format(user_count)

    # TO DO: Display counts of gender
    print(df['User Type'].value_counts())      
    if city != "washington":
       print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington":
       print(df['Birth Year'].mode()[0])
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


   
def main():
    while True:
        city, month, day = get_filters()
        #print(city , month , day)
        df = load_data(city, month, day)
        #print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
