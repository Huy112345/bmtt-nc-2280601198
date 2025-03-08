def TinhTongSoChan(lst):
    tong = 0
    for number in lst:
        if number % 2 == 0:
            tong += number
    return tong
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(',')))
tong_chan = TinhTongSoChan(numbers)
print("Tong cac so chan trong list la:", tong_chan)