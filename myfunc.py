#check how many nan values are in a col
def check_na(col_name,df):
    return sum(df[col_name].isna())


#turn dollars(prices) to 
def numericalize(string):
    if type(string) != str:
        pass
    else:
        num = ''
        for char in list(string):
            if char.isnumeric() or char == '.':
                num += char
        return float(num)
    
    
#get aggregated(adj,avg) data
def get_adj_avg(lst,df):
    adj_= []
    avg_= []
    for x in lst:
        adj_.append(df[x])
        avg_.append(df.groupby(x).price.mean())
    return adj_, avg_


