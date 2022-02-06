import time
import pandas as pd
import numpy as np
#city names and their data files
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


    # TO DO: get user input for month (all, january, february, ... , june)
    valid_cities_list = ['chicago','new york city','washington']
    valid_days_list = ['all','monday','tuesday','wednessday','friday','saturday','sunday']
    valid_months_list =['all','january', 'february', 'march', 'april', 'may', 'june']
    take_input = True
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(take_input):
        city=input("Enter the city Name :").lower()
       
        if(city not in valid_cities_list):
            print("Please check the available cities list once")
            continue
        month=input("Enter the month Name :").lower()
        if(month not in valid_months_list):
            print("Please check available months list")
            continue
        day=input("Enter Day name :").lower()
        if(day not in valid_days_list):
            print("please check available days list ")
            continue
        take_input = False
        
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

   
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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
    
    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    # TO DO: display the most common month
    most_common_month = months_list[df['month'].mode()[0]-1]
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    output_msg = "Most Common Month :{}\nMost Common Day :{}\nMost Common Hour :{}".format(most_common_month,most_common_day,most_common_hour)
    print(output_msg)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print("Most common start station :",most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print("Most common end station :",most_commonly_used_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['start_to_end']= df['Start Station'] + "-->" + df['End Station']
#     print(df['start_to_end'])
    most_common_start_and_end = df['start_to_end'].mode()[0]
    print("Most common start and end stations",most_common_start_and_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel duration",total_travel_time,"seconds")
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time ",mean_travel_time,"seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print(user_types_count,end="\n")
    # TO DO: Display counts of gender
    try:
        gender_types_count = df['Gender'].value_counts()
        print(gender_types_count,end="\n")
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        print("Earliest year of birth",earliest_year_of_birth)
        most_recent_birth = int(df['Birth Year'].max())
        print("Most recent year of birth",most_recent_birth)
    
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("Most common year of birth",most_common_year_of_birth)
    except KeyError:
        print("Unable to show birth and gender details")
        print("Some cities don't have gender and birth year data")
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)
    
def display_raw_data(df):
    display_data = input("Would you like to view the raw data for the 5 lines :(yes/no)").lower()
    starting_index = 0
    while(display_data=="yes"):
        print(df.iloc[starting_index : starting_index+5])
        starting_index += 5
        display_data = input("continue displaying data for the next 5 lines too :(yes/no)").lower()
        

def main():
    print(CITY_DATA)
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#original main function
#execution starts from here
if __name__ == "__main__":
    main()
    
