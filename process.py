import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('ver1.xlsx', sheet_name='Data Model')

# Feature Engineering
df['Ngày Xuất'] = pd.to_datetime(df['Ngày Xuất'])

last_date = pd.to_datetime('2023-11-30')

recency = df.groupby('Khách hàng')['Ngày Xuất'].max()
recency = (last_date - recency).dt.days

frequency = df.groupby('Khách hàng')['Ngày Xuất'].size()
aov = df.groupby('Khách hàng')['Doanh Thu'].mean()
promo = df.groupby('Khách hàng')['% SL Khuyến mãi'].mean()
profit = df.groupby('Khách hàng')['Lợi Nhuận'].sum()
revenue = df.groupby('Khách hàng')['Doanh Thu'].sum()
margin = profit / revenue
margin = margin.clip(lower=0)

# Create Label
churn = (recency > 30).astype(int)

#Model
X = pd.DataFrame({
    'Recency': recency,
    'Frequency': frequency,
    'AOV': aov,
    'PromoRate': promo,
    'Margin': margin
}).fillna(0)

# Lấy Segment (giữ 1 giá trị / KH)
segment = df.groupby('Khách hàng')['Segment'].first()

# Merge vào result
results = X.merge(segment, left_index=True, right_index=True)

y = churn

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

results['Churn_Prob'] = model.predict_proba(X_scaled)[:, 1]

#Output
#results = X.copy()
results['Khách hàng'] = results.index

results = results.sort_values('Churn_Prob', ascending=False)

def risk_level(p):
    if p > 0.8:
        return 'Khẩn cấp'
    elif p > 0.6:
        return 'Cao'
    else:
        return 'Trung bình'
    
results['Mức độ'] = results['Churn_Prob'].apply(risk_level)

def action(row):
    if row['Recency'] > 60:
        return 'Gọi ngay'
    elif row['Recency'] > 30:
        return 'Zalo offer'
    elif row['Segment'] == 'VIP':
        return 'Gặp mặt'
    return 'Email chăm sóc'

results['Hành động'] = results.apply(action, axis=1)

results.to_excel('churn_list.xlsx', index=False)