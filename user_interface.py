from retrieval import seasonal_booking_patterns, guest_composition_details, booking_history_loyalty, custom_booking_retrieval
from analysis import top_market_segments, room_assignment_consistency, guest_preferences_analysis, custom_booking_analysis
from visualisation import customer_stay_trends, stay_duration_relationship, guest_requests_behaviour, custom_visualisation

def retrieval_menu(header,data):
    while True:
        print('\nTASK B - DATA RETRIEVAL\n1. Seasonal Booking Patterns\n2. Guest Composition Details\n3. Booking History and Loyalty\n4. Custom Booking Retrieval\n5. Return')
        c=input('Enter your choice: ')
        if c=='1': seasonal_booking_patterns(header,data)
        elif c=='2': guest_composition_details(header,data)
        elif c=='3': booking_history_loyalty(header,data)
        elif c=='4': custom_booking_retrieval(header,data)
        elif c=='5': break
        else: print('Invalid choice.')

def analysis_menu(df):
    while True:
        print('\nTASK C - DATA ANALYSIS\n1. Top Market Segments\n2. Room Assignment Consistency\n3. Guest Preferences Analysis\n4. Custom Booking Analysis\n5. Return')
        c=input('Enter your choice: ')
        if c=='1': top_market_segments(df)
        elif c=='2': room_assignment_consistency(df)
        elif c=='3': guest_preferences_analysis(df)
        elif c=='4': custom_booking_analysis(df)
        elif c=='5': break
        else: print('Invalid choice.')

def visualisation_menu(df):
    while True:
        print('\nTASK D - DATA VISUALISATION\n1. Customer Stay Trends\n2. Stay Duration Relationship\n3. Guest Requests Behaviour\n4. Custom Visualisation\n5. Return')
        c=input('Enter your choice: ')
        if c=='1': customer_stay_trends(df)
        elif c=='2': stay_duration_relationship(df)
        elif c=='3': guest_requests_behaviour(df)
        elif c=='4': custom_visualisation(df)
        elif c=='5': break
        else: print('Invalid choice.')

def main_menu(header,data,df):
    while True:
        print('\n'+'='*60+'\nCOM731 HOTEL BOOKING ANALYSIS SYSTEM\n'+'='*60)
        print('1. Task B - Data Retrieval\n2. Task C - Data Analysis\n3. Task D - Data Visualisation\n4. Dataset Information\n5. Exit')
        c=input('Enter your choice: ')
        if c=='1': retrieval_menu(header,data)
        elif c=='2': analysis_menu(df)
        elif c=='3': visualisation_menu(df)
        elif c=='4': print('Rows:',df.shape[0],'\nColumns:',df.shape[1],'\nMissing values:',df.isnull().sum().sum())
        elif c=='5': print('Thank you for using the COM731 Hotel Booking Analysis System.'); break
        else: print('Invalid option.')
