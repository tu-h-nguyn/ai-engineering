import torch
import time

size = 5000
print(f"Khoi tao 2 ma tran vuong kich thuoc {size}x{size}...")
a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

# 1. Chay tren CPU
start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"Thoi gian CPU : {cpu_time:.3f}s")

# 2. Chay tren GPU RTX 3050
if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")
    
    # Dong bo CUDA truoc khi bam gio
    torch.cuda.synchronize()
    start = time.time()
    
    c_gpu = a_gpu @ b_gpu
    
    # Dong bo CUDA sau khi tinh xong de do chinh xac
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    
    print(f"Thoi gian GPU : {gpu_time:.3f}s")
    print(f"Toc do tang toc (Speedup): {cpu_time / gpu_time:.1f}x")
else:
    print("Khong tim thay GPU CUDA!")
