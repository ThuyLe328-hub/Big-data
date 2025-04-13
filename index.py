import pandas as pd
import plotly.express as px

# Đọc dữ liệu từ file CSV
df = pd.read_csv('Global_Cybersecurity_Threats_2015-2024.csv')

# Tính tổng số cuộc tấn công theo từng quốc gia
attack_counts = df['Country'].value_counts().reset_index()
attack_counts.columns = ['Country', 'Total Attacks']

# Chuẩn hóa tên quốc gia để phù hợp với mã quốc gia ISO
country_name_mapping = {
    'USA': 'United States',
    'UK': 'United Kingdom',
    'Russia': 'Russian Federation',
    'China': 'China',
    'India': 'India',
    'Germany': 'Germany',
    'France': 'France',
    'Japan': 'Japan',
    'Australia': 'Australia',
    'Brazil': 'Brazil'
}

attack_counts['Country'] = attack_counts['Country'].map(country_name_mapping)

# Tạo choropleth map
fig = px.choropleth(attack_counts,
                    locations='Country',
                    locationmode='country names',
                    color='Total Attacks',
                    hover_name='Country',
                    color_continuous_scale='YlOrRd',
                    title='Tổng số cuộc tấn công mạng theo quốc gia (2015-2024)',
                    labels={'Total Attacks': 'Số cuộc tấn công'},
                    projection='natural earth')

# Cập nhật layout
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    margin={"r":0,"t":40,"l":0,"b":0},
    coloraxis_colorbar=dict(
        title="Số cuộc tấn công",
        thicknessmode="pixels",
        thickness=15,
        lenmode="pixels",
        len=300,
        yanchor="top",
        y=1,
        xanchor="left",
        x=0.01
    )
)

# Hiển thị biểu đồ
fig.show()