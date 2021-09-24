import time
import datetime as dt
import statistics
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
    print()
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = ''
        city = input('Please enter name of city, valid options are: chicago, new york city, washington\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
            
        else:
            print()
            print('Wrong input; select city among chicago, new york city and washington')

    print()
    # Get user input for month (all, january, february, ... , june)
    while True:
        month = ''
        month = input('Now enter month you want to explore\n').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('wrong input; please try to enter month again')

    print()
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = ''
        day = input('Now it is time to enter the day of week to explore\n').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('wrong entry; please enter day of week again')

    print()
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
    print()   
    # load data file into a dataframe
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
    
    print()
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Display the most common month
    df['month'] = df['Start Time'].dt.month
    print('The most common month is:', statistics.mode(df['month']))   
    
    print()
    # Display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print('The most common day of week is:', statistics.mode( df['day_of_week']))     

    print()
    # Display the most common start hour
    df['Start_Hour'] = df['Start Time'].dt.hour
    print('The most common start hour is:', statistics.mode(df['Start_Hour']))

    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print()
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print()
    # Display most commonly used start station
    print('Most commonly used start station is:', statistics.mode(df['Start Station']))

    print()
    # Display most commonly used end station
    print('Most commonly used end station is:', statistics.mode(df['End Station']))

    print()
    # Display most frequent combination of start station and end station trip
    print('The most frequent combination of start and end staton is:', statistics.mode(df['Start Station'] + 'and' + df['End Station'])) 

    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print()
    # Display total travel time
    print('Total travel time is:', df['Trip Duration'].sum())

    print()
    # Display mean travel time
    print('Mean travel time is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print()
    # Display counts of user types
    print('The counts of user types are as follows:', df['User Type'].value_counts(ascending=True))
    
    print()
    # Display counts of gender
    if 'Gender' in df:
          print('The gender counts are as follows:', df['Gender'].value_counts())
    else:
          print('Sorry! there are no gender entries for this city')
    
    print()
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
          print('The earliest birth year is:', min(df['Birth Year'])) 
          print()
          print('The most recent birth year is:', max(df['Birth Year'])) 
          print()
          print('The most common birth year is:', statistics.mode(df['Birth Year']))
    else:
          print('Sorry! there are no birth year entries for this city')

    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Promts user if they want to see 5 rows of raw data."""
    print()
    ini = 0
    while True:
        user_prompt = input('Do you want to see 5 lines of raw data? Enter yes or no.\n').lower()
        if user_prompt == 'yes':
            ini += 1
            print(df.iloc[0:5])
        elif user_prompt.lower() == 'no':
            break     
    
    
def main():
    city = ''
    month = 0
    day = 0
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
