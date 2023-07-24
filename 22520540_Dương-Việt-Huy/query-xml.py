from lxml import etree
from tabulate import tabulate
import os
import glob

def read_xml_file(file_path, low_score, high_score):
    data = []

    # Đọc file XML
    tree = etree.parse(file_path)
    root = tree.getroot()

    # Sử dụng Xpath để lấy danh sách học sinh có điểm trung bình nằm trong ngưỡng điểm [thấp, cao]
    query = "//HS[DIEMTB >= {} and DIEMTB <= {}]".format(low_score, high_score)
    students = root.xpath(query)

    # Tạo danh sách dữ liệu
    data = []
    for student in students:
        ho = student.findtext('HO')
        ten = student.findtext('TEN')
        ntns = student.findtext('NTNS')
        diemtb = student.findtext('DIEMTB')
        xeploai = student.findtext('XEPLOAI')
        kqua = student.findtext('KQUA')
        data.append([ho + " " + ten, ntns, diemtb, xeploai, kqua])

    # Hiển thị danh sách dữ liệu dưới dạng bảng thông tin
    headers = ["Họ tên", "Ngày sinh", "Điểm trung bình", "Xếp loại", "Kết quả"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)

# Sử dụng hàm để đọc file XML và in ra danh sách học sinh
xml_folder="C:/Users/huydv/OneDrive - Trường ĐH CNTT - University of Information Technology/Tài liệu/Ben/Mysql/22520540_DuongVietHuy/do_an_ck"
# Liệt kê tất cả các tệp tin trong thư mục
all_files = os.listdir(xml_folder)
# Lọc chỉ các tệp tin có đuôi .xml
xml_files = [f for f in all_files if f.endswith(".xml")]
table_xml = tabulate(enumerate(xml_files), headers=["Mã chọn", "file"])
print(table_xml)


data_path_indx=input("Nhập mã chọn file xml: ")
data_path=xml_files[int(data_path_indx)]
min_point=input("Nhập ngưỡng điểm tối thiểu: ")
max_point=input("Nhập ngưỡng điểm tối đa: ")
print(read_xml_file(data_path, min_point , max_point))