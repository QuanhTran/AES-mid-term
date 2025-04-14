# AES-mid-term

## Mô tả

Project này triển khai thuật toán AES để mã hóa và giải mã dữ liệu từ file văn bản. Các tính năng chính bao gồm:  
- Mã hóa dữ liệu từ file `input.txt` bằng khóa trong `key.txt`.  
- Giải mã dữ liệu và ghi kết quả vào `file.txt`.  
- Hỗ trợ các bước trong AES như mở rộng khóa, SubBytes, ShiftRows, MixColumns và AddRoundKey.  

Project được viết bằng Python và sử dụng thư viện `numpy` để xử lý ma trận.

## Cấu trúc thư mục

- `aes/`: Chứa các module chính của thuật toán AES.  
  - `constants.py`: Hằng số như S-box, Rcon.  
  - `key_expansion.py`: Mở rộng khóa.  
  - `transformations.py`: Các phép biến đổi AES.  
  - `encryption.py`: Mã hóa.  
  - `decryption.py`: Giải mã.  
- `utils/`: Công cụ hỗ trợ.  
  - `file_io.py`: Đọc/ghi file.  
  - `data_utils.py`: Xử lý dữ liệu.  
- `data/`: File dữ liệu.  
  - `input.txt`: Dữ liệu đầu vào.  
  - `key.txt`: Khóa mã hóa.  
  - `file.txt`: Kết quả đầu ra.  
- `main.py`: File main.