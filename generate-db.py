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
def generate_truong_data(num_rows):
    data = []
    MATR = set()
    TENTR = []
    DCHITR = []
    TRUONG = genius_names[:]
    random.shuffle(TRUONG)

    TENDUONG = genius_names[:]
    random.shuffle(TENDUONG)

    with tqdm(total=num_rows, desc="Generating Truong data") as pbar:
        for i in range(num_rows+1):
            while len(MATR) < i:
                MATR.add(generate_random_number_string(6))
                TENTR.append(TRUONG[i-1])
                DCHITR.append(str(int(generate_random_number_string(3))) + ' ' + TENDUONG[i-1]+" street")
            pbar.update(1)
    
    for matr, tentr, dchitr in zip(MATR, TENTR, DCHITR):
        data.append((matr, tentr, dchitr))
    return data

#generate data for hs table
def generate_hs_data(num_rows):
    data = []
    mahs=set()
    cccd=set()
    ho=[]
    ten=[]
    ntns=[]
    dchi_hs=[]
    with tqdm(total=num_rows, desc="Generating HS data") as pbar:
        for i in range(num_rows):
            while len(mahs)<i+1:
                mahs.add(generate_random_number_string(8))
            while len(cccd)<i+1:
                cccd.add( generate_random_number_string(10))
            ho.append(generate_random_string(8))
            ten.append(generate_random_string(8))
            ntns.append(generate_random_date(datetime.date(1995, 1, 1), datetime.date(2005, 12, 31)))
            dchi_hs.append(str(int(generate_random_number_string(3))) + ' ' + generate_random_name(genius_names)+" street")
            pbar.update(1)
    
    for ma, Ho, Ten, cc, ns, dchi in zip(mahs, ho, ten, cccd, ntns, dchi_hs):
        data.append((ma, Ho, Ten, cc, ns, dchi))
    
    return data

# Generate data for the HOC table
def generate_hoc_data(truong_data, hs_data):
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

                data.append((matr, mahs, nam_hoc, str(diemtb)[:3], xeploai, kqua))
            pbar.update(1)
    
    return data

# function to save data to csv file
def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data saved to {filename}")

# Generate data for the truong table and save data to csv file
truong_data = generate_truong_data(100)
save_data_to_csv(truong_data, "truong_data.csv")

# Generate data for the hs table and save data to csv file
hs_data = generate_hs_data(1000000)
save_data_to_csv(hs_data, "hs_data.csv")

# Generate data for the hoc table and save data to csv file
hoc_data = generate_hoc_data(truong_data, hs_data)
save_data_to_csv(hoc_data, "hoc_data.csv")

# read data from csv file change to numpy array
truong_data = pd.read_csv("truong_data.csv",index_col=False,header=None)
hs_data = pd.read_csv("hs_data.csv",index_col=False,header=None)
hoc_data=pd.read_csv("hoc_data.csv",index_col=False,header=None)
truong_data=truong_data.values
hs_data=hs_data.values
hoc_data=hoc_data.values


#connect to mysql database
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Binben14",
    database="truonghoc2"
)
cursor = mydb.cursor()

# function to push data to truong table
def insert_truong(cursor, truong_data):
    sql = "INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s,%s,%s)"
    total_rows = len(truong_data)
    count=0
    with tqdm(total=total_rows, desc="Inserting TRUONG data") as pbar:
        for row in truong_data:
            values = (row[0], row[1], row[2])
            cursor.execute(sql, values)
            count+=1
            pbar.update(1)
            if count==100:
                mydb.commit()
                count=0


# function to push data to hs table
def insert_hs(cursor, hs_data):
    sql = "INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s,%s,%s,%s,%s,%s)"
    total_rows = len(hs_data)
    count=0
    with tqdm(total=total_rows, desc="Inserting HS data") as pbar:
        for row in hs_data:
            values = (row[0], row[1], row[2], row[3], row[4], row[5])
            cursor.execute(sql, values)
            count+=1
            pbar.update(1)
            if count==100:
                mydb.commit()
                count=0



# function to push data to hoc table
def insert_hoc(cursor, hoc_data):
    sql = "INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES(%s,%s,%s,%s,%s,%s)"
    total_rows = len(hoc_data)
    count=0
    with tqdm(total=total_rows, desc="Inserting HOC data") as pbar:
        for row in hoc_data:
            values = (row[0], row[1], row[2], row[3], row[4], row[5])
            cursor.execute(sql, values)
            count+=1
            pbar.update(1)
            if count==100:
                mydb.commit()
                count=0

'''
ở bước này em xin phép được sử dụng thư viện của python để thêm từng batch dữ liệu một
vào trong database, vì em đã thử xuất ra các file .sql để thực hiện điều tương tự nhưng
vì lượng dữ liệu quá lớn nên máy của em không thể hoàn thành việc insert dữ liệu vào nên
đã tìm một phương pháp thay thế.
'''
insert_truong(cursor,truong_data)
insert_hs(cursor,hs_data)
insert_hoc(cursor,hoc_data)