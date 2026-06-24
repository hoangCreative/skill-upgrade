# Nâng một skill cho tới chuẩn

Tôi có một skill chạy được. Phần lớn ca nó làm xong việc, và cái cám dỗ là chải
chuốt lại câu chữ, tăng số phiên bản, gọi đó là đã nâng cấp. Rồi tôi thả một hội
đồng agent vào, việc duy nhất của họ là phá nó, và tôi ngồi nhìn nó diễn lại đúng
kỷ luật của chính mình, tự khai là đạt, mà vẫn vi phạm chính luật của nó. Hôm đó
tôi hiểu ra: "làm cho đẹp hơn" không phải là nâng cấp. Nâng cấp bắt đầu từ chỗ gọi
được tên nó hỏng ở đâu.

Skill này là cái quy trình đó, viết ra để chạy được trên bất kỳ skill nào, không
riêng cái nó sinh ra từ đấy.

## Cổng phân cỡ trước đã

Bài học đắt nhất của bản trước: nó bê nguyên sức nặng của một engine lớn đè lên
mọi skill, bắt một skill phản xạ bốn chục dòng phải qua nguyên bộ test ngàn ca và
một dây chuyền tự kiểm nó chẳng bao giờ dùng. Nên giờ, trước mọi bước, phải phân
cỡ skill đã: phản xạ, mô-đun, hay engine. Cỡ nào thì bộ đồ nấy. Đừng dựng cái giàn
giáo mà skill không cần.

## Hai luật trùm

1. Nâng cấp phải có lý do. Đừng nâng cho gọn gàng. Gọi tên cái bản này đang làm
   sai, ai chịu thiệt, và một bản người lạ xài được sẽ mở ra điều gì. Không gọi
   được cái lỗ thì không có gì để nâng.
2. Phải tự ăn cơm mình nấu. Quy trình phải theo đúng kỷ luật của chính cái skill
   nó đang nâng, và để lại bằng chứng đã theo. Nâng một skill kiểm chứng thì mọi
   lời trong bản nâng cũng phải có nguồn hoặc ghi rõ là chưa kiểm.

## Bảy bước

Tóm gọn: (1) gọi tên cái lỗ và khóa kiến trúc trước khi viết một chữ; (2) thử dưới
áp lực, có hội đồng đối kháng, rồi vạch ranh cắt / giữ / sửa / thêm; (3) viết lại
và neo mọi điều vào cái đã có thật trước đó, cộng đồng trước, không lấy từ trí
nhớ; (4) tách bộ máy chung khỏi phần lệ thuộc bối cảnh; (5) hình thức hóa bộ test
thành thứ người khác chạy lại được; (6) dựng hạ tầng đóng góp giữ được chuẩn mà
không cần người gác cổng; (7) audit, lên phiên bản, đóng gói. Mỗi bước để lại một
dấu vết kiểm được, và cú tăng phiên bản bị khóa trên cái checklist đó.

## Chỗ nó dừng

Nó là một quy trình, không phải một bảo chứng. Nó làm một skill thành trung thực
và lặp lại được; nó không làm một ý tưởng dở thành đáng giữ, và không tự ép được
nếu bạn bỏ bước. Con checker chỉ soi được một artifact CÓ tồn tại, không soi được
nó có TỐT không. Phần đó là việc của mắt người.

(Bản đầy đủ tiếng Anh, phương pháp luận, bộ test ở README.md cùng thư mục.)

Tác giả: Lê Công Hoàng. Giấy phép Apache-2.0.
