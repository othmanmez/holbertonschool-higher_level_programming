import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print the titles"""
    # Send GET request
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Check the status code
    print(f"Status Code: {response.status_code}")
    
    # If successful, parse the JSON response
    if response.status_code == 200:
        posts = response.json()

        # Print the titles of the posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save to CSV"""
    # Send GET request
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Check the status code
    if response.status_code == 200:
        posts = response.json()

        # Prepare data for CSV (list of dictionaries)
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write to CSV file
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Write header row
            writer.writerows(posts_data)  # Write the post data rows

