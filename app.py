import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu (hoặc bạn có thể giữ nguyên cấu trúc này)
data = {
    'Họ tên': ['An', 'Bình', 'Chi', 'Dũng', 'Hà', 'Lan', 'Minh', 'Nam', 'Phúc', 'Trang'],
    'Chuyên cần': [8.0, 9.0, 7.5, 6.0, 8.5, 9.5, 7.0, 8.0, 6.5, 9.0],
    'Giữa kỳ': [7.0, 8.0, 6.5, 5.5, 9.0, 8.5, 6.0, 7.5, 7.0, 8.5],
    'Cuối kỳ': [7.5, 8.5, 7.0, 6.0, 8.0, 9.0, 6.5, 8.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

# Tính tổng kết và xếp loại
df['Tổng kết'] = (df['Chuyên cần'] * 0.2 + df['Giữa kỳ'] * 0.3 + df['Cuối kỳ'] * 0.5).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7.0:
        return 'Khá'
    elif diem >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)

# 1. Hiển thị bảng điểm
st.subheader("1. Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

# 2. Thống kê
st.subheader("2. Thống kê kết quả học tập")
diem_tb_lop = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5.0).sum()

st.write(f"- **Điểm tổng kết trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(f"- **Sinh viên có điểm tổng kết cao nhất:** {sv_max['Họ tên']} ({sv_max['Tổng kết']})")
st.write(f"- **Sinh viên có điểm tổng kết thấp nhất:** {sv_min['Họ tên']} ({sv_min['Tong_ket'] if 'Tong_ket' in sv_min else sv_min['Tổng kết']})")
st.write(f"- **Số sinh viên đạt (điểm tổng kết >= 5):** {so_sv_dat}")

# 3. Chọn sinh viên xem chi tiết qua Selectbox
st.subheader("3. Tra cứu thông tin chi tiết theo sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Họ tên'].tolist())

# Lọc thông tin sinh viên được chọn
student_info = df[df['Họ tên'] == selected_student].iloc[0]
st.write(f"Chi tiết điểm của **{selected_student}**:")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Chuyên cần", student_info['Chuyên cần'])
col2.metric("Giữa kỳ", student_info['Giữa kỳ'])
col3.metric("Cuối kỳ", student_info['Cuối kỳ'])
col4.metric("Tổng kết", student_info['Tổng kết'])
col5.metric("Xếp loại", student_info['Xếp loại'])

# 4. Biểu đồ cột trực quan hóa
st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df['Họ tên'], df['Tổng kết'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Tên sinh viên')
ax.set_title('Biểu đồ điểm tổng kết')
ax.set_xlim(0, 10)
ax.invert_yaxis()
st.pyplot(fig)

# 5. Thông tin người tạo ở cuối trang
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: small;'>Ứng dụng được tạo bởi [Họ tên của bạn] - [MSSV của bạn]</p>", unsafe_allow_html=True)
