import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    password_dict = {}
    for password in range(1000, 10000):
        hashing_number = hashlib.sha256(str(password).encode()).hexdigest()
        password_dict[hashing_number] = password
    with open(input_file_name) as f, open(output_file_name, 'w', newline='') as outf:
        reader = csv.reader(f)
        writer = csv.writer(outf)
        for row in reader:
            name = row[0]
            for key in row[1:]:
                d_password = password_dict.get(key,'')
                if d_password:
                    writer.writerow([name, d_password])

                    