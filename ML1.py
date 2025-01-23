from scipy.io import loadmat

mnist_raw=loadmat("mnist-original.mat")

print(mnist_raw)

from scipy.io import loadmat

mnist_raw=loadmat("mnist-original.mat")

print(mnist_raw)

mnist={    
    "data":mnist_raw["data"].T,
    "label":mnist_raw["label"][0]
}

x,y=mnist["data"],mnist["label"]

print("y shape ",y.shape)
