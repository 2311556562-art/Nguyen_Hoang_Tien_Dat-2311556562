DỰ ÁN: TỪ DỮ LIỆU ĐẾN PHÂN TÍCH VỚI PYTHON
Họ và tên: Nguyen Hoang Tien Dat
MSSV: 2311556562
Lớp: [Điền mã lớp]
Mục tiêu
Tìm hiểu mã hóa ASCII và UTF-8.
Thực hành tạo file TXT, CSV và JSON.
Làm quen với Git và GitHub.
Trả lời câu hỏi thu hoạch
Câu 1
Chuỗi tiếng Việt có dấu thường tốn nhiều byte hơn chuỗi tiếng Anh có cùng số ký tự vì UTF-8 mã hóa các chữ cái tiếng Anh cơ bản bằng 1 byte, trong khi nhiều ký tự tiếng Việt có dấu cần 2 hoặc 3 byte.

Câu 2
CSV phù hợp với dữ liệu dạng bảng gồm hàng và cột. JSON hỗ trợ đối tượng và danh sách lồng nhau nên phù hợp hơn khi dữ liệu có cấu trúc phân cấp.

Câu 3
Khi mở file ảnh bằng Notepad, ta thường thấy các ký tự lạ vì file ảnh chứa dữ liệu nhị phân, không phải văn bản thuần. Notepad cố gắng đọc các byte đó thành ký tự.

Câu 4
data/raw/ lưu dữ liệu gốc, còn data/processed/ lưu dữ liệu đã xử lý. Việc tách riêng giúp bảo vệ dữ liệu gốc và dễ tái lập quá trình phân tích. .gitignore giúp Git bỏ qua file tạm, cache và các file không cần đưa lên GitHub.

Câu 5
Sẽ bổ sung nhận xét về GPA trung bình, cao nhất và thấp nhất sau khi phân tích dữ liệu ở Buổi 2.