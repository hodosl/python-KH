def get_number_data():
    input_data = "abcd"
    number = int(input_data)
def get_data():
    try:
       return get_number_data()
    except ValueError:
        print("nem szám")
    print("end")


get_data()
