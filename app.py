import streamlit as st
import pandas as pd
import requests
import random

# Standard browser headers to bypass automated request blocks
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

@st.cache_data(ttl=600)
def fetch_products():
    response = requests.get('https://fakestoreapi.com/products', headers=HEADERS, timeout=10)
    response.raise_for_status()  # Throws HTTPError if response is 403, 500, etc.
    return response.json()

@st.cache_data(ttl=600)
def fetch_users():
    response = requests.get('https://randomuser.me/api/?results=20', headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()['results']

def transform_products(data):
    df = pd.DataFrame(data)
    df = df[['id', 'title', 'price', 'category', 'description', 'image']]
    return df

def transform_users(data):
    users = []
    for user in data:
        users.append({
            'user_id': user['login']['uuid'],
            'name': f"{user['name']['first']} {user['name']['last']}",
            'email': user['email'],
            'city': user['location']['city'],
            'country': user['location']['country'],
            'picture': user['picture']['medium']
        })
    return pd.DataFrame(users)

def assign_sellers(products, users):
    user_ids = users['user_id'].tolist()
    products['seller_id'] = [random.choice(user_ids) for _ in range(len(products))]
    return products.merge(users, left_on='seller_id', right_on='user_id')

def main():
    st.title("E-commerce Data Visualization with Sellers")
    st.write("This app visualizes e-commerce data fetched from the Fake Store API and assigns random sellers from the Random User API.")
    
    try:
        products_data = fetch_products()
        users_data = fetch_users()
    except Exception as e:
        st.error(f"Failed to fetch data from remote APIs: {e}")
        st.stop()
    
    products_df = transform_products(products_data)
    users_df = transform_users(users_data)
    
    merged_df = assign_sellers(products_df, users_df)
    
    st.write("## Data")
    st.write(merged_df)
    
    st.write("## Data Summary")
    st.write(merged_df.describe())

    st.write("## Product Prices")
    st.bar_chart(merged_df[['price']])
    
    if st.checkbox('Show product images'):
        st.write("## Product Images")
        for index, row in merged_df.iterrows():
            st.image(row['image'], caption=row['title'], use_container_width=True)

    if st.checkbox('Show seller information'):
        st.write("## Seller Information")
        for index, row in merged_df.iterrows():
            st.image(row['picture'], caption=row['name'], use_container_width=True)
            st.write(f"Name: {row['name']}")
            st.write(f"Email: {row['email']}")
            st.write(f"Location: {row['city']}, {row['country']}")
            st.write("---")

if __name__ == "__main__":
    main()