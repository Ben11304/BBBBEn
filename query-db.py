import mysql.connector
import time
import xml.etree.ElementTree as ET
import random
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


def query_data(database, school_name, academic_year, grade):
    # Kết nối đến cơ sở dữ liệu
    cnx = mysql.connector.connect(user='root', password='Binben14',
                                  host='127.0.0.1', database=database)
    cursor = cnx.cursor()

    # Tạo câu truy vấn
    query = '''
    SELECT HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
    FROM HS
    INNER JOIN HOC ON HS.MAHS = HOC.MAHS
    INNER JOIN TRUONG ON TRUONG.MATR = HOC.MATR
    WHERE TRUONG.TENTR = %s AND HOC.NAMHOC = %s AND HOC.XEPLOAI = %s
    '''

    # Thực hiện truy vấn
    start_time = time.time()
    cursor.execute(query, (school_name, academic_year, grade))
    results = cursor.fetchall()
    end_time = time.time()
    query_time = end_time - start_time

    # Tạo và xuất file XML
    root = ET.Element("data")
    for row in results:
        student = ET.SubElement(root, "student")
        ET.SubElement(student, "ho").text = row[0]
        ET.SubElement(student, "ten").text = row[1]
        ET.SubElement(student, "ntns").text = str(row[2])
        ET.SubElement(student, "diem_tb").text = str(row[3])
        ET.SubElement(student, "xep_loai").text = row[4]
        ET.SubElement(student, "ket_qua").text = row[5]
    
    tree = ET.ElementTree(root)
    xml_file = f"{database}-{school_name}-{academic_year}-{grade}.xml"
    tree.write(xml_file)

    # Đóng kết nối đến cơ sở dữ liệu
    cursor.close()
    cnx.close()

    # In thời gian truy vấn
    print("Thời gian truy vấn:", query_time, "giây")


database=["TRUONGHOC1","TRUONGHOC2"]

# School_name=input("Nhập Tên Trường: ")
# Year=input("Nhập Năm học: ")
# rank=input("Nhập Xếp Loại: ")

School_name=random.choice(genius_names)
Year=random.randint(2010, 2022)
rank=random.choice(["Xuất sắc", "Giỏi", "Khá", "Trung bình" ,"Yếu"])


# Gọi hàm query_data với các tham số tương ứng
query_data(database[0], School_name, Year, rank)
query_data(database[1], School_name, Year, rank)    
