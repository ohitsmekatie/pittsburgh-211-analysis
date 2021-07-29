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