import pickle
import os
# Specify the path to the pickled dictionary file
# pickle_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ,'resources','geocode_cache.pickle')
pickle_file = r"C:\Users\Akash Balaji\Downloads\DATA ENGINEERING\cis6930sp24-assignment2\resources\geocode_cache.pkl"

# Load the pickled dictionary
with open(pickle_file, 'rb') as file:
    dictionary = pickle.load(file)

print(len(dictionary.keys()))
# Access and use the loaded dictionary
# Example: Print the keys and values
# for key, value in dictionary.items():
#     print(key, value)