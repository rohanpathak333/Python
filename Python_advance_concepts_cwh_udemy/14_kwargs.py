def marks(**kwargs):
    # kwargs is a dictonary with all the key value pairs wich were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is  {kwargs[item]}")


marks (shubham = 34, vikrant =54, jack=34, Marie=90, Priya=45)