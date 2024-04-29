import os
import json
import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_record():
    name = random_string(random.randint(5, 15))
    age = random.randint(18, 80)
    bio = random_string(random.randint(20, 100))
    gender = random.choice(['male', 'female'])
    return {'name': name, 'age': age, 'bio': bio, 'gender': gender}

def json_file(file_path, num_records):
    data = [random_record() for _ in range(num_records)]
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def json_files(output_folder):
    num_files = random.randint(12, 17)
    os.makedirs(output_folder, exist_ok=True)
    for i in range(1, num_files + 1):
        num_records = random.randint(1000, 39480)
        file_name = f"data_{i}.json"
        file_path = os.path.join(output_folder, file_name)
        json_file(file_path, num_records)

if __name__ == "__main__":
    output_folder = "test_data"
    json_files(output_folder)
    print("JSON files generated successfully.")

