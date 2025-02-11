import requests
1716,1719,1843,1870,1724,1869,1725,1864,1721,1855,1723,1740,1753,1717,1715,1736,1752,1727,1764,1745,1747,1763,1749,1762,1728,1759,1758,1767,1768,1718,1734,1722,1858,1771,1770,1783,1760,1866,1779,1790,1794,1748,1810,1772,1776,1796,1761,1741,1735,1743,1756,1729
# Define the API URL
url = "http://127.0.0.1:8000/user/"  # Change to match your endpoint

# Define the headers with a Bearer token
headers = {
    "Authorization": "Bearer MY_SECRET_TOKEN"  # Replace with your actual token
}

# Send a GET request with the Bearer token
response = requests.get(url, headers=headers)

# Print response status and body
print(f"Status Code: {response.status_code}")
# print("Response:", response.json())  # Use .text if the response isn't JSON
