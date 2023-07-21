# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['plot_images', 'get_device']

# %% ../nbs/00_core.ipynb 2
import gc
import torch
import matplotlib.pyplot as plt

# %% ../nbs/00_core.ipynb 4
def plot_images(images, rows=1, columns=5):
    fig, ax = plt.subplots(rows, columns, figsize=(18, 6))
    for i, image in enumerate(images):
        ax[i].imshow(image)

# %% ../nbs/00_core.ipynb 5
def get_device():
    if torch.cuda.is_available(): device = 'cuda'
    else: device = 'cpu'
    return device