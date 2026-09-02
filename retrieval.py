def print_com731():
    print('COM731'); print('COM731'); print('COM731')

def get_column_indexes(header):
    return {name: i for i, name in enumerate(header)}

def seasonal_booking_patterns(header, data):
    print_com731(); idx = get_column_indexes(header)
    country = input('Enter country code (e.g. PRT, GBR, FRA): ').strip().upper()
    results = [[r[idx['arrival_date_month']], r[idx['arrival_date_week_number']], r[idx['arrival_date_day_of_month']]] for r in data if r[idx['country']].upper() == country]
    if not results: print('No bookings found for this country.'); return
    print('\nArrival Month | Week Number | Day of Month\n' + '-'*50)
    for x in results[:30]: print(x[0], '|', x[1], '|', x[2])
    print('\nTotal matching bookings:', len(results))

def guest_composition_details(header, data):
    print_com731(); idx = get_column_indexes(header)
    try: limit = int(input('Enter minimum number of nights: '))
    except ValueError: print('Invalid input. Please enter a whole number.'); return
    results=[]
    for r in data:
        try: weekend=int(r[idx['stays_in_weekend_nights']]); week=int(r[idx['stays_in_week_nights']])
        except ValueError: continue
        if weekend > limit or week > limit:
            results.append([r[idx['adults']], r[idx['children']], r[idx['babies']], weekend, week])
    if not results: print('No matching bookings were found.'); return
    print('\nAdults | Children | Babies | Weekend Nights | Week Nights\n' + '-'*65)
    for x in results[:30]: print(*x, sep=' | ')
    print('\nTotal matching records:', len(results))

def booking_history_loyalty(header, data):
    print_com731(); idx=get_column_indexes(header)
    customer=input('Enter customer type (Transient/Transient-Party/Contract/Group): ').strip()
    deposit=input('Enter deposit type (No Deposit/Non Refund/Refundable): ').strip()
    results=[]
    for r in data:
        if r[idx['customer_type']].lower()==customer.lower() and r[idx['deposit_type']].lower()==deposit.lower():
            results.append([r[idx['is_repeated_guest']], r[idx['previous_cancellations']], r[idx['previous_bookings_not_canceled']]])
    if not results: print('No matching records were found.'); return
    print('\nRepeated Guest | Previous Cancellations | Previous Bookings Not Cancelled\n' + '-'*80)
    for x in results[:30]: print(*x, sep=' | ')
    print('\nTotal matching records:', len(results))

def custom_booking_retrieval(header, data):
    print_com731(); idx=get_column_indexes(header)
    status=input('Enter reservation status (Check-Out/Canceled/No-Show): ').strip()
    results=[]
    for r in data:
        if r[idx['reservation_status']].lower()==status.lower():
            results.append([r[idx['hotel']], r[idx['market_segment']], r[idx['customer_type']], r[idx['average_daily_rate']]])
    if not results: print('No matching records were found.'); return
    print('\nHotel | Market Segment | Customer Type | Average Daily Rate\n' + '-'*80)
    for x in results[:30]: print(*x, sep=' | ')
    print('\nTotal matching records:', len(results))
