import os
import requests
from dotenv import load_dotenv

load_dotenv()

def query_huggingface_status(token: str) -> None:
    """Kiểm tra tính hợp lệ của Hugging Face Token qua whoami endpoint."""
    url = "https://huggingface.co/api/whoami-v2"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            user_data = response.json()
            print(f"[+] Token hợp lệ! User: {user_data.get('name')}")
        elif response.status_code == 401:
            print("[-] Lỗi 401: Token không hợp lệ hoặc đã bị thu hồi.")
        elif response.status_code == 429:
            print("[-] Lỗi 429: Rate limit - Quá nhiều yêu cầu trong thời gian ngắn.")
        else:
            print(f"[-] Yêu cầu thất bại với status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Lỗi kết nối mạng: {e}")

if __name__ == "__main__":
    hf_token = os.getenv("HUGGINGFACE_TOKEN", "")
    print(f"Đang kiểm tra token: {hf_token[:6]}...")
    query_huggingface_status(hf_token)
