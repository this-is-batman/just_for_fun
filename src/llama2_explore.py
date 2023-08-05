'''
pytorch_explore: Script to explore random pytorch code snippets present in llama2 to gain a deeper understanding
Here, we will be mostly exploring the different snippets of the llama2.c code given by Andrej
https://github.com/karpathy/llama2.c
All the codes are run on the CPU of a M2 Air
Author: Abhirup Gupta
'''

import torch
from dataclasses import dataclass

# this is a data class, which contains only arguments for the training data
# the init function is automatically added
# the data class is a very handy component of python
@dataclass
class ModelArgs:
    dim: int = 64
    n_layers: int = 12
    n_heads: int = 32
    vocab_size: int = -1
    max_seq_len: int = 24
    dropout: float = 0.0


# testing the RMS Norm function
x = torch.rand((2,2))
print("Testing RMSNorm: ")
print(x)
print(x * torch.rsqrt(x.pow(2).mean(-1, keepdim = True)) + 0.02) 

# here, -1 signifies the mean of the column values
# keepdim specifies that the dimensions before and after the mean operation should be similar
# the purpose of the RMS norm code is to normalize the input vector before multiplying with the weight matrix

# checking how the attention mask is created ( causal decoder attention mask)
mask = torch.full((1,1,12,12), float("-inf"))
mask = torch.triu(mask, diagonal=1)

'''
one important implementation specific thing in pytorch is the register buffer
https://discuss.pytorch.org/t/what-is-the-difference-between-register-buffer-and-register-parameter-of-nn-module/32723
Tldr: register buffers store those elements which should not be trained , but should be stored in the state_dict of the stored model
'''

print("\nTesting query, key, value vectors: ")
args = ModelArgs()
head_dim = args.dim // args.n_heads

# checking the linear layer
l1 = torch.nn.Linear(args.dim, args.n_heads * head_dim, bias = False)

# this is given as input to the attention layer
# this same operation will be carried out for key, query and value matrices in attention
x = torch.rand(2,args.max_seq_len,args.dim)
print(x.shape)
batch_size, seq_len, _ = x.shape

z = l1(x).view(batch_size, seq_len, args.n_heads, head_dim)
print(z.shape)
