# AES-mid-term

## Mô tả

Project này triển khai thuật toán AES để mã hóa và giải mã dữ liệu từ file văn bản sử dụng thuật toán AES-128. Các tính năng chính bao gồm:  
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

## Cách sử dụng

### 1. Chuẩn bị file đầu vào
- **File `data/input.txt`**: Chứa dữ liệu bạn muốn mã hóa (plaintext).  
    - Ví dụ nội dung:   This is a secret message!
    - Lưu ý: Dữ liệu sẽ được tự động padding (thêm `\x00`) nếu không đủ độ dài 16 bytes (một block AES).
- **File `data/key.txt`**: Chứa khóa mã hóa (key).  
    - Khóa phải là chuỗi ký tự có độ dài tối đa 16 bytes (128 bits). Nếu ngắn hơn, chương trình sẽ tự động padding bằng `\x00`.  
    - Ví dụ nội dung:   mysecretkey12345

### 2. Chạy chương trình
- Đảm bảo bạn đã cài đặt theo yêu cầu.  
- Mở terminal và di chuyển đến thư mục dự án:
```bash
cd /đường/dẫn/đến/thư/mục/dự/án

python main.py