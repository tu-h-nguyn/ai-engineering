import os
import sys
from dotenv import load_dotenv

# 1. Nạp các biến từ file .env vào os.environ
# Hàm này tự động tìm file .env ở thư mục hiện tại hoặc các thư mục cha
load_dotenv()

def verify_key(name: str) -> None:
    value = os.getenv(name)
    if not value:
        print(f"[-] {name:<20}: THIẾU (Chưa được cấu hình trong .env)")
    else:
        # Ẩn bớt ký tự để bảo mật (chỉ hiện 4 ký tự đầu và 4 ký tự cuối)
        masked = value[:4] + "*" * (len(value) - 8) + value[-4:] if len(value) > 8 else "***"
        print(f"[+] {name:<20}: ĐÃ TẢI ({masked})")

def main() -> None:
    print("=== KIỂM TRA BIẾN MÔI TRƯỜNG & API KEYS ===")
    keys = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GEMINI_API_KEY",
        "HUGGINGFACE_TOKEN"
    ]
    for key in keys:
        verify_key(key)
    print("==========================================")

if __name__ == "__main__":
    main()
