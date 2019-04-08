import csv
import json

data_list = []
data_dict = {
    "timestamp": 0,
    "gps_lat": 0,
    "gps_lon": 0,
    "gps_alt": 0,
    "pitch": 0,
    "yaw": 0,
    "roll": 0,
    "rel_forward_acc": 0,
    "rel_up_acc": 0,
    "abs_north_acc": 0,
    "abs_east_acc": 0,
    "abs_up_acc": 0
    }

# with open('accel.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         i = reader.line_num
#         data_dict['timestamp'] = i*0.1
#         temp = row[0].split(' ')
#         data_dict['abs_north_acc'] = float(temp[1])
#         data_dict['abs_east_acc'] = float(temp[0])
#         data_dict['abs_up_acc'] = 0
#         data_dict['yaw'] = float(temp[7])
#         data_list.append(dict(data_dict))


# with open('gps.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         i = reader.line_num - 1
#         data_list[i*10]['gps_lat'] = float(row[0])
#         data_list[i*10]['gps_lon'] = float(row[1])


with open('data.txt', 'r') as f:

    text = f.read().splitlines()
    del text[-1]
    # print(text)
    for line in text:
        temp = line.replace(' -> ',',').split(',')
        time = temp[0].split(':')
        # print(temp)
        # print(time)
        data_dict['timestamp'] = float(time[0])*3600 + float(time[1])*60 + float(time[2])
        data_dict['gps_lat'] = float(temp[1])*0.01
        data_dict['gps_lon'] = float(temp[3])*(-0.01)
        data_dict['abs_north_acc'] = float(temp[7])
        data_dict['abs_east_acc'] = float(temp[6])
        data_dict['abs_up_acc'] = 0
        data_dict['yaw'] = float(temp[9])
        data_list.append(dict(data_dict))

# print(data_list)


with open("data_file.json", "w") as write_file:
    json.dump(data_list, write_file)
