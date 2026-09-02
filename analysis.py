def print_com731():
    print('COM731'); print('COM731'); print('COM731')

def top_market_segments(df):
    print_com731()
    channel=input('Enter distribution channel: ').strip(); country=input('Enter country code: ').strip().upper()
    f=df[(df['distribution_channel'].astype(str).str.lower()==channel.lower()) & (df['country'].astype(str).str.upper()==country)]
    if f.empty: print('No matching records were found.'); return
    print('\nTop 3 Market Segments by Average Lead Time')
    print(f.groupby('market_segment')['lead_time'].mean().sort_values(ascending=False).head(3).round(2))

def room_assignment_consistency(df):
    print_com731(); month=input('Enter arrival month: ').strip()
    f=df[df['arrival_date_month'].astype(str).str.lower()==month.lower()].copy()
    if f.empty: print('No bookings found for this month.'); return
    f['room_match']=f['reserved_room_type']==f['assigned_room_type']
    result=f.groupby('customer_type')['room_match'].mean()*100
    print('\nRoom Assignment Consistency by Customer Type')
    for k,v in result.items(): print(k, ':', round(v,2), '%')

def guest_preferences_analysis(df):
    print_com731(); meal=input('Enter meal type (BB/HB/FB/SC/Undefined): ').strip().upper()
    m=df[df['meal'].astype(str).str.upper()==meal]
    if m.empty: print('No matching meal records.'); return
    avg=m['average_daily_rate'].mean(); f=m[m['average_daily_rate']>avg]
    print('\nAverage ADR for', meal, '=', round(avg,2))
    print(f.groupby('reservation_status')[['total_of_special_requests','required_car_parking_spaces','booking_changes']].mean().round(2))

def custom_booking_analysis(df):
    print_com731()
    try: year=int(input('Enter arrival year (2015, 2016 or 2017): '))
    except ValueError: print('Invalid year.'); return
    f=df[df['arrival_date_year']==year].copy()
    if f.empty: print('No bookings found for that year.'); return
    f['total_nights']=f['stays_in_weekend_nights']+f['stays_in_week_nights']
    result=f.groupby('hotel').agg(average_adr=('average_daily_rate','mean'), average_total_nights=('total_nights','mean'), average_special_requests=('total_of_special_requests','mean')).round(2)
    print('\nCustom Hotel Booking Analysis\n', result)
