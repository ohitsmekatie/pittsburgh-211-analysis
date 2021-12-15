
def top_10_chart(dataframe):
    # counts request categories 
    category_counts = dataframe.groupby("needs_category")["contact_date"].count()

# sorts values and changes them in place 
    category_counts.sort_values(inplace = True, ascending = False)

# gets top 10 rows after the series has been sorted in place 
    top_10_requests = category_counts.head(10)
    top_10_requests.sort_values(inplace = True)

    ax = top_10_requests.plot( kind="barh", color="thistle", figsize=(13,5), title="Top 10 Allegheny County 211 Requests", grid=True)
    ax.set_xlabel("Num. Requests")
    ax.set_ylabel("Request Category")
    

def show_month_count_chart(dataframe):
    month_counts = dataframe["contact_date"].groupby(dataframe.contact_date.dt.month).agg('count')
    
    ax = month_counts.plot(kind="bar", 
                           color="thistle", 
                           figsize=(13,5), 
                           title="Count of Requests by Month")
                          
    ax.set_xlabel("Month")
    ax.set_ylabel("Num. Requests")

    
def show_zipcode_counts(dataframe):
    zipcode_counts = dataframe.groupby("zip_code")["contact_date"].count()
    zipcode_counts.sort_values(inplace = True, ascending = False)
    
    ax = zipcode_counts.plot(kind="bar", 
                           color="thistle", 
                           figsize=(25,7), 
                           title="Count of Requests by Zipcode")
                          
    ax.set_xlabel("Zipcode")
    ax.set_ylabel("Num. Requests")
    
def show_age_counts(dataframe):
    age_counts = dataframe.groupby("age_range")["contact_date"].count()
    age_counts.sort_values(inplace = True, ascending = True)
    
    ax = age_counts.plot(kind="barh", 
                           color="thistle", 
                           title="Count of Requests by Age")
                          
    ax.set_xlabel("Age Range")
    ax.set_ylabel("Num. Requests")

    
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