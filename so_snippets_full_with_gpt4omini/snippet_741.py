# Extracted from https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu
torch.cuda.is_available()

torch.rand(10).to(device)

RuntimeError: CUDA error: no kernel image is available for execution on the device

