def top_10_chart(dataframe):
    # counts request categories 
    category_counts = dataframe.groupby("needs_category")["contact_date"].count()

# sorts values and changes them in place 
    category_counts.sort_values(inplace = True, ascending = False)

# gets top 10 rows after the series has been sorted in place 
    top_10_requests = category_counts.head(10)
    top_10_requests.sort_values(inplace = True)

    ax = top_10_requests.plot( kind="barh", color="teal", figsize=(13,5), title="Top 10 Allegheny County 211 Requests", grid=True)
    ax.set_xlabel("Num. Requests")
    ax.set_ylabel("Request Category")
    

def show_month_count_chart(dataframe):
    month_counts = dataframe["contact_date"].groupby(dataframe.contact_date.dt.month).agg('count')
    
    ax = month_counts.plot(kind="bar", 
                           color="gold", 
                           figsize=(13,5), 
                           title="Count of Requests by Month", 
                           grid=True)
                          
    ax.set_xlabel("Month")
    ax.set_ylabel("Num. Requests")

    
def show_zipcode_counts(dataframe):
    zipcode_counts = dataframe.groupby("zip_code")["contact_date"].count()
    zipcode_counts.sort_values(inplace = True, ascending = False)
    
    ax = zipcode_counts.plot(kind="bar", 
                           color="orchid", 
                           figsize=(25,7), 
                           title="Count of Requests by Zipcode", 
                           grid=True)
                          
    ax.set_xlabel("Zipcode")
    ax.set_ylabel("Num. Requests")
    
    
def show_age_counts(dataframe):
    age_counts = dataframe.groupby("age_range")["contact_date"].count()
    age_counts.sort_values(inplace = True, ascending = True)
    
    ax = age_counts.plot(kind="barh", 
                           color="yellowgreen", 
                           figsize=(25,7), 
                           title="Count of Requests by Age", 
                           grid=True)
                          
    ax.set_xlabel("Age Range")
    ax.set_ylabel("Num. Requests")
    