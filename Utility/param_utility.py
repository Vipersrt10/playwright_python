# def test_param(fileName):
#     test_data = ''
#     with open(fileName,'r') as f :
#         test_data = f.readlines()
#     print(test_data)
#     input_data_columns = test_data[0].replace('\n','').split('|')
#     # print(input_data_columns)
#     input_data_columns = ','.join(input_data_columns[:-1])
#     actual_data_values = []
#     test_ids = []
#     for i in range(1,len(test_data)) :
#         sam_data = test_data[i].replace('\n','').split('|')[:-1]
#         actual_data_values.append(sam_data)
#         test_ids.append(test_data[i].replace('\n','').split('|')[-1])
#     # print(actual_data_values)
#     # print(test_ids)
#     return input_data_columns,actual_data_values,test_ids


def test_input_data_fields(fileName) :
    test_data = ''
    with open(fileName,'r') as f :
        test_data = f.readlines()
    # print(test_data)
    input_data_columns = test_data[0].replace('\n','').split('|')
    # print(input_data_columns)
    input_data_columns = ','.join(input_data_columns[:-1])
    return input_data_columns

def test_actual_data_values(fileName):
    test_data = ''
    with open(fileName,'r') as f :
        test_data = f.readlines()
    actual_data_values = []
    # test_ids = []
    for i in range(1,len(test_data)) :
        sam_data = test_data[i].replace('\n','').split('|')[:-1]
        actual_data_values.append(sam_data)
        # test_ids.append(test_data[i].replace('\n','').split('|')[-1])
    return actual_data_values

def test_ids_name(fileName):
    test_data = ''
    with open(fileName,'r') as f :
        test_data = f.readlines()
    # actual_data_values = []
    test_ids = []
    for i in range(1,len(test_data)) :
        # sam_data = test_data[i].replace('\n','').split('|')[:-1]
        # actual_data_values.append(sam_data)
        test_ids.append(test_data[i].replace('\n','').split('|')[-1])
    return test_ids

# test_param('./Data/textBox.csv')