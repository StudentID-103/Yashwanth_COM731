import matplotlib.pyplot as plt

def print_com731(): print('COM731'); print('COM731'); print('COM731')
MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December']

def customer_stay_trends(df):
    print_com731(); country=input('Enter country code: ').strip().upper()
    try: year=int(input('Enter arrival year: '))
    except ValueError: print('Invalid year.'); return
    f=df[(df['country'].astype(str).str.upper()==country)&(df['arrival_date_year']==year)]
    if f.empty: print('No matching records.'); return
    g=f.groupby(['arrival_date_month','customer_type'])['stays_in_weekend_nights'].mean().unstack().reindex([m for m in MONTHS if m in f['arrival_date_month'].unique()])
    plt.figure(figsize=(11,6))
    for c in g.columns: plt.plot(g.index,g[c],marker='o',label=c)
    plt.title('Monthly Average Weekend Night Stays'); plt.xlabel('Arrival Month'); plt.ylabel('Average Weekend Nights'); plt.xticks(rotation=45); plt.legend(title='Customer Type'); plt.tight_layout(); plt.show()

def stay_duration_relationship(df):
    print_com731(); customer=input('Enter customer type: ').strip()
    f=df[df['customer_type'].astype(str).str.lower()==customer.lower()].copy()
    if f.empty: print('No matching records.'); return
    f['total_nights']=f['stays_in_weekend_nights']+f['stays_in_week_nights']
    plt.figure(figsize=(9,6)); plt.scatter(f['total_nights'],f['average_daily_rate'],alpha=.4); plt.title('Average Daily Rate vs Total Nights Stayed'); plt.xlabel('Total Nights Stayed'); plt.ylabel('Average Daily Rate'); plt.tight_layout(); plt.show()

def guest_requests_behaviour(df):
    print_com731(); deposit=input('Enter deposit type: ').strip()
    f=df[df['deposit_type'].astype(str).str.lower()==deposit.lower()]
    if f.empty: print('No matching records.'); return
    g=f.groupby('customer_type')['total_of_special_requests'].mean()
    if g.sum()==0: print('Cannot create pie chart because all averages are zero.'); return
    p=g/g.sum()*100
    plt.figure(figsize=(8,8)); plt.pie(p,labels=p.index,autopct='%1.1f%%'); plt.title('Proportion of Average Special Requests by Customer Type'); plt.tight_layout(); plt.show()

def custom_visualisation(df):
    print_com731(); hotel=input('Enter hotel type (City Hotel/Resort Hotel): ').strip()
    f=df[df['hotel'].astype(str).str.lower()==hotel.lower()]
    if f.empty: print('No matching hotel records.'); return
    g=f.groupby('arrival_date_month')['average_daily_rate'].mean(); g=g.reindex([m for m in MONTHS if m in g.index])
    plt.figure(figsize=(10,6)); plt.bar(g.index,g.values); plt.title('Average Daily Rate by Arrival Month'); plt.xlabel('Arrival Month'); plt.ylabel('Average Daily Rate'); plt.xticks(rotation=45); plt.tight_layout(); plt.show()
