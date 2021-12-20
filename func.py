import matplotlib.pyplot as plt

def counts_by_year(dataframe):
    string_dates = dataframe["contact_date"].astype(str)
    num_2021 = 0
    num_2020 = 0
    other = 0 
    
    for date in string_dates:
        if date.startswith('2020'):
            num_2020 += 1 
        elif date.startswith('2021'):
            num_2021 += 1 
        else:
            other +=1
    
    count_list = [54866,37434]
    years = [2020, 2021]
    requests_2020 = 54866
    requests_2021 = 37434
    
    fig = plt.figure()

    plt.bar(years,count_list, color="darkcyan")
    plt.xticks(years)
    plt.xlabel("year")
    plt.title("Count of requests by year", fontsize=14)
    fig.set_figheight(10)
    fig.set_figwidth(10)
    plt.show()
    
    
def top_10_chart(dataframe):
    '''
    a function that takes in a dataframe and prints a horizontal barchart of top 10 211 requests
    using pandas insted of matplotlib to see the difference in chart setup
    '''
   
    category_counts = dataframe.groupby("needs_category")["contact_date"].count()
    category_counts.sort_values(inplace = True, ascending = False)
    top_10_request_counts = category_counts[:10]
    categories = ['Covid-19 Control',
     'Rent Payment Assistance',
     'COVID-19 Immun. Clinics',
     'Tax Prep. Asst.',
     'Electric Pay Asst.',
     'Gas Payment Asst.',
     'Undesignated Temp Financial Asst.',
     'Food Pantries',
     'Housing Search Asst.',
     'Housing Coordinated Entry']

    fig = plt.figure()
    plt.bar(categories, top_10_request_counts, color = "plum")
    plt.title("Top 10 requests", fontsize=40)
    plt.xticks(categories,fontsize=20)
    plt.yticks(fontsize=20)
    fig.set_figheight(40)
    fig.set_figwidth(70)
    plt.show()
    

def show_month_count_chart(dataframe):
    '''
    a function that takes in a dataframe and groups the requests by month to get number of monthly requests
    '''
    month_counts = dataframe["contact_date"].groupby(dataframe.contact_date.dt.month).agg('count')
    months = ["Jan.", "Feb.", "March", "April", "May", "June", "July", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]

    fig = plt.figure()
    
    plt.bar(months, month_counts, color = "goldenrod")
    plt.xticks(months, fontsize=12)
    plt.title("Count of requests by month", fontsize=14)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    plt.show()

    
def show_zipcode_counts(dataframe):
    '''
    a function that takes in a dataframe, groups the requests by zipcode and prints a bar chart
    '''
    zipcode_counts = dataframe.groupby("zip_code")["contact_date"].count()
    zipcode_counts.sort_values(inplace = True, ascending = False)
    zipcode_counts = zipcode_counts[:20]
    zipcodes = zipcode_counts.index 

    fig = plt.figure()

    plt.bar(zipcodes, zipcode_counts, color = "rosybrown")
    plt.xticks = (zipcodes)
    plt.title("Count of requests by zipcode", fontsize=20)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    plt.show()
 
  
def show_age_counts(dataframe):
    age_counts = dataframe.groupby("age_range")["contact_date"].count()
    age_counts.sort_values(inplace = True, ascending = True)
    age_ranges = ["45 to 64", "25 to 44", "65 and over", "18 to 24", "6 to 17", "5 and under"]
    
    fig = plt.figure()
    
    plt.barh(age_ranges, age_counts, color = "olivedrab")
    # plt.xticks(age_ranges)
    plt.title("Count of requests by age", fontsize=20)
    fig.set_figheight(10)
    fig.set_figwidth(20)
    plt.show()
    
#     ax = age_counts.plot(kind="barh", 
#                            color="thistle", 
#                            title="Count of Requests by Age")
                          
#     ax.set_xlabel("Age Range")
#     ax.set_ylabel("Num. Requests")
    


    
# this is actually not very interesting so i'm commenting it out for now. top 3 requests counts age range 

# new_df = allegheny_df[["age_range","needs_category"]]
# new_df = new_df.fillna("No Age Given")

# top_3_list = ["Covid-19 Control", 
#                "COVID-19 Immunization Clinics", 
#                "Rent Payment Assistance"
#               ]

# top_3_requests_with_age = new_df[new_df["needs_category"].isin(top_3_list)]


# cat_count_by_age = top_3_requests_with_age.groupby(['age_range', 'needs_category']).agg({'needs_category': ['count']})
# cat_count_by_age.columns = ['number_of_requests']
# cat_count_by_age = cat_count_by_age.reset_index()

# cat_count_by_age