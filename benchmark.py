import torch
import time

size = 5000

print(f"Khởi tạo ma trận kích thước {size}x{size} trên CPU...")
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

# 1. Đo thời gian trên CPU
start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"Thời gian chạy trên CPU : {cpu_time:.3f}s")

# 2. Đo thời gian trên GPU
if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")
    
    # Warm-up GPU và đồng bộ hóa trước khi bấm giờ
    torch.cuda.synchronize()
    start = time.time()
    
    c_gpu = a_gpu @ b_gpu
    
    # Bắt buộc gọi synchronize: các thao tác CUDA chạy bất đồng bộ (asynchronous).
    # Không có synchronize(), timer sẽ dừng trước khi GPU tính xong.
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    
    print(f"Thời gian chạy trên GPU : {gpu_time:.3f}s")
    print(f"Tốc độ tăng tốc (Speedup): {cpu_time / gpu_time:.1f}x")
