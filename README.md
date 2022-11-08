json-to-csv
===========

*Nested JSON to CSV Converter.*

This python script converts valid, preformatted JSON to CSV which can be opened in excel and other similar applications.
This script can handle nested json with multiple objects and arrays.
Please see the explanation below and the sample files to understand how this works. It can handle non similar objects too. But, more the similarity of the objects, prettier the output.

Written in Python 2.7. Last tested in Python 3.6.3.

Usage
-----

```
python /path/to/json_to_csv.py node json_in_file_path csv_out_file_path
```


If you want to run the script via a jupyter notebook, you can use code below:

```
!python "json_to_csv.py" "STATION" "metadata.json" "metadata__2.csv"
```

Source Specification
--------------------
The script expects the json to be given via a file containing 

* A valid JSON
* The JSON can be an `Array` of `node` `Object`
Ex:-
```python
    {
        "node":[
            {
                "item_1":"value_11",
                "item_2":"value_12",
                "item_3":"value_13",
                "item_4":["sub_value_14", "sub_value_15"],
                "item_5":{
                    "sub_item_1":"sub_item_value_11",
                    "sub_item_2":["sub_item_value_12", "sub_item_value_13"]
                }
            },
            {
                "item_1":"value_21",
                "item_2":"value_22",
                "item_4":["sub_value_24", "sub_value_25"],
                "item_5":{
                    "sub_item_1":"sub_item_value_21",
                    "sub_item_2":["sub_item_value_22", "sub_item_value_23"]
                }
            }
        ]
    }
```
* The JSON can be a `list` of `dictionaries`
* If your JSON is a list of dictionaries, the first argument `node` can be any relevant string
```python
    [
        {
            "item_1":"value_11",
            "item_2":"value_12",
            "item_3":"value_13",
            "item_4":["sub_value_14", "sub_value_15"],
            "item_5":{
                "sub_item_1":"sub_item_value_11",
                "sub_item_2":["sub_item_value_12", "sub_item_value_13"]
            }
        },
        {
            "item_1":"value_21",
            "item_2":"value_22",
            "item_4":["sub_value_24", "sub_value_25"],
            "item_5":{
                "sub_item_1":"sub_item_value_21",
                "sub_item_2":["sub_item_value_22", "sub_item_value_23"]
            }
        }
    ]
```

Gotchas
-------
I have written a JSON generator which will take care of encoding issues and generate a valid JSON for this tool. 
~~However, If you find yourself in the character encoding hell, drop me a mail and I will add support for this~~ This is now fixed.

Read More
---------
Visit [converting nested json to csv post on my blog](https://askvinay.com/post/converting-nested-json-to-csv-8-december-2013.html) to read more about this script.
