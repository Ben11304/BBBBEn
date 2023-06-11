from lxml import etree

def read_xml_file(file_path, low_score, high_score):
    # Đọc file XML
    tree = etree.parse(file_path)
    root = tree.getroot()

    # Sử dụng Xpath để lấy danh sách học sinh có điểm trung bình nằm trong ngưỡng điểm [thấp, cao]
    query = "//HS[DIEMTB >= {} and DIEMTB <= {}]".format(low_score, high_score)
    students = root.xpath(query)

    # In ra danh sách học sinh
    for student in students:
        ho = student.findtext('HO')
        ten = student.findtext('TEN')
        ntns = student.findtext('NTNS')
        diemtb = student.findtext('../DIEMTB')
        xeploai = student.findtext('../XEPLOAI')
        kqua = student.findtext('../KQUA')
        print("Họ tên: {} {}, Ngày sinh: {}, Điểm trung bình: {}, Xếp loại: {}, Kết quả: {}".format(ho, ten, ntns, diemtb, xeploai, kqua))

# Sử dụng hàm để đọc file XML và in ra danh sách học sinh
data_path=input("nhập path của file xml: ")
read_xml_file(data_path, 7.7 , 10)