import datasets
from torch.utils.data import DataLoader

# Load dataset
ossia = datasets.load_dataset("ductai199x/open-set-synth-img-attribution", "arch")

# Use it
dataloader = DataLoader(ossia["train"], batch_size=32, shuffle=True)
for batch in dataloader:
    # training loop ...
    pass