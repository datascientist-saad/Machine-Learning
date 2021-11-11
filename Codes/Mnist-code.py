from sklearn.datasets import fetch_openml
# import pandas as pd

mnist = fetch_openml('mnist_784')

x = mnist.data.shape
y = mnist.target.shape

print("Shape of data", x)
print("Shape of target", y)