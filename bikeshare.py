#Explore US Bikeshare Data
#Last changed: 11/02/2019

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS_DICT = { 1 : 'january',2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city = ''
    while (city != 'chicago' and city != 'new york city'and city != 'washington'):
        city = input('Which city do you want to explore?: Chicago, New York City or Washington?').lower()

    #Get user input for month (all, january, february, ... , june)
    month = ''
    while (month != 'all' and month != 'january'and month != 'february'and month != 'march' and month != 'april'and month != 'may' and month != 'june'):
        month = input('Which month do you want to explore?: all, january, february, march, aril, may or june?').lower()

    #Get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while (day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday'and day != 'friday' and day != 'saturday' and day != 'sunday'):
        day = input('Which day do you want to explore?: all, monday, tuesday, wednesday, thusday, friday, saturday or sunday?').lower()
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

        #Read csv depending on inserted city
        df = pd.read_csv(CITY_DATA[city])

        #Transform Start Time into datetime format
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        #Extract month, day & hour as new columns
        df['month'] = df['Start Time'].dt.month
        df['day'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        #Apply filter
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

        if month != 'all':
            month =  MONTHS.index(month) + 1
            df = df[ df['month'] == month]

        if day != 'all':
           df = df[ df['day'] == day.title()]

        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month
    most_c_month = df['month'].value_counts().idxmax()
    most_c_month = MONTHS_DICT[most_c_month].title()
    print('The most common bikeshare travel month is: ',most_c_month)

    #Display the most common day of week
    most_c_day = df['day'].value_counts().idxmax()
    print('The most common bikeshare travel day is: ',most_c_day)

    #Display the most common start hour
    most_c_hour = df['hour'].value_counts().idxmax()
    print('The most common bikeshare start hour is: ',most_c_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    most_c_start = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', most_c_start)

    #Display most commonly used end station
    most_c_end = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', most_c_end)

    #Display most frequent combination of start station and end station trip / research source: https://pandas.pydata.org/pandas-docs
    most_f_route = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent used route is: {}, {}'\
            .format(most_f_route[0], most_f_route[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    #Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats1(df):
    """Displays part1 statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types / research source: https://pandas.pydata.org/pandas-docs
    counts_user_type = df.groupby('User Type')['User Type'].count()
    print(counts_user_type)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats2(df):
    """Displays part2 statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of gender / research source: https://pandas.pydata.org/pandas-docs
    counts_gender = df.groupby('Gender')['Gender'].count()
    print(counts_gender)

    #Display earliest, most recent, and most common year of birth

    earliest_birthyear = df['Birth Year'].min()
    print("The most earliest birth year is: ", earliest_birthyear)

    mostrecent_birthyear = df['Birth Year'].max()
    print("The most recent birth year: ", mostrecent_birthyear)

    most_c_birthyear = df['Birth Year'].value_counts().idxmax()
    print("The most common birth year is: ", most_c_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    see_data = ''
    k=1
    see_data = input('Do you want to see the raw data? yes/no?').lower()
    while see_data == 'yes':
        print(df.iloc[k:k+5])
        k = k+5
        see_data = input('Do you want to see more raw data? yes/no?').lower()

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats1(df)
        if city!='washington':
            user_stats2(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
