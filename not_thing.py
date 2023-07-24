import random
import string
import datetime
import mysql.connector
from tqdm import tqdm
import csv
import pandas as pd
import numpy as np

# this is an array of genius names I will use for school name and street
genius_names = [
    "Albert Einstein",
    "Leonardo da Vinci",
    "Isaac Newton",
    "Nikola Tesla",
    "Marie Curie",
    "Galileo Galilei",
    "Alexander Graham Bell",
    "Charles Darwin",
    "Thomas Edison",
    "Alan Turing",
    "Stephen Hawking",
    "Ada Lovelace",
    "Michael Faraday",
    "Wolfgang Amadeus Mozart",
    "Pablo Picasso",
    "Ludwig van Beethoven",
    "Nikolaus Copernicus",
    "Louis Pasteur",
    "Sigmund Freud",
    "Alberto Santos-Dumont",
    "Rosalind Franklin",
    "Leonhard Euler",
    "Archimedes",
    "Enrico Fermi",
    "Antoine Lavoisier",
    "Carl Friedrich Gauss",
    "Niels Bohr",
    "Marie-Louise von Franz",
    "Emily Dickinson",
    "Rene Descartes",
    "C. V. Raman",
    "Lise Meitner",
    "Gottfried Wilhelm Leibniz",
    "James Clerk Maxwell",
    "Louis Armstrong",
    "Guglielmo Marconi",
    "Ada Yonath",
    "Leonhard Euler",
    "Amelia Earhart",
    "Antoni Gaudí",
    "Jane Goodall",
    "Gottlieb Daimler",
    "Martha Graham",
    "Alfred Nobel",
    "George Washington Carver",
    "Mahatma Gandhi",
    "Hermann Hesse",
    "Eleanor Roosevelt",
    "John Locke",
    "Frida Kahlo",
    "Lao Tzu",
    "Hypatia",
    "Muhammad Ali",
    "Johannes Kepler",
    "Mae Jemison",
    "Fyodor Dostoevsky",
    "Coco Chanel",
    "Cleopatra",
    "Louis Braille",
    "Kurt Gödel",
    "Maria Montessori",
    "Nelson Mandela",
    "Plato",
    "Rabindranath Tagore",
    "Walt Disney",
    "Ernest Hemingway",
    "Johann Sebastian Bach",
    "Helen Keller",
    "Alan Rickman",
    "Alexander Fleming",
    "Grace Hopper",
    "Hedy Lamarr",
    "Billie Holiday",
    "Claude Monet",
    "James Watt",
    "Margaret Hamilton",
    "Mozart",
    "Rumi",
    "Vincent van Gogh",
    "Fridtjof Nansen",
    "Oscar Wilde",
    "Fridtjof Nansen",
    "Rosa Parks",
    "Marcel Proust",
    "Ludwig Wittgenstein",
    "Frederick Douglass",
    "Indira Gandhi",
    "J.R.R. Tolkien",
    "Auguste Rodin",
    "Leonhard Euler",
    "Blaise Pascal",
    "Mary Shelley",
    "Ella Fitzgerald",
    "Mahmoud Darwish",
    "Thomas Jefferson",
    "Rosalind Franklin",
    "John Keats",
    "George Orwell",
    "Friedrich Nietzsche",
    "Sojourner Truth"
]

def plus_one(num_str):
    """
    Adds 1 to a number string and pads the output with leading zeros.
    """
    num_int = int(num_str)  # convert number string to integer
    num_int += 1  # add 1 to integer
    num_str_length = len(num_str)
    result = str(num_int).zfill(num_str_length)  # convert integer back to string and pad with leading zeros
    return result


def insert_truong(cursor, truong_data):
    sql = "INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s,%s,%s)"
    values = (truong_data[0], truong_data[1], truong_data[2])
    cursor.execute(sql, values)
    mydb.commit()


# function to push data to hs table
def insert_hs(cursor, hs_data):
    sql = "INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (hs_data[0], hs_data[1], hs_data[2], hs_data[3], hs_data[4], hs_data[5])
    cursor.execute(sql, values)
    mydb.commit()


# function to push data to hoc table
def insert_hoc(cursor, hoc_data):
    sql = "INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES(%s,%s,%s,%s,%s,%s)"
    values = (hoc_data[0], hoc_data[1], hoc_data[2], hoc_data[3], hoc_data[4], hoc_data[5])
    cursor.execute(sql, values)
    mydb.commit()



#get an random name of school or street
def generate_random_name(genius_name):
    return random.choice(genius_name)

#get random name for student
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

#get random date of birth
def generate_random_date(start_date, end_date):
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    random_days=start_date + datetime.timedelta(days=random_days)

    # Convert datetime to string
    return random_days.strftime("%Y-%m-%d")   

#get random number string have length we want
def generate_random_number_string(length):
    digits=string.digits
    random_string = ''.join(random.choices(digits, k=length))
    return random_string

# generate a hundred data for truong table   
def generate_truong_data(cursor,num_rows):
    TRUONG = genius_names[:]
    random.shuffle(TRUONG)
    TENDUONG = genius_names[:]
    random.shuffle(TENDUONG)

    with tqdm(total=num_rows, desc="Generating Truong data") as pbar:
        for i in range(num_rows+1):
            MATR=generate_random_number_string(6)
            TENTR=TRUONG[i-1]
            DCHITR=str(int(generate_random_number_string(3))) + ' ' + TENDUONG[i-1]+" street"
            insert_truong(cursor,(MATR, TENTR, DCHITR))
            pbar.update(1)
            
#generate data for hs table
def generate_hs_data(cursor,num_rows):
    mahs="00000000"
    cccd="1000000000"
    with tqdm(total=num_rows, desc="Generating HS data") as pbar:
        for i in range(num_rows):
            mahs=plus_one(mahs)
            cccd=plus_one(cccd)
            ho=generate_random_string(8)
            ten=generate_random_string(8)
            ntns=generate_random_date(datetime.date(1995, 1, 1), datetime.date(2005, 12, 31))
            dchi_hs=str(int(generate_random_number_string(3))) + ' ' + generate_random_name(genius_names)+" street"
            insert_hs(cursor,(mahs, ho, ten, cccd, ntns, dchi_hs))
            pbar.update(1)

# Generate data for the HOC table
def generate_hoc_data(cursor,truong_data, hs_data):
    data = []
    temp = []
    with tqdm(total=len(hs_data), desc="Generating HOC data") as pbar:
        for row in hs_data:
            mahs = row[0]
            matr, _, _ = random.choice(truong_data)
            time = random.randint(1, 3)
            nam_hoc = random.randint(2010, 2019)
            for i in range(time):
                nam_hoc=nam_hoc+1
                diemtb = random.uniform(0, 10)
                xeploai = ''
                if diemtb > 9:
                    xeploai = "Xuất sắc"
                elif diemtb > 8:
                    xeploai = "Giỏi"
                elif diemtb > 6.5:
                    xeploai = "Khá"
                elif diemtb > 5:
                    xeploai = "Trung bình"
                else:
                    xeploai = "Yếu"
                kqua = ''
                if xeploai == "Yếu":
                    kqua = "Chưa hoàn thành"
                else:
                    kqua = "Hoàn thành"

                insert_hoc(cursor,(matr, mahs, nam_hoc, str(diemtb)[:3], xeploai, kqua))
            pbar.update(1)

# function to save data to csv file
def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data saved to {filename}")

print("WORKING WITH TRUONGHOC1....")
#connect to mysql database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Binben14",
    database="truonghoc1"
)
cursor = mydb.cursor()
# Generate data for the truong table and save data to csv file
truong_data = generate_truong_data(cursor,100)

# Generate data for the hs table and save data to csv file
hs_data = generate_hs_data(cursor,1000000)

# Generate data for the hoc table and save data to csv file
hoc_data = generate_hoc_data(cursor,truong_data, hs_data)

print("WORKING WITH TRUONGHOC2....")

#connect to mysql database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Binben14",
    database="truonghoc2"
)
cursor = mydb.cursor()
# Generate data for the truong table and save data to csv file
truong_data = generate_truong_data(cursor,100)

# Generate data for the hs table and save data to csv file
hs_data = generate_hs_data(cursor,1000000)

# Generate data for the hoc table and save data to csv file
hoc_data = generate_hoc_data(cursor,truong_data, hs_data)



# function to push data to truong table
# def insert_truong(cursor, truong_data):
#     sql = "INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s,%s,%s)"
#     total_rows = len(truong_data)
#     count=0
#     with tqdm(total=total_rows, desc="Inserting TRUONG data") as pbar:
#         for row in truong_data:
#             values = (row[0], row[1], row[2])
#             cursor.execute(sql, values)
#             count+=1
#             pbar.update(1)
#             if count==100:
#                 mydb.commit()
#                 count=0


# # function to push data to hs table
# def insert_hs(cursor, hs_data):
#     sql = "INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s,%s,%s,%s,%s,%s)"
#     total_rows = len(hs_data)
#     count=0
#     with tqdm(total=total_rows, desc="Inserting HS data") as pbar:
#         for row in hs_data:
#             values = (row[0], row[1], row[2], row[3], row[4], row[5])
#             cursor.execute(sql, values)
#             count+=1
#             pbar.update(1)
#             if count==100:
#                 mydb.commit()
#                 count=0



# # function to push data to hoc table
# def insert_hoc(cursor, hoc_data):
#     sql = "INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES(%s,%s,%s,%s,%s,%s)"
#     total_rows = len(hoc_data)
#     count=0
#     with tqdm(total=total_rows, desc="Inserting HOC data") as pbar:
#         for row in hoc_data:
#             values = (row[0], row[1], row[2], row[3], row[4], row[5])
#             cursor.execute(sql, values)
#             count+=1
#             pbar.update(1)
#             if count==100:
#                 mydb.commit()
#                 count=0


# cursor = mydb.cursor()
# insert_truong(cursor,truong_data)
# insert_hs(cursor,hs_data)
# insert_hoc(cursor,hoc_data)


# #connect to mysql database
# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Binben14",
#     database="truonghoc2"
# )
# cursor = mydb.cursor()
# insert_truong(cursor,truong_data)
# insert_hs(cursor,hs_data)
# insert_hoc(cursor,hoc_data)