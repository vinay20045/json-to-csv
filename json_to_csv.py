##
# This is as simple as a license can get. Please read 
# carefully and understand before using.
#
# I wrote this script because I needed it. I am opening
# up the source code to the world because I believe in 
# the power of royalty free knowledge and shared ideas.
#
# 1. This piece of code comes to you at no cost and no 
#    obligations.
# 2. You get NO WARRANTIES OR GUARANTEES OR PROMISES of
#    any kind.
# 3. If you are using this script you understand the risks
#    completely.
# 4. I request and insist that you retain this notice without
#    modification, but if you can't... I understand.
#
# --
# Vinay Kumar N P 
# vinay@askvinay.com
# www.askVinay.com
##

import sys
import json
import csv

##
# This function converts an item like 
# {
#   "item_1":"value_11",
#   "item_2":"value_12",
#   "item_3":"value_13",
#   "item_4":["sub_value_14", "sub_value_15"],
#   "item_5":{
#       "sub_item_1":"sub_item_value_11",
#       "sub_item_2":["sub_item_value_12", "sub_item_value_13"]
#   }
# }
# To
# {
#   "node_item_1":"value_11",
#   "node_item_2":"value_12",
#   "node_item_3":"value_13",
#   "node_item_4_0":"sub_value_14", 
#   "node_item_4_1":"sub_value_15",
#   "node_item_5_sub_item_1":"sub_item_value_11",
#   "node_item_5_sub_item_2_0":"sub_item_value_12",
#   "node_item_5_sub_item_2_0":"sub_item_value_13"
# }
##
def reduce_item(key, value):
    global reduced_item
    
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item(key+'_'+str(i), sub_item)
            i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key+'_'+str(sub_key), value[sub_key])
    
    #Base Condition
    else:
        reduced_item[str(key)] = str(value)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "\nUsage: python json_to_csv.py <node_name> <json_in_file_path> <csv_out_file_path>\n"
    else:
        #Reading arguments
        node = sys.argv[1]
        json_file_path = sys.argv[2]
        csv_file_path = sys.argv[3]

        fp = open(json_file_path, 'r')
        json_value = fp.read()
        raw_data = json.loads(json_value)

        processed_data = []
        header = []
        for item in raw_data[node]:
            reduced_item = {}
            reduce_item(node, item)

            header += reduced_item.keys()

            processed_data.append(reduced_item)

        header = list(set(header))
        header.sort()

        with open(csv_file_path, 'wb+') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in processed_data:
                writer.writerow(row)

        print "Just completed writing csv file with %d columns" % len(header)