# python coding by 'hanter-xd official' team,
# code by [md rasel] the team owner,
# tolos by wifi speed test only...
import os
os.system("pip install colorama")
os.system("pip install speedtest-cli requests tqdm")
os.system("pip install speedtest-cli tqdm")
os.system("pip install speedtest-cli")
def clear():
    os.system("clear")
clear()
import speedtest
import requests
from tqdm import tqdm
import time
import random
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Function to generate random RGB colors
def random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"\033[38;2;{r};{g};{b}m"  # ANSI escape code for RGB


def get_ip_info():
    """Get public IP address and related information."""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        ip = data.get("ip", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        isp = data.get("org", "N/A")
        return ip, city, region, country, isp
    except Exception as e:
        print(f"Error fetching IP information: {e}")
        return "N/A", "N/A", "N/A", "N/A", "N/A"
logo=("""_    _ ___________ _____   ___________     _____ _____ _____ _____ 
| |  | |_   _|  ___|_   _| /  ___| ___ \   |_   _|  ___/  ___|_   _|
| |  | | | | | |_    | |   \ `--.| |_/ /_____| | | |__ \ `--.  | |  
| |/\| | | | |  _|   | |    `--. \  __/______| | |  __| `--. \ | |  
\  /\  /_| |_| |    _| |_  /\__/ / |         | | | |___/\__/ / | |  
 \/  \/ \___/\_|    \___/  \____/\_|         \_/ \____/\____/  \_/  """)
def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    # Display IP and ISP Information
    ip, city, region, country, isp = get_ip_info()
    print(logo)
    print(f"\n{random_color()}--- Wi-Fi user public customer info ---\n")
    print(f"{random_color()}Public IP Address: {ip}")
    print(f"{random_color()}Location: {city}, {region}, {country}")
    print(f"{random_color()}ISP: {isp}\n")

    # Download speed test
    print(f"{random_color()}Testing download speed...")
    download_speed = st.download()
    for _ in tqdm(range(100), desc="Download Progress", unit="%", ncols=75):
        time.sleep(0.05)  # Delay for progress bar
    download_speed_mbps = download_speed / 1e+6  # Convert to Mbps

    # Upload speed test
    print(f"\n{random_color()}Testing upload speed...")
    upload_speed = st.upload()
    for _ in tqdm(range(100), desc="Upload Progress", unit="%", ncols=75):
        time.sleep(0.05)  # Delay for progress bar
    upload_speed_mbps = upload_speed / 1e+6  # Convert to Mbps

    # Display results
    print(f"\n{random_color()}--- Speed Test Results ---")
    print(f"{random_color()}Download Speed: {download_speed_mbps:.2f} Mbps")
    print(f"{random_color()}Upload Speed: {upload_speed_mbps:.2f} Mbps")

if __name__ == "__main__":
    run_speed_test()