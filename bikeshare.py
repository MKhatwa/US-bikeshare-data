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
    possible_cities = ['chicago', 'new york city', 'washington']
    
    while True:
        city = input('Which city you would like to hear about: ').lower()
        try:
            if city in possible_cities:
                print('\nLooks like we will explore the data from {}\n'.format(city.title()))
                break
            else:
                print('\nYou have entered an invalid city.\n')
                print('\nMake sure that your selection is Chicago, New York City or Washington\n')   
        except:
            print('\nWrong Input\n')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    possible_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    
    while True:        
        month = input('Which month you would like to know about: ').lower()
        try:
            if month in possible_months:
                print('\nLooks like we will filter by {}\n'.format(month.title()))
                break
            else:
                print('\nYou have entered an invalid month.')
                print('Make sure that your selection is one of the following (January, February, March, April, May, June)')
                print('You can also enter "all" to continue without filtering\n')
        except:
            print('\nWrong Input\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    possible_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    
    while True:        
        day = input('Which day you would like to know about: ').lower()
        try:
            if day in possible_days:
                print('\nLooks like we will filter by {}\n'.format(day.title()))
                break
            else:
                print("\nYou have entered an invalid day. Make sure that you enter the day's format as so: 'Friday'")
                print('You can also enter "all" to continue without filtering\n')
        except:
            print('\nWrong Input\n')
            
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
                    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def see_raw_data(df):
    raw_data = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
    i = 0
    while True:
        if raw_data != 'yes':
            break
        else:
            print(df.iloc[i:i+5])
            more_data = input('\nWould you like to see more data? Enter yes or no.\n').lower()
            i += 5
            if more_data != 'yes':
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()        
       
    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    pop_month_dic= {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    print('Most common month:', pop_month_dic[popular_month])

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most common hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['popular_comb'] = df['Start Station'] + ' <-> ' + df['End Station']
    freq_comb = df['popular_comb'].value_counts().idxmax()
    #df['popular_comb'] = df.groupby(['Start Station', 'End Station'])
    #freq_comb = df['popular_comb'].value_counts().idxmax()
    print('Most frequent combination:', freq_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time:', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    #if city != 'washington'
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)
    else:
        print('\nNo information was found related to "Gender" for Washington\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    #if city != 'washington'
    if 'Birth Year' in df:
        ealiest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].value_counts().idxmax()
        
        print('Ealiest year of birth:', int(ealiest_year))
        print('Most recent year of birth:', int(recent_year))
        print('Most common year of birth:', int(common_year))
    else:
        print('\nNo information was found related to "Year of Birth" for Washington\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        see_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
               
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
