#creating function to split header
def parse_headers(header_line):
    return header_line.strip().split(',')
#function to replace missing values
def parse_values(data_line):
    values=[]
    for items in data_line.strip().split(','):
        if items== '':#check if there is an empty string
            values.append(0.0)
        else:
            values.append(float(items))
    return values
#function to create dictionary of items
def create_item_dict(values,headers):
    results={}
    for value,header in zip(values,headers):
        result[header]=value
    return result


#creating a read_csv function
def read_csv(path):
    result=[]
    #open the file in read mode
    with open (path,'r') as f:
        #get a list of lines
        lines=f.realines()
        #parse the header
        headers = parse_headers(lines[0])
        #loop over the remaining lines
        for data_line in lines[1:]:
            #parse the values
            values= parse_values(data_line)
            #create a dictionary using values and headers
            item_dict = create_item_dict(values,headers)
            #add the dictionary to the result
            results.append(item_dict)
    return result 

